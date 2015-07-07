from urllib import quote

from xbmcswift2 import Plugin

CHANNEL_LIST = {
    1: ("BBC One", "http://tvcatchup.com/watch/bbcone"),
    2: ("BBC Two", "http://tvcatchup.com/watch/bbctwo"),
    3: ("ITV", "http://tvcatchup.com/watch/itv"),
    4: ("Channel 4", "http://tvcatchup.com/watch/channel4"),
    5: ("Channel 5", "http://tvcatchup.com/watch/channel5"),
    17: ("BBC News", "http://tvcatchup.com/watch/bbcnews"),
    18: ("CBBC", "http://tvcatchup.com/watch/cbbc"),
    24: ("CBeeBies", "http://tvcatchup.com/watch/cbeebies"),
    12: ("BBC3", "http://tvcatchup.com/watch/bbc3"),
    13: ("BBC4", "http://tvcatchup.com/watch/bbc4"),
    501: ("MillenniumTV", "http://tvcatchup.com/watch/millenniumtv"),
    73: ("Quest", "http://tvcatchup.com/watch/quest"),
    37: ("VIVA", "http://tvcatchup.com/watch/viva"),
    31: ("BBC Parliament", "http://tvcatchup.com/watch/bbcparliament"),
    78: ("RT", "http://tvcatchup.com/watch/rt"),
    65: ("BBC Red Button", "http://tvcatchup.com/watch/bbcredbutton"),
    95: ("Gala TV", "http://tvcatchup.com/watch/galatv"),
    151: ("Sail TV", "http://tvcatchup.com/watch/sailtv"),
    177: ("Sub TV", "http://tvcatchup.com/watch/subtv"),
    158: ("Community Channel", "http://tvcatchup.com/watch/communitychannel"),
    144: ("S4C", "http://tvcatchup.com/watch/s4c")
}

plugin = Plugin()


@plugin.route('/')
def index():
    return [{'label': info[0],
             'path': "plugin://plugin.video.livestreamer/play?url={0}".format(quote(info[1])),
             'is_playable': True,
             'thumbnail': 'http://tvcatchup.com/tvc-static//images/channels/v3/{0}.png'.format(cid)}
            for cid, info in CHANNEL_LIST.items()]

if __name__ == '__main__':
    plugin.run()
