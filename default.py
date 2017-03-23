# -*- coding: utf-8 -*-
# please visit http://www.yttv.vn

import xbmc,xbmcgui,xbmcplugin,sys

plugin_handle = int(sys.argv[1])
xbmcplugin.setContent(plugin_handle, 'movies')
icon = xbmc.translatePath("special://home/addons/plugin.video.YTTV/icon.png")
	
def add_video_item(url, infolabels, img=''):
    #url = 'http://edge2.everyon.tv/etv2/'+url+'/BratuMarian.m3u8'
    # rtmp://edge2.everyon.tv/etv2/phd1003
    #url = 'rtmp://lm7.everyon.tv/ptv7/'+url+' live=1'
    #url = 'http://lm7.everyon.tv/ptv7/'+url+'/BratuMarian.m3u8'
    #url = 'http://edge2.everyon.tv/etv2sb/'+url+'.m3u8'
    if 'rtmp://' in url: url = url + ' live=1' 
    listitem = xbmcgui.ListItem(infolabels['title'], iconImage=img, thumbnailImage=img)
    listitem.setInfo('video', infolabels)
    listitem.setProperty('IsPlayable', 'false')
    xbmcplugin.addDirectoryItem(plugin_handle, url, listitem)
    return

add_video_item('http://210.211.108.67:1935/hytcc/hytcc.stream/playlist.m3u8',{ 'title': 'YTTV'}, "special://home/addons/plugin.video.YTTV/icon/Logo YTTV Final.png")
add_video_item('rtmp://tv.kgtv.vn/livepkgr/kgtv?adbe-live-event=liveevent',{ 'title': 'Kiên giang'}, "special://home/addons/plugin.video.YTTV/icon/Kien_Giang_TV.png")
add_video_item('rtmp://tv.kgtv.vn:1935/livepkgr/kgtv1?adbe-live-event=liveevent',{ 'title': 'Kiên giang 1'}, "special://home/addons/plugin.video.YTTV/icon/KG.png")
add_video_item('http://210.211.108.67:1935/vtsic/vtsic.stream/playlist.m3u8',{ 'title': 'Trực tiếp Kiên giang 2'}, "special://home/addons/plugin.video.YTTV/icon/Logo YTTV Final.png")
add_video_item('http://210.211.108.67:1935/dn/_definst_/v_dn2.stream/playlist.m3u8',{ 'title': 'Đồng Nai 2'}, "special://home/addons/plugin.video.YTTV/icon/Dong_Nai_TV2.png")
add_video_item('http://210.211.108.67:1935/dn/_definst_/htvmuasam.stream/playlist.m3u8',{ 'title': 'HTV Shopping'}, "special://home/addons/plugin.video.YTTV/icon/HTVC_Shopping.png")

#add_video_item('rtmp://edge1.everyon.tv/etv1sb/phd765',{ 'title': 'Viki Premium'}, icon)
#add_video_item('rtmp://edge1.everyon.tv/etv1sb/phd497',{ 'title': 'Playboy'}, icon)
#add_video_item('http://edge2.everyon.tv/etv2/phd1003/BratuMarian.m3u8',{ 'title': 'Korea JAV TV'}, icon)
xbmcplugin.endOfDirectory(plugin_handle)
sys.exit(0)

