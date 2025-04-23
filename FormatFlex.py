
import sys
import mainFunctions as mf
import tools
from webview.dom import DOMEventHandler
import DExplorer as Dp
import os
import flask
from werkzeug.utils import secure_filename
import shutil
import pickle as pkl
from datetime import datetime as dt



sys.path.append("FormatFlex")
import fftools as ft

STATIC = "http://127.0.0.1:5555/static/FormatFlex"
STATIC_FOLDER = "static/FormatFlex"
TEMPCACHES = "tempcaches"
Dp.STATIC = STATIC
OPEN_QUEUE = ft.Queu(1)
SAVE_QUEU = ft.Queu(1)
OPERATION = {}
HIST = "FormatFlex/formatflex.dexp"

def on_drag(e):
    pass
def on_drop(e):
    files = e['dataTransfer']['files']
    if len(files) == 0:
        return
    l=[ww.get("pywebviewFullPath").replace("\\", "/") if os.path.exists(ww.get("pywebviewFullPath")) else ww for ww in files]
    OPEN_QUEUE.get()
    OPEN_QUEUE.put(l)
def bind():
    main.window.dom.document.events.dragenter += DOMEventHandler(on_drag, True, True)
    main.window.dom.document.events.dragstart += DOMEventHandler(on_drag, True, True)
    main.window.dom.document.events.dragover += DOMEventHandler(on_drag, True, True, debounce=500)
    main.window.dom.document.events.drop += DOMEventHandler(on_drop, True, True)

def setfhist():
    if not os.path.exists(HIST):
        with open(HIST, "wb") as f:
            pkl.dump({}, f)
    try:
        with open(HIST, "rb") as f:
            a = pkl.load(f)
        if type(a)!=dict:
            with open(HIST, "wb") as f:
                pkl.dump({}, f)
    except:
        with open(HIST, "wb") as f:
            pkl.dump({}, f)
            
def addInHist(title, details, output):
    setfhist()
    with open(HIST, "rb") as f:
        data = pkl.load(f)
    d = {"input": {"title": title, "details": details},
                 "output": output,
                 "date": str(dt.date(dt.now())),
                 "cible": title+str(dt.now())}
    data[d["cible"]] = d
    with open(HIST, "wb") as f:
        pkl.dump(data, f)

def readHist():
    setfhist()
    with open(HIST, "rb") as f:
        dt = pkl.load(f)
    return dt

def removeFromHist(title):
    setfhist()
    with open(HIST, "rb") as f:
        dt = pkl.load(f)
    if title in dt.keys():
        del(dt[title])
    with open(HIST, "wb") as f:
        pkl.dump(dt, f)


class MainApp(tools.Window):

    def __init__(self, title, url=None, html=None, api=None, picture=None):
        global APP
        tools.Window.__init__(self, title, url, html, api)
        self.window.min_size = (1000, 500)

class API:
    def __init__(self):
        dp = Dp.API()
        Dp.EXTERNAL_FUNC = self.externalFunc
        Dp.IS_IT_USED = True
        Dp.STATIC_FOLDER = STATIC_FOLDER
        self.setLibDir = dp.setLibDir
        self.askCopy = dp.askCopy
        self.askDelete = dp.askDelete
        self.askNew = dp.askNew
        self.askRename = dp.askRename
        self.openSaveCancel = dp.openSaveCancel
        self.runFile = dp.runFile
        self.searchFile = dp.searchFile
    
    def externalFunc(self, method, list_=[]):
        if method=="OPEN":
            OPEN_QUEUE.get()
            OPEN_QUEUE.put(list_)
            main.window.run_js("FFmodalMethod();")
        elif method=="SAVE":
            SAVE_QUEU.get()
            SAVE_QUEU.put(list_)
            main.window.run_js("FFmodalMethod();")
        else:
            print(method)

    def ffSetFormItem(self, listOfExt):
        return {"data": ft.FFsetFormItem(listOfExt) if len(listOfExt)>0 else []}

    def checkDir(self, dir):
        check = False
        if(os.path.isdir(dir)):
            check = True
        else:
            dr = os.path.dirname(dir)
            if os.path.exists(dr):
                check = True
        return {"check": check}
    
    def askQueu(self):
        open = OPEN_QUEUE.get()
        save = SAVE_QUEU.get()
        opname = []
        if open:
            for ww in open:
                opname.append({"name":os.path.basename(ww), "path": ww, "dir": os.path.dirname(ww)})
        return {"open": open, "save": save, "opname": opname}

    def verifyDrop(self, drop):
        l = OPEN_QUEUE.get()
        while not l:
            l = OPEN_QUEUE.get()
        queu = [ww.lower() for ww in l]
        drop = [ww.lower() for ww in drop]
        data = []
        ok = False
        if(len(queu)==len(drop)):
            ok=True
            for ww in queu:
                if not os.path.basename(ww) in drop:
                    ok=False
                    break
                data.append({"name": os.path.basename(ww), "path": ww})
        return {"ok": ok, "data": data}
    
    def askAllModalExt(self, ext = "*"):
        data=[]
        for ww in ft.LIST:
            d={
                "cible": ww["name"],
                "list": ww["ext"],
                "text": ww["name"].capitalize()+" files ("
            }
            d["list"].sort()
            d["text"]+= "".join(["*.{}".format(e) for e in d["list"]])+")"
            data.append(d)
        return {"data": data}

    def askInfo(self, target):
        data = []
        dir = os.listdir(target) if os.path.isdir(target) else [target]
        der = [f"{target}/{ww}" for ww in os.listdir(target)] if os.path.isdir(target) else [target]
        for xx, ww in enumerate(dir):
            if not os.path.isdir(ww):
                preview = False
                path = der[xx]
                if Dp.getKind(ww.split(".")[-1].lower().strip()) in ["audio", "video", "image", "text", "pdf", "html"]:
                    filename = secure_filename(os.path.basename(ww))   
                    if Dp.getKind(ww.split(".")[-1].lower().strip())=="image":
                        save_path = os.path.join(tools.APP.config["UPLOAD_FOLDER"], filename)
                        if not os.path.exists(save_path):
                            try:
                                shutil.copyfile(der[xx], save_path)
                            except:pass
                    preview = f"{STATIC}/{filename}"
                    
                stat = os.stat(ww) if os.path.exists(ww) else None
                ext = ww.split(".")[-1].lower().strip()
                data.append({"cible":path,
                            "preview": preview,
                            "name": os.path.basename(ww),
                            "checked": True if ft.getKind(ext) in [k["name"] for k in ft.LIST] else False,
                            "size": Dp.convertOct(stat.st_size if stat else 0),
                            "ext": ext,
                            "type": ft.getKind(ext)
                            })
        return {"data": data}

    def askShowPreview(self, target):
        try:
            filename = secure_filename(os.path.basename(target))
            save_path = os.path.join(tools.APP.config["UPLOAD_FOLDER"], filename)
            if not os.path.exists(save_path):
                shutil.copyfile(target, save_path)
            return {"op": True}
        except:
            return {"op": False}
    
    def askClearStatic(self):
        mf.clearDirectory(STATIC_FOLDER)
    
    def convertThis(self, this):
        def _(x):
            main.window.run_js(x)
        convert = ft.Convert(this, _, addInHist)
        trd = tools.Thread()
        trd.add(convert.convert, join=False)
        trd.start()
        ps = convert.ps()
        OPERATION[ps[0]] = ps[1]
        main.window.run_js(ps[2])
    
    def cancelProgress(self, id):
        OPERATION[id].kill()

    def askHist(self):
        a = readHist()
        l = []
        for ww in a.keys():
            l.append(a[ww])
        return {"data": l}

    def removeHist(self, title):
        removeFromHist(title)


if __name__ == "__main__":
    mf.clearDirectory(STATIC_FOLDER)
    ft.setTC()
    ft.clearAllTC()
    def t(*args):
        main.window.run_js(f"console.log([{args}])")
    ft.setPS(t)
    with open("D-Explorer/DExplorer.html", "r", encoding="utf-8") as f:
        de = f.read()
    with open("FormatFlex/FormatFlex.html","r", encoding="utf-8") as f:
        ff = f.read()
    
    main = MainApp("FormatFlex", html=ff.replace('***HERE***', de), api=API())
    Dp.main = main
    tools.serverRequierement()
    
    UPLOAD_FOLDER = os.path.join(tools.APP.root_path, "static", "FormatFlex")
    os.makedirs(UPLOAD_FOLDER, exist_ok=True) 
    tools.APP.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
    
    @tools.APP.route('/static/FormatFlex/<filename>')
    def serve_image(filename):
        return flask.send_from_directory(tools.APP.config["UPLOAD_FOLDER"], filename)

    thread = tools.Thread()
    thread.add(tools.startToolsFlask, join=False)
    thread.start()
    sys.exit(main.start(gui="edgechromium", func=bind))
