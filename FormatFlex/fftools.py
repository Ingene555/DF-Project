import math
import os
import mainFunctions as mf
import tools
from datetime import datetime as dt

import toAUDIO
import toEXCEL
import toIMG
import toPDF
import toPP
import toTXT
import toWORD
import toVIDEO

import time


class Queu:
    def __init__(self, maxsize=math.inf):
        self.queu = []
        self.length = 0
        self.qsize = maxsize
    
    def actualize(self):
        while len(self.queu)>self.qsize:
            self.queu.pop(-1)
    
    def isEmpty(self):
        self.actualize()
        return len(self.queu)==0
    
    def isFull(self):
        self.actualize()
        return len(self.queu)>=self.qsize
    
    def put(self, *items):
        self.actualize()
        for item in items:
            if not self.isFull():
                self.queu.append(item)
                self.length+=1
    
    def get(self):
        self.actualize()
        x=None
        if not self.isEmpty():
            x=self.queu[0]
            self.queu.pop(0)
            self.length-=1
        return x


def getKind(ext):
    if not ext:
        ext=""
    ext = ext.lower().strip()
    if ext in ["png", "jpg", "jpeg", "bmp", "gif", "tif", "tiff", "ico", "webp", "svg"]:
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
    elif ext in [""]:
        kind = "file"
    else:
        kind = "undefined"
    return kind

def getTo(ext):
    l = []
    ext = getKind(ext)
    for ww in LIST:
        if ext in ww["from"]:
            l.append(ww["name"])
    return l

def compare(items):
    l=[]
    to = [getTo(ww) for ww in items]
    ma = max(to, key=len)
    for ww in ma:
        a = True
        for xx in to:
            if not ww in xx:
                a=False
        if a:
            l.append(ww)
    return l

def FFsetFormItem(listOfExt):
    l = []
    a = compare(listOfExt)
    for ww in a:
        output = {"name": "", "ext": []}
        for xx in LIST:
            if ww==xx["name"]:
                output["name"]=xx["name"]
                for yy in xx["ext"]:
                    output["ext"].append({
                        "ext": yy,
                        "method": "one",
                        "name": yy,
                        "title": "ONE input = ONE output"
                    })
                    if xx["multiple"]:
                        output["ext"].append({
                            "ext": yy,
                            "method": "multiple",
                            "name": yy+" in one",
                            "title": "ALL input = ONE output"
                        })
                break
        l.append(output)
    return(l)

def setTC():
    global LIST, DICT
    LIST = [AUDIO, IMAGE, EXCEL, PDF, PWP, TEXT, WORD, VIDEO]
    DICT = {
        "audio": AUDIO,
        "image": IMAGE,
        "excel": EXCEL,
        "pdf": PDF,
        "pwp": PWP,
        "text": TEXT,
        "word": WORD,
        "video": VIDEO
    }

    for ww in LIST:
        os.makedirs(ww["tempcaches"], exist_ok=True)
    toAUDIO.TEMPCACHES = AUDIO["tempcaches"]
    toIMG.TEMPCACHES = IMAGE["tempcaches"]
    toEXCEL.TEMPCACHES = EXCEL["tempcaches"]
    toPDF.TEMPCACHES = PDF["tempcaches"]
    toPP.TEMPCACHES = PWP["tempcaches"]
    toTXT.TEMPCACHES = TEXT["tempcaches"]
    toWORD.TEMPCACHES = WORD["tempcaches"]

def clearAllTC():
    setTC()
    for ww in LIST:
         mf.clearDirectory(ww["tempcaches"])        

def setPS(ps):
    toAUDIO.PROGRESS_SHOW = ps
    toIMG.PROGRESS_SHOW = ps
    toEXCEL.PROGRESS_SHOW = ps
    toPDF.PROGRESS_SHOW = ps
    toPP.PROGRESS_SHOW = ps
    toTXT.PROGRESS_SHOW = ps
    toVIDEO.PROGRESS_SHOW = ps
    toWORD.PROGRESS_SHOW = ps

AUDIO = {
    "name": "audio",
    "from":["audio", "video"],
    "ext": ["aif", "aiff", "aac", "m4a", "mp3", "wav", "flac"],
    "multiple": True,
    "convert":{
        "one": {"video": toAUDIO.VideoToAudio, "audio": toAUDIO.AudioToAudio},
        "multiple": toAUDIO.MixedToAudio
            },
    "ps":{
        "one": {"video": "{},", "audio": "{},"},
        "multiple": ""
    },
    "tempcaches": toAUDIO.TEMPCACHES+"/ff-toaudio/",
    "to": "toAUDIO"
    }
IMAGE = {
    "name": "image",
    "from": ["video", "image", "text", "pdf", "pwp"],
    "ext": ["bmp", "gif", "ico", "jpeg", "jpg", "png", "svg", "tif", "tiff"],
    "multiple": False,
    "convert":{
        "one":{
            "image": toIMG.ImgToImg,
            "video": toIMG.VideoToImg,
            "text": toIMG.TextToImg, 
            "pdf": toIMG.PdfToImg,
            "word": toIMG.WordToImg,
            "pwp": toIMG.PpToImg
            },
        "multiple": None
    },
    "ps":{
        "one":{
            "image": "{},",
            "video": "'png', None, {},",
            "pdf": "'png', None, {},",
            "text": "[997, 1080, 10], ['white', 'black'], ['arial', 20], {},",
            "word": "'png', {},",
            "pwp": "'png', {},"
            },
        "multiple": None
        },
    "tempcaches": toIMG.TEMPCACHES+"/ff-toimg/",
    "to":"toIMG"
}
EXCEL = {
    "name": "excel",
    "from": ["excel"],
    "ext": ["csv", "xls", "xlsb", "xlsm", "xlsx", "xlt", "xltx"],
    "multiple": False,
    "convert":{
        "one":{"excel": toEXCEL.ExcelToExcel},
        "multiple": None
    },
    "ps":{
        "one": {"excel": ""},
        "multiple": None
    },
    "tempcaches": toEXCEL.TEMPCACHES+"/ff-toexcel/",
    "to":"toEXCEL"
}
PDF = {
    "name": "pdf",
    "from": ["text", "image"],
    "ext": ["pdf"],
    "multiple": True,
    "convert":{
        "one":{"text": toPDF.TextToPdf, "image": toPDF.ImgToPdf},
        "multiple": toPDF.MixedToPdf
    },
    "ps":{
        "one":{"text": "", "image": ""},
        "multiple": "'multiple',"
        },
    "tempcaches": toPDF.TEMPCACHES+"/ff-topdf/",
    "to": "toPDF"
}
PWP = {
    "name": "pwp",
    "from": ["pwp"],
    "ext": ["pot", "potx", "ppt", "pptx"],
    "multiple": False,
    "convert": {
        "one":{"pwp": toPP.PpToPp},
        "multiple": None
    },
    "ps":{
        "one":{"pwp": ""},
        "multiple": ""
        },
    "tempcaches": toPP.TEMPCACHES+"/ff-topwp/",
    "to": "toPP"
}
TEXT = {
    "name": "text",
    "from": ["image", "excel", "pdf", "text", "video", "pwp", "word"],
    "ext": ["txt"],
    "multiple": False,
    "convert":{
        "one": {
            "image": toTXT.ImgToTxt,
            "excel": toTXT.ExcelToTxt,
            "pdf": toTXT.PdfToTxt,
            "text": toTXT.TxtToTxt,
            "video": toTXT.VideoToTxt,
            "pwp": toTXT.PpToTxt,
            "word": toTXT.WordToTxt
        },
        "multiple": None
    },
    "ps": {
        "one":{
            "image": "'@%#*+=-:. ', 'multiple', {}, True,",
            "excel": "'multiple',",
            "pdf": "'multiple',",
            "text": "'multiple',",
            "video": "None, '@%#*+=-:. ', {}, 'multiple',",
            "pwp": "'multiple',",
            "word": "'multiple',"
            },
        "multiple": ""
        },
    "tempcaches": toTXT.TEMPCACHES+"/ff-totxt/",
    "to": "toTXT"
}
VIDEO = {
    "name": "video",
    "from": ["video"],
    "ext": ["avi", "flv", "mkv", "mov", "mp4", "wmv"],
    "multiple": False,
    "convert":{
        "one":{"video": toVIDEO.VideoToVideo},
        "multiple": None
    },
    "ps":{
        "one":{"video": ""},
        "multiple":""
        },
    "tempcaches": toVIDEO.TEMPCACHES+"/ff-tovideo/",
    "to": "toVIDEO"
}
WORD = {
    "name": "word",
    "from": ["word", "text", "image", "excel"],
    "ext": ["docx", "doc", "dot", "dotx"],
    "multiple": True,
    "convert":{
        "one": {
            "word": toWORD.WordToWord,
            "text": toWORD.TextToWord,
            "image": toWORD.ImgToWord,
            "excel": toWORD.ExcelToWord
        },
        "multiple": toWORD.MixedToWord
    },
    "ps":{
        "one":{
            "word": "'multiple',",
            "text": "'multiple',",
            "image": "'multiple',",
            "excel": "'multiple',"
            },
        "multiple": "'multiple',"
        },
    "tempcaches": toWORD.TEMPCACHES+"/ff-toword/",
    "to": "toWORD"
}
FILE = {
    "name": "file",
    "from": [],
    "ext": [],
    "multiple": False,
    "convert":{
        "one":None,
        "multiple": None
    },
    "tempcaches": "tempcaches"
}
UNDEFINED = {
    "name": "undefined",
    "from": [],
    "ext": [],
    "multiple": False,
    "convert":{
        "one":None,
        "multiple": None
    },
    "tempcaches": "tempcaches"
}
LIST = [AUDIO, IMAGE, EXCEL, PDF, PWP, TEXT, WORD, VIDEO]
DICT = {
    "audio": AUDIO,
    "image": IMAGE,
    "excel": EXCEL,
    "pdf": PDF,
    "pwp": PWP,
    "text": TEXT,
    "word": WORD,
    "video": VIDEO
}


class ProgressShow:
    def __init__(self, main, id, group, percentShow):
        self.main = main
        self.group = group
        self.id=id if type(id)==list else [id]
        self.pes = percentShow
    def show(self, percent, finished=False, stop=False, output=[]):
        if stop:
            pass
        else:
            for ww in self.id:
                script = f"""
                $("#{self.group}").find(".ffbg-convert").find("div[cible='{ww}']").find(".ff-il-name").attr("percent", "{percent}").text("{percent}%");
                $("#{self.group}").find(".ffbg-convert").find("div[cible='{ww}']").find(".ff-il-fill").css("width", "{percent}%");
                var length = $("#{self.group}").find(".ffbg-convert").find(".ffbgil-item").length;
                """
                self.main(script)
                self.pes.set(ww, percent, finished)


class PercentShow:
    def __init__(self, group, main, aih):
        self.group = group
        self.main = main
        self.length = 0
        self.list = {}
        self.cls = []
        self.hist=[]
        self.write = aih
    def add(self, id):
        id = id if type(id)==list else [id]
        for ww in id:
            self.list[ww] = {"val":0, "end": False}
            self.length+=1
    def set(self, id, value, finished=False):
        self.list[id] = {"val": value, "end": finished}
        percent = 0
        for ww in self.list.keys():
            a = 100/self.length
            b = self.list[ww]["val"]*a/100
            percent +=b
        script = f"""
        $("#{self.group}").find("div[for='percent']").text("{int(percent)}%");
        """
        self.main(script)
        a = True
        for ww in self.list.values():
            if not ww["end"]:
                a = False
                break
        if a:
            self.write(self.hist[0], self.hist[1], self.hist[2])
            script = f"""
            let name = $("#{self.group}").find(".ffbgio-gtitle").text();
            FFshowMessage("Group "+name+" completed");
            $("#{self.group}").find("button[for='cancel']").hide();
            $("#{self.group}").find("button[for='delete']").show();
            $("#{self.group}").find("wataba[for='success']").show();
            $("#{self.group}").find("div[for='percent']").hide();
            """
            self.main(script)
            for ww in range(5):
                time.sleep(1)
                self.main(script)
    def append(self, cls):
        self.cls.append(cls)
    def setHist(self, title, details, output):
        self.hist = [title, details, output]
    def kill(self):
        for ww in self.cls:
            ww.kill()
        script = """
        $(group).attr("converting", "no");
        $(group).find("button[for='convert']").show();
        $(group).find("button[for='cancel']").hide();
        $(group).find("div[for='percent']").hide();
        $(group).find("button[for='delete']").show();
        $(group).find(".ffea-browse").show();
        $(group).find("input[type='text']").prop("disabled", false);
        $(group).find(".ffbgio-element")[0].style.setProperty("display", "block", "important");
        $(group).find(".ffb-additem")[0].style.setProperty("display", "block", "important");
        $(group).find("input[type='checkbox']").show();
        $(group).find(".ff-il-tdtop, .ff-il-tddown").show();
        $(group).find(".ffbgc-list").find(".ffbgil-item").each(function(ind, el){
        el.style.setProperty("display", "none", "important");
        });
        FFactualizeFunction();
        """.replace("group", f'"#{self.group}"')
        self.main(script)


class Convert:
    def __init__(self, convert, main, aih):
        self.name = convert["name"]
        self.cible = convert['cible']
        self.id = convert["id"]
        self.path = os.path.normpath(mf.Return(mf.getName(convert["output"])).getValues(0))
        self.ext = convert["ext"]
        self.method = convert["method"]
        self.input = convert["input"]
        self.thread = tools.Thread()
        self.listThread = list()
        true = len(self.input)==1
        to = DICT.get(getKind(self.ext))
        self.main = main
        self.pes = None
        self.aih = aih
        if self.method=="one":
            for xx, ww in enumerate(self.input):
                d={}
                fr = getKind(ww["ext"])
                d["class"] = to["convert"]["one"][fr](os.path.normpath(ww["name"]))
                if true:
                    aot = f"{self.path}.{self.ext}"
                else:
                    aot = os.path.normpath(f"{self.path} ({xx+1}).{self.ext}")
                d["id"] = ww["id"]
                d["output"] = aot
                d["attr"] = to["to"]
                self.listThread.append(d)
        else:
            l=[]
            d={"id":[]}
            for xx, ww in enumerate(self.input):
                fr = getKind(ww["ext"])
                l.append([fr, ww["name"], None])
                d["id"].append(ww["id"])
            d["output"] = os.path.normpath(f"{self.path}.{self.ext}")
            d["attr"] = to["to"]
            d["class"] = to["convert"]["multiple"](l)
            self.listThread.append(d)
    
    def convert(self):
        self.pes = PercentShow(self.id, self.main, self.aih)
        self.pes.setHist(self.name, [ww["name"] for ww in self.input], self.path+"."+self.ext)
        for ww in self.listThread:
            ww["class"].progressShow = ProgressShow(self.main, ww["id"], self.id, self.pes).show
            self.pes.add(ww["id"])
            self.pes.append(ww["class"])
            exec(f"""self.thread.add(ww["class"].{ww["attr"]}, (ww["output"],), False)""")
        self.thread.start()
    
    def get(self):
        return self.listThread
    
    def ps(self):
        script = """
        $("#%s").find("button[for='cancel']").click(function(){
            pywebview.api.cancelProgress("%s");
        });
        """% (self.id, self.id)
        return [self.id, self.pes, script]
    


