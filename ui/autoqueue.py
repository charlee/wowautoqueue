# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui\autoqueue.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AutoQueueDialog(object):
    def setupUi(self, AutoQueueDialog):
        AutoQueueDialog.setObjectName("AutoQueueDialog")
        AutoQueueDialog.resize(314, 238)
        self.line = QtWidgets.QFrame(AutoQueueDialog)
        self.line.setGeometry(QtCore.QRect(20, 170, 271, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.layoutWidget = QtWidgets.QWidget(AutoQueueDialog)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 190, 271, 32))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.status = QtWidgets.QLabel(self.layoutWidget)
        self.status.setObjectName("status")
        self.verticalLayout.addWidget(self.status)
        self.groupBox = QtWidgets.QGroupBox(AutoQueueDialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 281, 91))
        self.groupBox.setObjectName("groupBox")
        self.widget = QtWidgets.QWidget(self.groupBox)
        self.widget.setGeometry(QtCore.QRect(10, 20, 257, 58))
        self.widget.setObjectName("widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.start_time = QtWidgets.QTimeEdit(self.widget)
        self.start_time.setObjectName("start_time")
        self.horizontalLayout.addWidget(self.start_time)
        self.startTimerButton = QtWidgets.QPushButton(self.widget)
        self.startTimerButton.setObjectName("startTimerButton")
        self.horizontalLayout.addWidget(self.startTimerButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.startNowButton = QtWidgets.QPushButton(self.widget)
        self.startNowButton.setObjectName("startNowButton")
        self.horizontalLayout_2.addWidget(self.startNowButton)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.groupBox_2 = QtWidgets.QGroupBox(AutoQueueDialog)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 110, 281, 51))
        self.groupBox_2.setObjectName("groupBox_2")
        self.startAntiIdle = QtWidgets.QPushButton(self.groupBox_2)
        self.startAntiIdle.setGeometry(QtCore.QRect(10, 20, 123, 23))
        self.startAntiIdle.setObjectName("startAntiIdle")

        self.retranslateUi(AutoQueueDialog)
        QtCore.QMetaObject.connectSlotsByName(AutoQueueDialog)

    def retranslateUi(self, AutoQueueDialog):
        _translate = QtCore.QCoreApplication.translate
        AutoQueueDialog.setWindowTitle(_translate("AutoQueueDialog", "《魔兽世界经典怀旧服》自动排队工具"))
        self.label_2.setText(_translate("AutoQueueDialog", "当前状态"))
        self.status.setText(_translate("AutoQueueDialog", "待机"))
        self.groupBox.setTitle(_translate("AutoQueueDialog", "自动排队"))
        self.label.setText(_translate("AutoQueueDialog", "选择启动游戏的时间"))
        self.start_time.setDisplayFormat(_translate("AutoQueueDialog", "hh:mm"))
        self.startTimerButton.setText(_translate("AutoQueueDialog", "定时排队"))
        self.label_3.setText(_translate("AutoQueueDialog", "或者不使用定时器"))
        self.startNowButton.setText(_translate("AutoQueueDialog", "立即排队"))
        self.groupBox_2.setTitle(_translate("AutoQueueDialog", "防掉线"))
        self.startAntiIdle.setText(_translate("AutoQueueDialog", "启动防掉线"))
