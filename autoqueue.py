import sys
import time
from datetime import datetime, timedelta
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import QThread, pyqtSignal, Qt
from ui.autoqueue import Ui_AutoQueueDialog
from appctrl.battlenet import BattleNetApp
from appctrl.wow import WowClassicApp



class AutoQueueDialog(QDialog):

    def __init__(self):
        super().__init__(None, Qt.WindowStaysOnTopHint)

        self.ui = Ui_AutoQueueDialog()
        self.ui.setupUi(self)

        self.ui.startTimerButton.clicked.connect(self.start_timer)
        self.ui.startNowButton.clicked.connect(self.start_now)
        self.ui.startAntiIdle.clicked.connect(self.start_anti_idle)

    def update_status(self, msg):
        self.ui.status.setText(msg)

    def disable_buttons(self):
        self.ui.start_time.setEnabled(False)
        self.ui.startNowButton.setEnabled(False)
        self.ui.startTimerButton.setEnabled(False)
        self.ui.startAntiIdle.setEnabled(False)

    def start_timer(self):
        # Disable button
        self.disable_buttons()

        # Calculate countdown secs
        start_time = datetime.combine(
            datetime.today(),
            self.ui.start_time.time().toPyTime()
        )
        now = datetime.now()

        if start_time < now:
            start_time = start_time + timedelta(days=1)

        secs = (start_time - now).seconds

        self.thread = AutoQueueThread(secs)
        self.thread.signal.connect(self.update_status)
        self.thread.start()

    def start_now(self):
        self.disable_buttons()
        self.thread = AutoQueueThread(0)
        self.thread.signal.connect(self.update_status)
        self.thread.start()

    def start_anti_idle(self):
        self.disable_buttons()
        self.thread = AntiIdleThread()
        self.thread.signal.connect(self.update_status)
        self.thread.start()


class AntiIdleThread(QThread):

    signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()

    def update_status(self, msg):
        self.signal.emit(msg)


    def anti_idle(self):
        wow = WowClassicApp()

        # Anti idle
        anti_idle_interval = 60
        anti_idle_timer = anti_idle_interval
        while True:
            self.update_status('防掉线已启动，%s 秒后移动角色...' % anti_idle_timer)
            time.sleep(1)
            anti_idle_timer -= 1
            if anti_idle_timer == 0:
                wow.antiIdle()
                anti_idle_timer = anti_idle_interval


    def run(self):
        self.anti_idle()


class AutoQueueThread(AntiIdleThread):

    signal = pyqtSignal(str)

    def __init__(self, countdown):
        super().__init__()
        self.countdown = countdown

    def update_status(self, msg):
        self.signal.emit(msg)

    def run(self):
        # Show label
        while self.countdown > 0:
            self.update_status('开始倒计时，%s 秒后启动游戏' % self.countdown)
            time.sleep(1)
            self.countdown -= 1

        self.update_status('正在启动游戏，30秒后检测排队...')

        battlenet = BattleNetApp()
        battlenet.start_game()

        time.sleep(30)

        wow = WowClassicApp()

        # Start queuing...
        queued_secs = 0
        while not wow.isCharacterSelect():
            self.update_status('正在排队，已排队 %s 秒...' % queued_secs)
            time.sleep(1)
            queued_secs += 1

        enter_game_timer = 30
        while enter_game_timer > 0:
            self.update_status('已进入角色选择画面，%s 秒后进入游戏...' % enter_game_timer)
            time.sleep(1)
            enter_game_timer -= 1
        
        self.update_status('正在进入游戏，10秒后启动防掉线...')
        wow.enterGame()

        time.sleep(10)

        self.anti_idle()



def create_main_window():
    app = QApplication(sys.argv)
    window = AutoQueueDialog()
    window.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    create_main_window()