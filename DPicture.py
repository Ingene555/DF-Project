import os
import sys
import webview
import time
import datetime as dt
import flask
from win32api import GetSystemMetrics as gsm
import mainFunctions as mf
import tools
from win32api import GetSystemMetrics
sys.path.append("D-Picture")
import dp_asset

CURRENT_IMAGE = set()
ID = 0
APP = None
CURRENT_DIR = ""
IMAGE_DIR = []


class MainApp(tools.Window):

    def __init__(self, title, url=None, html=None, api=None, picture=None):
        global APP
        tools.Window.__init__(self, title, url, html, api)
        self.window.min_size = (500, 500)

        
class Api:

    def setUrl(self):
        main.window.load_url("http://127.0.0.1:5555/DPicture/madara.jpg")
        
    def unsetFullscreen(self):
        try:
            main.window.toggle_fullscreen()
        except:
            None
        return {"message": False}

    def setFullscreen(self):
        try:
            main.window.toggle_fullscreen()
        except:
            None
        fw, fh = GetSystemMetrics(0), GetSystemMetrics(1)
        wdt, hgt = main.window.width, main.window.height
        screen_size = fw==wdt and fh==hgt 
        return {"message": screen_size}

    def openFile(self):
        global CURRENT_IMAGE, CURRENT_DIR
        files_types = ('Image Files (*.bmp;*.gif;*.jpg;*.jpeg;*.ico;*.png;*.svg;*.tif;*.webp)',
                      'BMP Files (*.bmp)',
                      "GIF Files (*.gif)",
                      "JPG Files (*.jpg)",
                      "JPEG Files (*.jpeg)",
                      "ICO Files (*.ico)",
                      "PNG Files (*.png)",
                      "svg Files (*.svg)",
                      "TIF Files (*.tif)",
                      "WEBP Files (*.webp)")
        result = main.window.create_file_dialog(webview.OPEN_DIALOG, directory="Pictures", allow_multiple=True, file_types=files_types)
        if result:
            where = f"tempcaches/{dt.datetime.now()}".replace(":", "-")
            os.mkdir(where)
            CURRENT_DIR = where
            text = ""
            for ww, xx in enumerate(result):
                xx = xx.replace("\\", "/")
                name = xx.split("/")[-1]
                os.rename(xx, os.path.join(CURRENT_DIR, name))
                CURRENT_IMAGE.add(name)
                text += xx
                if(ww < len(result) - 1):
                    text += "::"
            return {"message": text}
        else:
            return {"message": None}


if __name__ == "__main__":
    # mf.run_as_admin
    mf.clearDirectory("tempcaches")
    main = MainApp("DPicture", html=dp_asset.asset)
    main.window._js_api = Api()
    tools.serverRequierement()
    main.window.events
    def openImg():
        main.window.run_js("openImageFile()")
    
    thread = tools.Thread()
    thread.add(tools.startToolsFlask, join=False)
    thread.add(openImg, join=False)
    thread.start()
    sys.exit(main.start())
