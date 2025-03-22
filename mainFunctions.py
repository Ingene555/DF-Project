""" 
This library will contain the main functions that will be used in all extensions and in the main application
"""

import ctypes
import sys
import os
import pickle as pkl
import shutil
from PIL import ImageColor


class Return:
    """This class return bool, values and type of result, to manage some errors"""

    def __init__(self, value=None):
        self.succed = value['bool'] if value else False
        self.values = value['values'] if value else []
        self.types = value['types'] if value else []

    def set(self, value):
        self.succed = value['bool']
        self.values = value['values']
        self.types = value['types']

    def getSucced(self):
        return self.succed

    def getValues(self, index='*'):
        return self.values if index == '*' else self.values[index]

    def getTypes(self, index='*'):
        return self.types if index == '*' else self.types[index]


def setReturn(bool_, types, values):
    "This function return a structured result"
    try:
        for ww in types:
            types[types.index(ww)] = ww.__name__
        return {
            "bool":bool_,
            "types":types,
            "values":values
        }
    except Exception as e:
        return {
            "bool":False,
            "types": [type(e).__name__],
            "values": [e]
        }

        
def execFunc(function):
    "This function will try to execute \"function\" and will check if there is an error"
    try:
        return function()
    except Exception as e:
        return setReturn(False, [type(e)], [e])


def is_admin(): 
    "This function will check if the program has admin permission"
    try:
        permission = ctypes.windll.shell32.IsUserAnAdmin()  # Check if the program has admin permission
        return setReturn(True if permission else False, [type(permission)], [permission])
    except Exception as e:
        return setReturn(False, [type(e)], [e])


def run_as_admin():
    "This function will run the program as admin"
    try:
        script = sys.argv[0]
        params = ' '.join(sys.argv[1:])
        # Run as admine >>>
        permission = ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, f"{script} {params}", None, 1) if not Return(is_admin()).getValues()[0] else True
        return setReturn(True if permission else False, [type(permission)], [permission])
    except Exception as e:
        return setReturn(False, [type(e)], [e])


def getExtension(name):
    "return extension of name "
    try:
        ext = name.rsplit('.')[len(name.rsplit('.')[:]) - 1].lower()
        return setReturn(True if ext else False, [type(ext)], [ext])
    except Exception as e:
        return setReturn(False, [type(e)], [e])


def getName(name):
    "return name without extension "
    try:
        name = '.'.join(name.rsplit('.')[:len(name.rsplit('.')[:]) - 1])
        return setReturn(True if name else False, [type(name)], [name])
    except Exception as e:
        return setReturn(False, [type(e)], [e])


def writeType(path, data):
    "This function will save variables as file"
    try:
        with open(path, 'wb') as f:
            pkl.dump(data, f)
            return setReturn(True, [type(path)], [path])
    except Exception as e:
        return setReturn(False, [type(e)], [e])


def readType(path):
    "This function will read file and get the variable"
    try:
        with open(path, 'rb') as f:
            data = pkl.load(f)
            return setReturn(True, [type(data)], data)
    except Exception as e:
        return setReturn(False, [type(e)], [e])


def clearDirectory(directory):
    "This function clear directory"
    try:
        if not os.path.exists(directory):
            return  setReturn(False, [type('directory not found')], ['directory not found'])
        if os.path.exists(directory):
            try:
                _ = list()
                for filename in os.listdir(directory):
                    file_path = os.path.join(directory, filename)
                    try:
                        if os.path.isfile(file_path) or os.path.islink(file_path):
                            os.remove(file_path)
                        elif os.path.isdir(file_path):
                            shutil.rmtree(file_path)
                        _.append(setReturn(True, [type(file_path)], [file_path]))
                    except Exception as e:
                        _.append(setReturn(False, [type(file_path)], [file_path]))
                return setReturn(True, [type(_)], [_])
            except Exception as e:
                return setReturn(False, [type(e)], [e])
    except Exception as e:
        return setReturn(False, [type(e)], [e])


def getColor(color):
    """
    Convertit une couleur donnée en format (r, g, b, a).
    
    :param color: Nom de la couleur ("red", "blue", etc.) ou couleur hexadécimale ("#RRGGBBAA" ou "#RRGGBB").
    :return: Tuple (r, g, b, a) où r, g, b, a sont des entiers entre 0 et 255.
    """
    try:
        # Utilise PIL pour convertir la couleur en (r, g, b)
        rgba = ImageColor.getcolor(color, "RGBA")
        return rgba
    except:
        return (0, 0, 0, 0)





