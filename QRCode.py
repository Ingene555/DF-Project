import os
import sys
import webview
import time
import datetime as dt
import flask
import mainFunctions as mf
import tools
from werkzeug.utils import secure_filename

sys.path.append("QRCode")
import qr


class MainApp(tools.Window):

    def __init__(self, title, url=None, html=None, api=None):
        global APP
        tools.Window.__init__(self, title, url, html, api)
        self.window.min_size = (500, 500)


class API:

    def newQr(self, param={}):
        try:
            q = qr.LinkToImg("").Convert([param.get("link")], [], param)
            inp = fr'{mf.Return(q[0]).getValues(0)}'.replace("\\", "/")
            
            filename = secure_filename(os.path.basename(inp))
            save_path = os.path.join(tools.APP.config["UPLOAD_FOLDER"], filename)
            os.rename(inp, save_path)
            return {"isOk":True, "link": f"http://127.0.0.1:5555/static/img/{filename}"}
        except:
            return {"isOK": False, "link":None}

    def saveQr(self, param={}):
        if True:
            def t(*args):
                None
            q = qr.LinkToImg(param.get("link")).toIMG(param.get("path"), param, t, False)
            if mf.Return(q[0]).getSucced():
                return {"isOk": True, "link": fr"{mf.Return(q[0]).getValues(0)}".replace("\\", "/")}
            else:
                return {"isOk": False}
        else:
            return {"isOk": False}
    
    def saveAs(self):
        dir = main.window.create_file_dialog(webview.SAVE_DIALOG, "Pictures", False, "qrcode.png",
                                       (
                                        "PNG File (*.png)",
                                        "BMP File (*.bmp)",
                                        "GIF File (*.gif)",
                                        "JPG File (*.jpg)",
                                        "JPEG File (*.jpeg)",
                                        "SVG File (*.svg)",
                                        "TIF File (*.tif)",
                                        "TIFF File (*.tiff)",
                                        "WEBP File (*.webp)"
                                        ))
        if dir:
            return {"selected": True, "direction": dir}
        else:
            return {"selected":False}

    def checkPath(self, path):
        p = os.path.dirname(path)
        if os.path.exists(p):
            return {"path": True}
        else:
            return {"path": False}

    def openTextFile(self):
        dir = main.window.create_file_dialog(webview.OPEN_DIALOG, "documents", False, 
                                       file_types=("TEXT File (*.txt)",
                                                   "ALL File(*.*)"))
        if dir:
            try:
                with open(dir[0], "r", encoding="utf-8") as f:
                    text = f.read()
                return {"selected":True, "text": text}
            except Exception as e:
                print(e)
                return {"selected": False, "why":"MISTAKE"}
        else:
            return {"selected": False}

    def openLogo(self):
        dir = main.window.create_file_dialog(webview.OPEN_DIALOG, "Pictures",
                                             file_types=("Image File (*.png;*.bmp;*.gif;*.jpg;*.jpeg;*.svg;*.tif;*.tiff;*.webp)",
                                                         "All Files (*.*)"))
        if dir:
            return {"selected": True, "path":dir[0].replace("\\", "/"), "name": os.path.basename(dir[0])}
        else:
            return {"selected": False}


if __name__ == "__main__":
    # mf.run_as_admin
    mf.clearDirectory("tempcaches")
    mf.clearDirectory("static/img")
    main = MainApp("DPlayer", url="QRCode/QRCode.html", api=API())
    tools.serverRequierement()
    
    UPLOAD_FOLDER = os.path.join(tools.APP.root_path, "static", "img")
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)
    tools.APP.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
    
    @tools.APP.route('/static/img/<filename>')
    def serve_image(filename):
        return flask.send_from_directory(tools.APP.config["UPLOAD_FOLDER"], filename)
    
    thread = tools.Thread()
    thread.add(tools.startToolsFlask, join=False)
    thread.start()
    sys.exit(main.start(gui="edgechromium"))
