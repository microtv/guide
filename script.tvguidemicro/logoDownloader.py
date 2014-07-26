import xbmc
import xbmcaddon
import download
import extract
import base64


ADDON  = xbmcaddon.Addon(id = 'script.tvguidemicro')
datapath = xbmc.translatePath(ADDON.getAddonInfo('profile'))
extras   = os.path.join(datapath, 'extras')
logos    = os.path.join(extras, 'logos')
nologos  = os.path.join(logos, 'None')
dest     = os.path.join(extras, 'logos.zip')
url      = base64.b64decode('aHR0cDovL3N0YXRpYy5wbmdyb3VwLmluZm8vX2d1aWRlL2xvZ29zLnppcA==')


try:
    os.makedirs(logos)
    os.makedirs(nologos)
except:
    pass

download.download(url, dest)
extract.all(dest, extras)

try:
    os.remove(dest)
except:
    pass
