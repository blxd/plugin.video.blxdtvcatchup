import re
from xbmcswift2 import Plugin
from operator import itemgetter
import urllib2

CHANNEL_MAP = {1: "BBC One"}
plugin = Plugin()

M3U8_PATTERN = re.compile(r"\"(http://.*m3u8.*clientKey=[^\"]*)\";")

def http_get(url):
    req = urllib2.Request(url)
    try:
        page = urllib2.urlopen(req)
    except urllib2.HTTPError, e:
        print e.fp.read()
        raise

    return page


@plugin.route('/')
def index():
    return [{'label': name,
             'path': plugin.url_for('play_stream', stream_id=cid),
             'is_playable': True,
             'thumbnail': 'http://tvcatchup.com/tvc-static//images/channels/v3/{0}.png'.format(cid)}
            for cid, name in sorted(CHANNEL_MAP.items(), itemgetter(0))]


@plugin.route('/stream/<stream_id>')
def play_stream(stream_id):
    stream_id = int(stream_id)
    channel_name = CHANNEL_MAP[stream_id]

    wurl = "http://tvcatchup.com/watch/{0}".format(stream_id)
    plugin.log.debug("Getting watch url: {0}".format(wurl))
    page = http_get(wurl)
    content = page.read()

    m3u8_match = M3U8_PATTERN.search(content, re.IGNORECASE | re.MULTILINE)

    if m3u8_match:
        stream_url = m3u8_match.group(1)
        plugin.log.info("Loading streaming URL: {0}".format(stream_url))
        plugin.set_resolved_url(stream_url)
    elif "intended geographic area this channel" in content:
        plugin.notify("The channel \"{0}\" is not available from this country".format(channel_name))
        plugin.log.error("The channel \"{0}\" (stream_id={1}) is not "
                         "available from this country".format(channel_name, stream_id))
    else:
        plugin.notify("The channel \"{0}\" is not currently available".format(channel_name))
        plugin.log.error("An unknown error occurred")


if __name__ == '__main__':
    plugin.run()

