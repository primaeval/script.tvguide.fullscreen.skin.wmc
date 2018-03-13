import xbmc,xbmcgui,xbmcaddon

SKINS = [["WMC", "WMC"]]


d = xbmcgui.Dialog()
names = [s[0] for s in SKINS]
skin = d.select("TV Guide Fullscreen - Set Default Skin", names)
if skin > -1:
    tvgf = xbmcaddon.Addon("script.tvguide.fullscreen")
    if tvgf:
        tvgf.setSetting('skin.source', '2')
        tvgf.setSetting('skin.folder', 'special://home/addons/script.tvguide.fullscreen.skin.wmc/')
        tvgf.setSetting('skin.user', SKINS[skin][1])
        tvgf.setSetting('action.bar', 'true')
        tvgf.setSetting('down.action', 'true')
        tvgf.setSetting('channels.per.page', '10')
        tvgf.setSetting('epg.box.spacing', '2')
        tvgf.setSetting('epg.focus.color', '[COLOR ffffffff]white[/COLOR]')
        tvgf.setSetting('epg.nofocus.color', '[COLOR ffffffff]white[/COLOR]')
        tvgf.setSetting('timebar.color', '[COLOR ff87ceeb]skyblue[/COLOR]')
        tvgf.setSetting('categories.background.color', '[COLOR ff4682b4]steelblue[/COLOR]')
        tvgf.setSetting('epg.font', 'font13')
        tvgf.setSetting('up.cat.mode', 'First Channel')
        tvgf.setSetting('date.custom', 'true')
        tvgf.setSetting('date.custom.format', '{dt:%a %b} {dt.day}')
        tvgf.setSetting('program.background.image', 'special://home/addons/script.tvguide.fullscreen.skin.wmc/resources/skins/WMC/media/background.jpg')
        tvgf.setSetting('program.background.image.source', '1')
        tvgf.setSetting('epg.subtitle', 'true')
		
		

