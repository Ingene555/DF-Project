""" 
This library will be used for conversion into pdf
A class per file type will be defined
"""

from datetime import datetime as dt
import os
import mainFunctions as mf
import PyPDF2 as ppdf2
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from docx2pdf import convert as cwp
from toIMG import ModifyToImg
import win32com.client as client32
import subprocess as spss
import time

TEMPCACHES = "tempcaches"
MULTIPLE = "multiple"
ONE = "one"
LINK = "link"
IMG = "img"
TEXT = "text"
PDF = "pdf"


def pls():
    powershell_command = """
    $PowerPoint = New-Object -ComObject PowerPoint.Application
    $PowerPoint.Visible = -1  # msoTrue
    Write-Host "PowerPoint lancé avec succès."
    """
    try:
        result = spss.run(
            ["powershell", "-Command", powershell_command],
            capture_output=True, text=True, shell=True
        )
        return [True, result]
    except Exception as e:
        return [False, e]

        
def wtw(input_file, output_file):
    word = client32.Dispatch("Word.Application")
    word.Visible = False
    doc = word.Documents.Open(os.path.abspath(input_file))
    doc.SaveAs(os.path.abspath(output_file), FileFormat=16)
    doc.Close()
    word.Quit()
    time.sleep(.1)
    
    return output_file


def ptp(input_file, output_file):
    r = pls()
    if r[0]:
        powerpoint = client32.Dispatch("PowerPoint.Application")
        presentation = powerpoint.Presentations.Open(os.path.abspath(input_file))
        presentation.SaveAs(os.path.abspath(output_file), 24)
        presentation.Close()
        time.sleep(.1)
        return [True, output_file]
    else:return r


class PdfToPdf:

    def __init__(self, file):
        self.file = file if type(file) == list else [file]
        self.stop = False
        self.progressShow = None

    def toPDF(self, path, method=MULTIPLE):
        path = path if type(path) == list else [path]
        _ = list()
        if self.progressShow:
            self.progressShow(0)
        if method == MULTIPLE:
            for xx, ww in enumerate(self.file):
                if not self.stop:
                    try:
                        with open(ww, 'rb') as in_file:
                            pdf_reader = ppdf2.PdfReader(in_file)
                            pdf_writer = ppdf2.PdfWriter()
                            for page_num in range(len(pdf_reader.pages)):
                                page = pdf_reader.pages[page_num]
                                pdf_writer.add_page(page)
                                if self.progressShow:
                                    self.progressShow(int(page_num * 100 / len(pdf_reader.pages)))
                            with open(path[xx], 'wb') as out_file:
                                pdf_writer.write(out_file)
                            _.append(mf.setReturn(True, [type(path[xx])], path[xx]))
                    except Exception as e:
                        _.append(mf.setReturn(False, [type(e)], [e]))
                else:
                    for i in _:
                        try:
                            os.remove(mf.Return(i).getValues(0))
                        except:pass
                    _=[]
                    break
        elif method == ONE:
            pdf_writer = ppdf2.PdfWriter()
            for xx, ww in enumerate(self.file):
                if not self.top:
                    try:
                        with open(ww, 'rb') as in_file:
                            pdf_reader = ppdf2.PdfReader(in_file)
                            for page_num in range(len(pdf_reader.pages)):
                                page = pdf_reader.pages[page_num]
                                pdf_writer.add_page(page)
                                if self.progressShow:
                                    self.progressShow(int(page_num * 100 / len(pdf_reader.pages)))
                    except Exception as e:
                        print(e)
                else:
                    break
            for ww in path:
                if not self.stop:
                    try:
                        with open(ww, 'wb') as out_file:
                            pdf_writer.write(out_file)
                        _.append(mf.setReturn(True, [type(ww)], [ww]))
                    except Exception as e:
                        _.append(mf.setReturn(False, [type(e)], [e]))
                else:
                    for i in _:
                        try:
                            os.remove(mf.Return(i).getValues(0))
                        except:pass
                    _=[]
                    break
        else:
            _.append(mf.setReturn(False, [type(None)], [None]))
        if self.progressShow:
            self.progressShow(100, True, self.stop, _)
        return _

    def kill(self):
        self.stop = True
   

class MixedToPdf:

    def __init__(self, *file):
        self.file = [*file]
        n = False
        for ww in self.file:
            if type(ww) != list:
                n = True
                break
        if n:self.file = [self.file]
        self.stop = False
        self.toKill = None
        self.progressShow = None

    def Convert(self, pathF, pathT):
        pathT
        _ = list()
        for ww in range(len(pathF)):
            type(ww)
            _.append(os.path.join(TEMPCACHES, f"tc-mdf-{ww}-{dt.now()}.pdf".replace(":", "")))
        while(len(pathF) > len(_)):
            _.append(os.path.join(TEMPCACHES, f"tc-mdf-{dt.now()}.pdf".replace(":", "")))
        __ = list()
        for xx, ww in enumerate(pathF):
            if not self.stop:
                try:
                    c = canvas.Canvas(_[xx], pagesize=letter)
                    c.setFont("Helvetica", 12)
                    y = 750
                    for yy, item in enumerate(ww):
                        if not self.stop:
                            try:
                                if len(item) < 3:
                                    item.append(None)
                                item_type, content, none = item
                                if item_type == "text":
                                    with open(content, "r", encoding="utf-8") as f:
                                        content = f.read()
                                    item_type = "string"
                                if item_type == "string":

                                    def draw_paragraph(text, y_position):
                                        styles = getSampleStyleSheet()
                                        paragraph = Paragraph(text.replace("\n", "<br />"), style=styles['Normal'])
                                        paragraph_width = 500
                                        paragraph_height = paragraph.wrap(paragraph_width, 1000000)[1]
                                        paragraph.drawOn(c, 50, y_position - paragraph_height)
                                        return paragraph_height

                                    if y < 50:
                                        c.showPage()
                                        c.setFont("Helvetica", 12)
                                        y = 750
                                    paragraph_height = draw_paragraph(content, y)
                                    y -= paragraph_height + 10
                                elif item_type == "image":
                                    try:
                                        tm = f"{TEMPCACHES}/tc-{dt.now()}.png".replace(":", "")
                                        self.toKill = ModifyToImg(content)
                                        im = mf.Return(self.toKill.toIMG(tm, none if none else {})[0]).getValues(0)
                                        c.drawImage(im, 50, y - 200, width=300, height=200)
                                        y -= 220
                                        try:os.remove(im)
                                        except Exception as e:print(e)
                                    except Exception as e:
                                        print(e)
                                if y < 50:
                                    c.showPage()
                                    y = 750
                            except Exception as e:
                                print(e)
                            if self.progressShow:
                                self.progressShow(int(yy * 100 / len(ww)))
                        else:
                            break
                    c.save()
                    __.append(mf.setReturn(True, [type(_[xx])], [_[xx]]))
                except Exception as e:
                    __.append(mf.setReturn(False, [type(e)], [e]))
            else:
                for i in __:
                    try:
                        os.remove(mf.Return(i).getValues(0))
                    except:pass
                break
        return __

    def toPDF(self, path, method=MULTIPLE):
        temp = self.Convert(self.file, [])
        self.toKill = PdfToPdf([mf.Return(ww).getValues(0) for ww in temp])
        _ = self.toKill.toPDF(path, method)
        for ww in temp:
            if not self.stop:
                if mf.Return(ww).getSucced():
                    try:os.remove(mf.Return(ww).getValues(0))
                    except Exception as e:print(e)
            else: 
                for i in _:
                    try:
                        os.remove(mf.Return(i).getValues(0))
                    except:pass
                _=[]
                break
        if self.progressShow:
            self.progressShow(100, True, self.stop, _)
        return _

    def kill(self):
        self.stop = True
        if self.toKill:
            try:
                self.toKill.kill()
            except Exception as e:
                print(e)


class ImgToPdf:
    def __init__(self, file):
        self.file = file if type(file) == list else [file]
        self.stop = False
        self.toKill = None
        self.progressShow = None
    
    def toPDF(self, path):
        _ = list()
        for ww in self.file:
            if not self.stop:
                self.toKill = MixedToPdf([["image",  ww, None]])
                self.toKill.progressShow = self.progressShow
                _.append(self.toKill.toPDF(path))
            else:
                for i in _:
                    try:
                        os.remove(mf.Return(i).getValues(0))
                    except:pass
                _=[]
                break
        if self.progressShow:
            self.progressShow(100, True, self.stop, _)
        return _
    
    def kill(self):
        self.stop = True
        if self.toKill:
            try:
                self.toKill.kill()
            except Exception as e:
                print(e)


class TextToPdf:
    def __init__(self, file):
        self.file = file if type(file) == list else [file]
        self.stop = False
        self.toKill = None
        self.progressShow = None
    
    def toPDF(self, path):
        _ = list()
        for ww in self.file:
            if not self.stop:
                self.toKill = MixedToPdf([["text",  ww, None]])
                self.toKill.progressShow = self.progressShow
                _.append(self.toKill.toPDF(path))
            else:
                for i in _:
                    try:
                        os.remove(mf.Return(i).getValues(0))
                    except:pass
                _=[]
                break
        if self.progressShow:
            self.progressShow(100, True, self.stop, _)
        return _
    
    def kill(self):
        self.stop = True
        if self.toKill:
            try:
                self.toKill.kill()
            except Exception as e:
                print(e)


    
