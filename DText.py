import os
import sys
import webview
import flask
import tools



class MainApp(tools.Window):

    def __init__(self, title, url=None, html=None, api=None, text=None):
        global APP
        tools.Window.__init__(self, title, url, html, api)
        self.window.min_size = (700, 500)
        self.window.confirm_close = True


class API:
    def __init__(self):
        self.DT={}

    def openFile(self):
        fileTypes = ("Text Files (*.txt)", "All Files (*.*)")
        result = main.window.create_file_dialog(webview.OPEN_DIALOG, "Documents", file_types=fileTypes, allow_multiple=True)
        if result:
            text = {}
            for ww, xx in enumerate(result):
                try:
                    with open(xx, "r", encoding="utf-8") as f:
                        text[result[ww].replace("\\", "/")] = f.read()
                except Exception as e:
                    text[result[ww]] = None
            return text
        else:
            return {}

    def saveFile(self, dir, content):
        self.DT["past"] = dir
        if not os.path.exists(dir):
            dir = main.window.create_file_dialog(webview.SAVE_DIALOG, "Documents", False, os.path.basename(dir),
                                           ("Text Files (*.txt)", "All Files (*.*)"))
        if dir:
            with open(dir, "w", encoding="utf-8") as f:
                f.write(content)
            self.DT["message"]=True
            self.DT["new"]=dir.replace("\\", "/")
            self.DT["content"]=content
        else:
            self.DT["message"]=False
        return self.DT
    
    def getFile(self):
        return self.DT

    def close(self):
        main.window.run_js("closeAll();")
        main.window.destroy()
        flask.request.environ.get('werkzeug.server.shutdown')


if __name__ == "__main__":
    api = API()
    main = MainApp("DText", url="D-Text/DText.html", api=api)
    tools.serverRequierement()
    thread = tools.Thread()
    thread.add(tools.startToolsFlask, join=False)
    thread.start()
    main.window.events.closed += api.close
    sys.exit(main.start())
