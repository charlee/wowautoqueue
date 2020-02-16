import time
import pyautogui as gui
from . import AppCtrl
from utils.screenshot import regionMatchesColor


class WowClassicApp(AppCtrl):
    title = "魔兽世界"

    def isCharacterSelect(self):
        """Test if in Character Select screen.
        """
        rect = self.getRect()
        return regionMatchesColor((rect[0] + 857, rect[1] + 983, 22, 19), (117, 0, 0), 16)

    def enterGame(self):
        self.activate()
        rect = self.getRect()
        gui.moveTo(rect[0] + 860, rect[1] + 990, 1)
        gui.click()

    def antiIdle(self):
        self.activate()
        gui.keyDown('w')
        time.sleep(0.05)
        gui.keyUp('w')
        gui.keyDown('s')
        time.sleep(0.05)
        gui.keyUp('s')
