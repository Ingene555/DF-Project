import os
import sys
import webview
import time
import datetime as dt
import flask
from win32api import GetSystemMetrics as gsm
import mainFunctions as mf
import tools



class MainApp(tools.Window):

    def __init__(self, title, url=None, html=None, api=None, text=None):
        global APP
        tools.Window.__init__(self, title, url, html, api)
        self.window.min_size = (700, 500)


class API:
    def setName(self, name):
        main.window.set_title("Dpdf | "+name)

if __name__ == "__main__":
    mf.clearDirectory("tempcaches")
    api = API()
    main = MainApp("Dpdf", url="D-PDF/DPDF.html", api=api)
    tools.serverRequierement()
    def openPdf():
        main.window.run_js("openPDF();")
    thread = tools.Thread()
    thread.add(tools.startToolsFlask, join=False)
    thread.add(openPdf, join=False)
    thread.start()
    sys.exit(main.start())
