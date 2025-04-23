""" 
This library will be used for conversion into powerpoint
A class per file type will be defined
"""
#no ODP PPS 

import mainFunctions as mf
import os
import win32com.client as client32
import subprocess as spss
import time

TEMPCACHES = "tempcaches"

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


class PpToPp:

    def __init__(self, file):
        self.file = file if type(file) == list else [file]
        self.stop = False
        self.progressShow = None

    def toPP(self, path):
        path = path if type(path) == list else [path]
        _ = list()
        for xx, ww in enumerate(self.file):
            if not self.stop:
                if self.progressShow:
                    self.progressShow(xx*100/len(self.file))
                try:
                    a = ptp(ww, path[xx])
                    _.append(mf.setReturn(True, [type(a[1])], [a[1]]))
                except Exception as e:
                    _.append(mf.setReturn(False, [type(e)], [e]))
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
