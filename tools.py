import webview as wb
import  flask
from flask_cors import CORS
import os
import threading as trd


class Window:

    def __init__(self, title, url=None, html=None, api=None):
        self.window = wb.create_window(title, url, html, js_api=api)
        self.app = flask.Flask(__name__)
    
    def start(self, icon="", gui="", func=None):
        wb.start(func, icon=icon, gui=gui, debug=True, http_server=False)


class Thread:

    def __init__(self):
        self.thread = []

    def add(self, func, args="__NO_ARGUMENT__", join=True):
        if args != "__NO_ARGUMENT__":
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

