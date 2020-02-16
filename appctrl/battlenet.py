import time
import pyautogui as gui
import win32gui

from . import AppCtrl

class BattleNetApp(AppCtrl):
    classname = 'Qt5QWindowOwnDCIcon'

    def start_game(self):
        hWnd = self.getWindow()
        rect = self.getRect()

        click_pos = (rect[0] + 320, rect[3] - 60)

        self.activate()
        gui.moveTo(*click_pos, 1)
        gui.click()
        gui.moveTo(100, 100)

