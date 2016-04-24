import xbmc
import xbmcaddon
import download
import extract
import base64
import os

ADDON  = xbmcaddon.Addon(id = 'script.tvguidemicro')
datapath = xbmc.translatePath(ADDON.getAddonInfo('profile'))
extras   = os.path.join(datapath, 'extras')
logos    = os.path.join(extras, 'logos')
nologos  = os.path.join(logos, 'None')
dest     = os.path.join(extras, 'logos.zip')
url      = base64.b64decode('aHR0cDovL3d3dy5taWNyb3NpdGVzbWFsYWdhLmNvbS9fZ3VpZGUvbG9nb3Muemlw')


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
