from operator import itemgetter
import sys
import xbmcgui
import xbmcplugin
import requests

if __name__ == "__main__":
    addon_handle = int(sys.argv[1])

    xbmcplugin.setContent(addon_handle, 'livetv')

    cache_url = "http://tvcatchup.com/cache.php"

    cache_data = requests.get(cache_url).json()

    for channel_id, channel_data in sorted(cache_data['channels'].items(), key=itemgetter(0)):

        data_url = "http://tvcatchup.com/stream.php"

        stream_data = requests.get(data_url, params=dict(chan=channel_id)).json()

        stream_url = stream_data.get('url')

        if stream_url:
            img_url = "http://tvcatchup.com/tvc-static//images/channels/v3/{0}.png".format(channel_id)
            li = xbmcgui.ListItem(str(channel_data['name']), iconImage=img_url)
            xbmcplugin.addDirectoryItem(handle=addon_handle, url=stream_url, listitem=li)

    xbmcplugin.endOfDirectory(addon_handle)
