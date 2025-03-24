""" 
This library will be used for conversion into image
A class per file type will be defined
"""

from PIL import Image
import mainFunctions as mf
from datetime import datetime as dt
import os
from wand.image import Image as WandImage
import win32api
import qrcode

TEMPCACHES = 'tempcaches'
mf.clearDirectory("tempcaches")
ALL = "all"


class ImgToImg:

    def __init__(self, file):
        self.file = file if type(file) == list else [file]
        self.ext = [mf.Return(mf.getExtension(ww)).getValues(0).lower() for ww in self.file]
    
    def toIMG(self, path, param={None:None}, progressShow=print, detailed=True):
        param = param if type(param) == dict else {None:None}
        _ = list()
        type(detailed)
        for xx in range(len(self.file)):
            progressShow(int(xx * 100 / len(path)), 0)
            try:
                param = param if type(param) == dict else {None:param}
                path = path if type(path) == list else [path]
                clss = [mf.Return(mf.getExtension(path[ww])) for ww in range(len(path))]
                ext = [clss[ww].getValues(0).lower() if clss[ww].getValues(0) in "cur,bmp,gif,jpeg,jpg,ico,png,svg,tiff,tif,webp".rsplit(",") else "png" for ww in range(len(clss))]
                clss = [mf.Return(mf.getName(path[ww])) for ww in range(len(path))]
                name = [clss[ww].getValues(0) for ww in range(len(clss))]
                output = f"{TEMPCACHES}/tc-{dt.now()}.png".replace(":", "") if xx >= len(ext) else ".".join([name[xx], ext[xx]])
                exec(f"""a=self.to{'PNG' if xx>=len(ext) else ext[xx].upper()}('{self.file[xx]}', '{output}', param)
_.append(mf.setReturn(True, [type(a)], [a]))""")
                if not _[-1]: del(_[-1])
            except Exception as e:
                _.append(mf.setReturn(False, [type(e)], [e]))
            progressShow(int(xx * 100 / len(path)), 100)
        progressShow(100, 100)
        return _
    
    def toPNG(self, pathF, pathT, param={None:None}):
        param = param if type(param) == dict else {None:None}
        if mf.Return(mf.getExtension(pathF)).getValues(0) == 'svg':
            with WandImage(filename=pathF) as img:
                img.format = 'png'
                img.save(filename=mf.Return(mf.getName(pathT)).getValues(0) + ".png", format="PNG")
        else:
            with Image.open(pathF) as img:
                output_file = mf.Return(mf.getName(pathT)).getValues(0) + ".png"
                try: img.convert("RGBA")
                except: pass
                img.save(output_file, format="PNG")
        return pathT
    
    def toCUR(self, pathF, pathT, param={None:None}):
        param = param if type(param) == dict else {None:None}
        a = self.toICO(pathF, f"{TEMPCACHES}\\any-png-curany-{dt.now()}.png".replace(':', '.'))
        output_file = mf.Return(mf.getName(pathT)).getValues(0) + ".cur"
        win32api.CopyFile(a, output_file, True)
        os.remove(a)
        return output_file
    
    def toBMP(self, pathF, pathT, param={None:None}):
        param = param if type(param) == dict else {None:None}
        a = self.toPNG(pathF, f"{TEMPCACHES}\\any-png-bmpany-{dt.now()}.png".replace(':', '.'))
        output_file = mf.Return(mf.getName(pathT)).getValues(0) + ".bmp"
        with Image.open(a) as img:
            img.save(output_file, format="BMP")
        os.remove(a)
        return output_file
    
    def toGIF(self, pathF, pathT, param={None:None}):
        param = param if type(param) == dict else {None:None}
        a = self.toPNG(pathF, f"{TEMPCACHES}\\any-png-gifany-{dt.now()}.png".replace(':', '.'))
        output_file = mf.Return(mf.getName(pathT)).getValues(0) + ".gif"
        with Image.open(a) as img:
            img.save(output_file, format="GIF")
        os.remove(a)
        return output_file
    
    def toICO(self, pathF, pathT, param={None:None}):
        param = param if type(param) == dict else {None:None}
        a = self.toPNG(pathF, f"{TEMPCACHES}\\any-png-icoany-{dt.now()}.png".replace(':', '.'))
        output_file = mf.Return(mf.getName(pathT)).getValues(0) + ".ico"
        with Image.open(a) as img:
            img.save(output_file, format="ICO")
        os.remove(a)
        return output_file
    
    def toJPEG(self, pathF, pathT, param={None:None}):
        param = param if type(param) == dict else {None:None}
        a = self.toPNG(pathF, f"{TEMPCACHES}\\any-png-jpegany-{dt.now()}.png".replace(':', '.'))
        output_file = mf.Return(mf.getName(pathT)).getValues(0) + ".jpeg"
        with Image.open(a) as img:
            img.save(output_file, format="JPEG")
        os.remove(a)
        return output_file
    
    def toJPG(self, pathF, pathT, param={None:None}):
        param = param if type(param) == dict else {None:None}
        a = self.toPNG(pathF, f"{TEMPCACHES}\\any-png-jpgany-{dt.now()}.png".replace(':', '.'))
        output_file = mf.Return(mf.getName(pathT)).getValues(0) + ".jpg"
        with Image.open(a) as img:
            img.save(output_file, format="JPEG")
        os.remove(a)
        return output_file
    
    def toSVG(self, pathF, pathT, param={None:None}):
        param = param if type(param) == dict else {None:None}
        a = self.toPNG(pathF, f"{TEMPCACHES}\\any-png-svgany-{dt.now()}.png".replace(':', '.'))
        output_file = mf.Return(mf.getName(pathT)).getValues(0) + ".svg"
        with WandImage(filename=a, resolution=param.get("resolution", 1080)) as img:
            img.format = 'svg'
            img.save(filename=output_file)
        os.remove(a)
        return output_file
    
    def toTIFF(self, pathF, pathT, param={None:None}):
        param = param if type(param) == dict else {None:None}
        a = self.toPNG(pathF, f"{TEMPCACHES}\\any-png-tiffany-{dt.now()}.png".replace(':', '.'))
        output_file = mf.Return(mf.getName(pathT)).getValues(0) + ".tiff"
        with Image.open(a) as img:
            img.save(output_file, format="TIFF")
        os.remove(a)
        return output_file

    def toTIF(self, pathF, pathT, param={None:None}):
        param = param if type(param) == dict else {None:None}
        a = self.toPNG(pathF, f"{TEMPCACHES}\\any-png-tifany-{dt.now()}.png".replace(':', '.'))
        output_file = mf.Return(mf.getName(pathT)).getValues(0) + ".tif"
        with Image.open(a) as img:
            img.save(output_file, format="TIFF")
        os.remove(a)
        return output_file
    
    def toWEBP(self, pathF, pathT, param={None:None}):
        param = param if type(param) == dict else {None:None}
        a = self.toPNG(pathF, f"{TEMPCACHES}\\any-png-webpany-{dt.now()}.png".replace(':', '.'))
        output_file = mf.Return(mf.getName(pathT)).getValues(0) + ".webp"
        with Image.open(a) as img:
            img.save(output_file, format="WEBP")
        os.remove(a)
        return output_file


class LinkToImg:

    def __init__(self, link):
        file = link
        self.file = file if type(file) == list else [file]
    
    def Convert(self, pathF, pathT, qr={}, progressShow=print, detailed=True):
        pathT
        qr = {"pixel":qr.get("pixel", 10),
            "margin":qr.get("margin", 30),
            "bg":qr.get("bg", "white"),
            "fg":qr.get("fg", "black"),
            "version":qr.get("version", 1),
            "correction":qr.get("correction", "L"),
            "width":qr.get("width", 300),
            "height":qr.get("height", 300),
            "image":qr.get("image", None),
            "impact":qr.get("impact", .2),
            "reduction":qr.get("reduction", .5)}
        _ = list()
        for ww in range(len(pathF)):
            _.append(os.path.join(TEMPCACHES, f"tc-linkc-{ww}-{dt.now()}.png".replace(":", "")))
        while(len(pathF) > len(_)):
            _.append(os.path.join(TEMPCACHES, f"tc-linkc-{dt.now()}.png".replace(":", "")))
        __ = list()
        x, y = 0, 0
        progressShow(x, y)
        for xx, ww in enumerate(pathF):
            y = 0
            progressShow(x, y)
            try:
                correction_levels = {'L': qrcode.constants.ERROR_CORRECT_L,
                                    'M': qrcode.constants.ERROR_CORRECT_M,
                                    'Q': qrcode.constants.ERROR_CORRECT_Q,
                                    'H': qrcode.constants.ERROR_CORRECT_H}
                qrc = qrcode.QRCode(
                    version=qr["version"],
                    error_correction=correction_levels.get(qr["correction"], qrcode.constants.ERROR_CORRECT_L),
                    box_size=qr["pixel"],
                    border=qr["margin"] // qr["pixel"],
                )
                qrc.add_data(ww)
                qrc.make(fit=True)
                img = qrc.make_image(fill=qr["fg"], back_color=qr["bg"])
                img = img.resize((qr["width"], qr["height"]))
                if qr["image"]:
                    logo = Image.open(os.path.abspath(qr["image"]))
                    if logo.mode != 'RGBA':
                        logo = logo.convert('RGBA')
                    logo_size = int(min(img.size) * qr["impact"])
                    logo = logo.resize((logo_size, logo_size))
                    logo_pos = ((img.width - logo.width) // 2, (img.height - logo.height) // 2)
                    img.paste(logo, logo_pos, logo)
                if qr["reduction"] != 1:
                    img = img.resize((int(img.width * qr["reduction"]), int(img.height * qr["reduction"])))
                img.save(_[xx])
                detailed
                __.append(mf.setReturn(True, [type(_[xx])], [_[xx]]))
            except Exception as e:
                __.append(mf.setReturn(True, [type(e)], [e]))
            x = int(xx * 100 / len(pathF))
            y = 100
            progressShow(x, y)
        progressShow(100, 100)
        return __

    def toIMG(self, path, qr={}, progressShow=print, detailed=True):
        temp = self.Convert(self.file, [], qr, progressShow, detailed)
        path = path if type(path) == list else [path]
        _ = list()
        for ww in range(len(temp)):
            if mf.Return(temp[ww]).getSucced():
                inp = fr'{mf.Return(temp[ww]).getValues(0)}'.replace("\\", "/")
                outp = fr'{path[ww]}'.replace("\\", "/")
                _.append(ImgToImg(inp).toIMG(outp, {None:None}, progressShow, detailed)[0])
                try:
                    os.remove(mf.Return(temp[ww]).getValues(0))
                except Exception as e:
                    print(e)
            else:
                print(mf.Return(temp[ww]).getValues())
        return _



