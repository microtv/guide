import urllib,dxmnew,xbmc,xbmcgui,xbmcaddon,base64
ADDON  = xbmcaddon.Addon(id = 'script.tvguidemicro')

ooOOOoo = ''
def ttTTtt(i, t1, t2=[]):
	t = ooOOOoo
	for c in t1:
	  t += chr(c)
	  i += 1
	  if i > 1:
	   t = t[:-1]
	   i = 0  
	for c in t2:
	  t += chr(c)
	  i += 1
	  if i > 1:
	   t = t[:-1]
	   i = 0
	return t

dialog = xbmcgui.DialogProgress()
dialog.create('Please Wait.', 'Logo Pack Downloading...')
dialog.update(0)
datapath = xbmc.translatePath(ADDON.getAddonInfo('profile'))
Path=os.path.join(datapath,'extras')
try: os.makedirs(Path)
except: pass
Url = base64.b64decode('aHR0cDovL3N0YXRpYy5wbmdyb3VwLmluZm8vX2d1aWRlL2xvZ29zLnppcA==')
LocalName = 'logos.zip'
LocalFile = xbmc.translatePath(os.path.join(Path, LocalName))
dialog.update(33)
try: urllib.urlretrieve(Url,LocalFile)
except:xbmc.executebuiltin("XBMC.Notification(Micro TV Guide,Logo download failed,3000)")
dialog.update(66)
if os.path.isfile(LocalFile):
    extractFolder = Path
    pluginsrc =  xbmc.translatePath(os.path.join(extractFolder))
    dxmnew.unzipAndMove(LocalFile,extractFolder,pluginsrc)
    dialog.update(100)
    dialog.close()
    ok = xbmcgui.Dialog()
    ok.ok('Micro TV Guide', 'Logo Pack Download Complete')
try:os.remove(LocalFile)
except:pass
