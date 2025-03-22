import webview as wb
import  flask
from flask_cors import CORS
import time
import pickle as pkl
import os
import threading as trd
import sys
import mainFunctions as mf



class Window:

    def __init__(self, title, url=None, html=None, api = None):
        self.window = wb.create_window(title, url, html, js_api=api)
        self.app = flask.Flask(__name__)
    
    def getAll(self):
        return  {
            "title":self.window.title,
            "url":self.window.get_current_url(),
            "original_url":self.window.original_url,
            "html":self.window.html,
            "js_api":self.window._js_api,
            "width":self.window.width,
            "height":self.window.height,
            "initiale_width":self.window.initial_width,
            "initiale_height":self.window.initial_height,
            "x":self.window.x,
            "y":self.window.y,
            "initiale_x": self.window.initial_x,
            "initiale_y": self.window.initial_y,
            "screen":self.window.screen,
            "resizable":self.window.resizable,
            "fullscreen":self.window.fullscreen,
            "min_size":self.window.min_size,
            "hidden":self.window.hidden,
            "frameless":self.window.frameless,
            "easy_drag":self.window.easy_drag,
            "shadow":self.window.shadow,
            "focus":self.window.focus,
            "minimized":self.window.minimized,
            "maximazed":self.window.maximized,
            "on_top":self.window.on_top,
            "confirm_close":self.window.confirm_close,
            "background_color":self.window.background_color,
            "transparent":self.window.transparent,
            "text_select": self.window.text_select,
            "zoomable":self.window.zoomable,
            "draggable": self.window.draggable,
            "vibrancy": self.window.vibrancy,
            "localization": self.window.localization,
            "http_port":self.window._http_port,
            "server_args":self.window._server_args
        }

    def setAll(self, args={}):
        """
        title: str,
        url: str | None = None,
        html: str | None = None,
        js_api: Any = None,
        width: int = 800,
        height: int = 600,
        x: int | None = None,
        y: int | None = None,
        screen: Screen = None,
        resizable: bool = True,
        fullscreen: bool = False,
        min_size: tuple[int, int] = (200, 100),
        hidden: bool = False,
        frameless: bool = False,
        easy_drag: bool = True,
        shadow: bool = True,
        focus: bool = True,
        minimized: bool = False,
        maximized: bool = False,
        on_top: bool = False,
        confirm_close: bool = False,
        background_color: str = '#FFFFFF',
        transparent: bool = False,
        text_select: bool = False,
        zoomable: bool = False,
        draggable: bool = False,
        vibrancy: bool = False,
        localization: Mapping[str, str] | None = None,
        server: type[ServerType@create_window] = http.BottleServer,
        http_port: int | None = None,
        server_args: ServerArgs = {}
        """
        a = self.getAll() 
        for ww in range(len(a.keys())):
            try:
                exec(f'self.window.{list(a.keys())[ww]} = args.get(list(a.keys())[ww], list(a.values())[ww])')
            except Exception as e:print(e)
            finally:
                self.window.resize(args.get("width", a["width"]), args.get("height", a["height"]))
        return self.getAll()

    def start(self, icon = "", gui = ""):
        wb.start(icon=icon, gui=gui, debug=False, http_server=False)

class Thread:
    def __init__(self):
        self.thread = []
    def add(self, func, args="__NO_ARGUMENT__", join = True):
        if args!="__NO_ARGUMENT__":
            t = trd.Thread(target=func, args=args)
        else:
            t = trd.Thread(target=func)
        self.thread.append({"thread": t, "function":func, "args":args, "join":join})
        return t
    def start(self):
        for ww in self.thread:
            ww["thread"].start()
        for ww in self.thread:
            if ww["join"]:
                ww["thread"].join()

APP = None
BS_PATH = "bootstrap-5.3.3-dist"
BS_CSS_PATH = os.path.join(BS_PATH, "css")
BS_JS_PATH = os.path.join(BS_PATH, "js")
JQ_PATH = "jquery"
CSS_VARIABLE = "ressources/util"

def serverRequierement():
    global APP
    APP = flask.Flask(__name__)
    @APP.route(f"/{BS_PATH}/css/<filename>")
    def serve_bs_css(filename):
        return flask.send_from_directory(BS_CSS_PATH, filename)

    @APP.route(f"/{BS_PATH}/js/<filename>")
    def serve_bs_js(filename):
        return flask.send_from_directory(BS_JS_PATH, filename)

    @APP.route(f"/{JQ_PATH}/<filename>")
    def serve_jquery(filename):
        return flask.send_from_directory(JQ_PATH, filename)

    @APP.route(f"/{CSS_VARIABLE}/<filename>")
    def serve_var_css(filename):
        return flask.send_from_directory(CSS_VARIABLE, filename)


def startToolsFlask():
    global APP
    CORS(APP)
    return APP.run(host="127.0.0.1", port=5555)





