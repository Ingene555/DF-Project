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

class API:
    def fullscreen(self):
        main.window.toggle_fullscreen()
        fw, fh = GetSystemMetrics(0), GetSystemMetrics(1)
        wdt, hgt = main.window.width, main.window.height
        screen_size = fw==wdt and fh==hgt 
        return {"message": screen_size}


if __name__ == "__main__":
    # mf.run_as_admin
    mf.clearDirectory("tempcaches")
    main = MainApp("DPlayer", url="D-Player/DPlayer.html", api=API())
    tools.serverRequierement()
    
    thread = tools.Thread()
    thread.add(tools.startToolsFlask, join=False)
    thread.start()
    sys.exit(main.start(gui="edgechromium"))
