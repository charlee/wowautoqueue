import win32gui

class AppCtrl(object):

    classname = None
    title = None

    def __init__(self):
        self.hWnd = self.getWindow()

    def getWindow(self):
        assert(self.classname is not None or self.title is not None)
        return win32gui.FindWindow(self.classname, self.title)

    def getRect(self):
        return win32gui.GetWindowRect(self.hWnd)

    def activate(self):
        win32gui.SetForegroundWindow(self.hWnd)
