import os
from pathlib import Path
import sys
import datetime as dt
import flask
import mainFunctions as mf
import tools
from werkzeug.utils import secure_filename
import shutil
import subprocess as spss
import send2trash as s2t
import shutil


def convertOct(value):
    units = ["B", "KB", "MB", "GB", "TB", "PB"]
    size = float(value)
    
    i = 0
    while size >= 1024 and i < len(units) - 1:
        size /= 1024
        i += 1
    
    return f"{size:.2f} {units[i]}"


def convertDate(timestamp):
    return [dt.datetime.fromtimestamp(timestamp).strftime("%m / %d / %Y"), dt.datetime.fromtimestamp(timestamp).strftime("%Y-%m-%dT%H:%M:%S.%f")]


def getKind(ext):
    ext = ext.lower()
    if ext in ["png", "jpg", "jpeg", "bmp", "gif", "tif", "tiff", "ico", "webp"]:
        kind = "image"
    elif ext in ["aac", "aif", "wav", "mp3", "m4a", "flac"]:
        kind = "audio"
    elif ext in ["3go", "avi", "flv", "mkv", "mov", "mp4", "wmv", "webm"]:
        kind = "video"
    elif ext in ["txt"]:
        kind = "text"
    elif ext in ["pdf"]:
        kind = "pdf"
    elif ext in ["doc", "docx", "dot", "dotx", "rft"]:
        kind = "word"
    elif ext in ["xls", "xlsx", "xlt", "xlstx", "csv", "xlsb", "xlsm"]:
        kind = "excel"
    elif ext in ["odp", "pot", "potx", "ppt", "pptx", "pps", "ppsx"]:
        kind = "pwp"
    elif ext in ["htm"]:
        kind = "html"
    elif ext in ["jsp"]:
        kind = "java"
    elif ext in ["mjs", "cjs"]:
        kind = "js"
    elif ext in ["phtml", "phps"]:
        kind = "php"
    elif ext in ["pyc", "pyo", "pyd"]:
        kind = "py"
    elif ext in ["ada", "adb", "ads", "asm", "s", "bas", "vb", "cpp", "cc", "cxx",
                 "hpp", "hxx", "clj", "cljs", "cljc", "coffee", "cr",
                 "d", "di", "dart", "ex", "exs", "erl", "hrl", "fs", "fsx", "fsi",
                 "go", "groovy", "hs", "lhs",
                 "jl", "kt", "kts", "lua", "m", "mm", "nim",
                 "pas", "pp", "p", "pl", "pm", "t", "pro",
                 "pl", "ps1", "psm1", "psd1", "r", "rmd",
                 "rb", "erb", "rake", "rs", "scala", "scm", "ss", "sh", "bash", "zsh",
                 "swift", "ts", "tsx", "vb", "vbs", "v", "vh", "yaml", "yml"]:
        kind = "code"
    elif ext in ["zip", "rar", "7z", "tar", "gz", "bz2", "xz", "z", "lz", "lzma",
                 "lzo", "iso", "jar", "war", "xpi",
                 "crx", "arj", "zst"]:
        kind = "archive"
    else:
        kind = ext
    return kind


def get_folder_category(path):
    home = Path.home()
    paths = {
        "desktop": home / "Desktop",
        "downloads": home / "Downloads",
        "documents": home / "Documents",
        "music": home / "Music",
        "pictures": home / "Pictures",
        "videos": home / "Videos"
    }
    path = Path(path).resolve()
    for category, folder_path in paths.items():
        try:
            if os.path.commonpath([path, folder_path]) == str(folder_path):
                return category
        except:
            pass
    return "c"
 
 
def search(path, name):
    whatIFound = []
    name = name.lower()
    if os.path.exists(path):
        for root, dirs, files in os.walk(path):
            for file in files:
                if name in file.lower():
                    whatIFound.append(os.path.join(root, file).replace("\\", "/"))
            for dir in dirs:
                if name in dir.lower():
                    whatIFound.append(os.path.join(root, dir).replace("\\", "/"))
    return whatIFound


class MainApp(tools.Window):

    def __init__(self, title, url=None, html=None, api=None):
        global APP
        tools.Window.__init__(self, title, url, html, api)
        self.window.min_size = (900, 600)


class API:

    def getLibDir(self):
        home = Path.home()
        paths = {
            "c": "C:/",
            "desktop": str(home / "Desktop").replace("\\", "/"),
            "downloads": str(home / "Downloads").replace("\\", "/"),
            "documents": str(home / "Documents").replace("\\", "/"),
            "music": str(home / "Music").replace("\\", "/"),
            "pictures": str(home / "Pictures").replace("\\", "/"),
            "videos": str(home / "Videos").replace("\\", "/")
        }
        return paths

    def setLibDir(self, lib, setLD=True, parent=False):
        data = {"data":{}}
        data["category"] = get_folder_category(lib)
        data["dir"] = dir = self.getLibDir()[lib] if setLD else lib if os.path.exists(lib) else self.getLibDir()["c"]
        if parent:data["dir"] = dir = os.path.dirname(dir)
        for ww in os.listdir(dir):
            icon = False
            file_path = os.path.abspath(os.path.join(dir, ww))
            if not os.path.isdir(file_path) and file_path.split(".")[-1].lower() in ["png", "jpg", "jpeg", "bmp", "gif", "tif", "tiff", "webp", "ico"]:
                filename = secure_filename(os.path.basename(ww)) 
                save_path = os.path.join(tools.APP.config["UPLOAD_FOLDER"], filename)
                if not os.path.exists(save_path):
                    shutil.copyfile(file_path, save_path)
                icon = f"http://127.0.0.1:5555/static/img/{filename}"
            
            stat = os.stat(file_path) if os.path.exists(file_path) else None
            temps = convertDate(stat.st_mtime if stat else 0)
            data["data"][ww] = {"name":ww,
                        "isDir": os.path.isdir(file_path),
                        "date": temps[0],
                        "brutDate": temps[1],
                        "size": convertOct(stat.st_size if stat else 0),
                        "brutSize": stat.st_size if stat else 0,
                        "icon": icon,
                        "path": dir,
                        "type": getKind(file_path.split(".")[-1].lower()) if "." in os.path.basename(file_path) else ""
                        }
        return data

    def runFile(self, file):
        epath = "D-Explorer/explorer.dexp"
        if not os.path.exists(epath):
            mf.writeType(epath, {"history":[]})
        ret = mf.readType(epath)
        dexp = ret["values"] if ret["bool"] else {"history":[]}
        hist = dexp.get("history", [])
        if(file):
            if file in hist:
                del(hist[hist.index(file)])
            try:
                spss.Popen(["start", "", file], shell=False)
                hist.reverse()
                hist.append(file)
                hist.reverse()
                if(len(hist) > 20):
                    hist.pop()
            except:
                try:
                    os.startfile(file)
                    hist.reverse()
                    hist.append(file)
                    hist.reverse()
                    if(len(hist) > 20):
                        hist.pop()
                except:pass
        dexp["history"] = hist
        mf.writeType(epath, dexp)
        return {"history": [{os.path.dirname(ww): os.path.basename(ww)} for ww in hist]}

    def searchFile(self, dir, name):
        data = {"dir": False, "data": {}, "category": "c"}
        if os.path.exists(dir):
            data["dir"] = dir
            data["category"] = get_folder_category(dir)
            results = search(dir, name)
            for result in results:
                icon = False
                file_path = result
                ww = os.path.basename(result)
                if not os.path.isdir(file_path) and file_path.split(".")[-1].lower() in ["png", "jpg", "jpeg", "bmp", "gif", "tif", "tiff", "webp", "ico"]:
                    filename = secure_filename(os.path.basename(ww)) 
                    save_path = os.path.join(tools.APP.config["UPLOAD_FOLDER"], filename)
                    if not os.path.exists(save_path):
                        shutil.copyfile(file_path, save_path)
                    icon = f"http://127.0.0.1:5555/static/img/{filename}"
                
                stat = os.stat(file_path) if os.path.exists(file_path) else None
                temps = convertDate(stat.st_mtime if stat else 0)
                data["data"][ww] = {"name":ww,
                            "isDir": os.path.isdir(file_path),
                            "date": temps[0],
                            "brutDate": temps[1],
                            "size": convertOct(stat.st_size if stat else 0),
                            "brutSize": stat.st_size if stat else 0,
                            "icon": icon,
                            "path": dir,
                            "type": getKind(file_path.split(".")[-1].lower()) if "." in os.path.basename(file_path) else ""
                            }
        return data
    
    def askNew(self, dir, type_="file"):
        response = {"message": False, "data":{}}
        try:
            new = "new file" if type_ == "file" else "new folder"
            if os.path.exists(f"{dir}/{new}"):
                a = 1
                while os.path.exists(f"{dir}/{new} ({a})"):
                    a += 1
                new += f" ({a})"
            file_path = f"{dir}/{new}"
            if(type_ == "file"):
                with open(file_path, "w", encoding="utf-8") as f:None
            else:os.mkdir(file_path)
            stat = os.stat(file_path) if os.path.exists(file_path) else None
            temps = convertDate(stat.st_mtime if stat else 0)
            response["data"] = {"name":new,
                        "isDir": os.path.isdir(file_path),
                        "date": temps[0],
                        "brutDate": temps[1],
                        "size": convertOct(stat.st_size if stat else 0),
                        "brutSize": stat.st_size if stat else 0,
                        "icon": False,
                        "path": dir,
                        "type": getKind(file_path.split(".")[-1].lower()) if "." in os.path.basename(file_path) else ""
                        }
            response["message"]=True
        except Exception as e:
            print(e)
        return response

    def askRename(self, dir, old, new):
        response = {"statut": False, "why": "NO_EXISTS", "data":{}}
        file_path = dir+"/"+new
        if(old.lower().strip()!=new.lower().strip()):
            if os.path.exists(file_path) :
                a=1
                d=dir
                t="file" if os.path.isfile(file_path) else "folder"
                n=new.split(".") if t=="file" else new
                e=None
                if len(n)>1 and t=="file":
                    e=n[-1]
                    n=".".join(n[:-1])
                else:
                    n="".join(n)
                while os.path.exists(f'{d}/{n} ({a}){f".{e}" if e else ""}'):
                    a+=1
                file_path=f'{d}/{n} ({a}){f".{e}" if e else ""}'
            try:
                os.rename(dir+"/"+old, file_path)
                dir = os.path.dirname(dir)
                stat = os.stat(file_path) if os.path.exists(file_path) else None
                temps = convertDate(stat.st_mtime if stat else 0)
                response["data"] = {"name":os.path.basename(file_path),
                            "isDir": os.path.isdir(file_path),
                            "date": temps[0],
                            "brutDate": temps[1],
                            "size": convertOct(stat.st_size if stat else 0),
                            "brutSize": stat.st_size if stat else 0,
                            "icon": False,
                            "path": dir,
                            "type": getKind(file_path.split(".")[-1].lower()) if "." in os.path.basename(file_path) else ""
                            }
                response["statut"]=True
            except Exception as e:
                print(e)
        return response
    
    def askDelete(self, paths):
        response = {}
        for ww in paths:
            if os.path.exists(ww):
                try:
                    s2t.send2trash(os.path.normpath(ww))
                    response[ww]=os.path.basename(ww)
                except Exception as e:
                    response[ww]=False
                    print(e)
            else:
                response[ww]=None
        return response

    def askCopy(self, paths, dir, action="copy"):
        data={"data":{}}
        for ww in paths:
            try:
                name = os.path.basename(ww)
                file_path = dir+"/"+name
                print(file_path)
                if action=="copy":
                    if(os.path.isdir(ww)):
                        shutil.copytree(ww, file_path)
                    else:
                        shutil.copy2(ww, file_path)
                else:
                    shutil.move(ww, file_path)
                icon = False
                if not os.path.isdir(file_path) and file_path.split(".")[-1].lower() in ["png", "jpg", "jpeg", "bmp", "gif", "tif", "tiff", "webp", "ico"]:
                    filename = secure_filename(os.path.basename(file_path)) 
                    save_path = os.path.join(tools.APP.config["UPLOAD_FOLDER"], filename)
                    if not os.path.exists(save_path):
                        shutil.copyfile(file_path, save_path)
                    icon = f"http://127.0.0.1:5555/static/img/{filename}"
                
                stat = os.stat(file_path) if os.path.exists(file_path) else None
                temps = convertDate(stat.st_mtime if stat else 0)
                data["data"][ww] = {"isOk":True,
                            "name":name,
                            "isDir": os.path.isdir(file_path),
                            "date": temps[0],
                            "brutDate": temps[1],
                            "size": convertOct(stat.st_size if stat else 0),
                            "brutSize": stat.st_size if stat else 0,
                            "icon": icon,
                            "path": dir,
                            "type": getKind(file_path.split(".")[-1].lower()) if "." in os.path.basename(file_path) else ""
                            }
            except Exception as e:
                print(e)
                data[ww] = {
                    "isOk": False,
                    "exception": str(e)
                }
        return data

if __name__ == "__main__":
    script = """$("#fvl-defpath").find(".fvlc-item[cible='c']").click();"""
    mf.clearDirectory("tempcaches")
    mf.clearDirectory("static/img")
    main = MainApp("DExplorer", url="D-Explorer/DExplorer.html", api=API())
    tools.serverRequierement()
    
    UPLOAD_FOLDER = os.path.join(tools.APP.root_path, "static", "img")
    os.makedirs(UPLOAD_FOLDER, exist_ok=True) 
    tools.APP.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
    
    @tools.APP.route('/static/img/<filename>')
    def serve_image(filename):
        return flask.send_from_directory(tools.APP.config["UPLOAD_FOLDER"], filename)
    def st():
        import time
        time.sleep(3)
        main.window.run_js(script)
        
    thread = tools.Thread()
    thread.add(tools.startToolsFlask, join=False)
    thread.add(st, join=False)
    thread.start()
    sys.exit(main.start(gui="edgechromium"))
