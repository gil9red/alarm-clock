# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Tue Aug 25 19:08:53 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(234, 178)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.at_time_rb = QtGui.QRadioButton(self.centralwidget)
        self.at_time_rb.setChecked(True)
        self.at_time_rb.setObjectName("at_time_rb")
        self.gridLayout.addWidget(self.at_time_rb, 0, 0, 1, 1)
        self.at_time = QtGui.QTimeEdit(self.centralwidget)
        self.at_time.setTime(QtCore.QTime(7, 0, 0))
        self.at_time.setObjectName("at_time")
        self.gridLayout.addWidget(self.at_time, 0, 1, 1, 1)
        self.through_time_rb = QtGui.QRadioButton(self.centralwidget)
        self.through_time_rb.setObjectName("through_time_rb")
        self.gridLayout.addWidget(self.through_time_rb, 1, 0, 1, 1)
        self.through_time = QtGui.QTimeEdit(self.centralwidget)
        self.through_time.setTime(QtCore.QTime(0, 45, 0))
        self.through_time.setObjectName("through_time")
        self.gridLayout.addWidget(self.through_time, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.time_remaining = QtGui.QLabel(self.centralwidget)
        self.time_remaining.setObjectName("time_remaining")
        self.verticalLayout.addWidget(self.time_remaining)
        self.start_stop = QtGui.QPushButton(self.centralwidget)
        self.start_stop.setCheckable(True)
        self.start_stop.setObjectName("start_stop")
        self.verticalLayout.addWidget(self.start_stop)
        self.i_woke_up = QtGui.QPushButton(self.centralwidget)
        self.i_woke_up.setObjectName("i_woke_up")
        self.verticalLayout.addWidget(self.i_woke_up)
        self.more_sleep = QtGui.QPushButton(self.centralwidget)
        self.more_sleep.setObjectName("more_sleep")
        self.verticalLayout.addWidget(self.more_sleep)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.at_time_rb.setText(QtGui.QApplication.translate("MainWindow", "В заданное время", None, QtGui.QApplication.UnicodeUTF8))
        self.through_time_rb.setText(QtGui.QApplication.translate("MainWindow", "Через заданное время", None, QtGui.QApplication.UnicodeUTF8))
        self.time_remaining.setText(QtGui.QApplication.translate("MainWindow", "Осталось: ", None, QtGui.QApplication.UnicodeUTF8))
        self.start_stop.setText(QtGui.QApplication.translate("MainWindow", "Запустить", None, QtGui.QApplication.UnicodeUTF8))
        self.i_woke_up.setText(QtGui.QApplication.translate("MainWindow", "Я проснулся", None, QtGui.QApplication.UnicodeUTF8))
        self.more_sleep.setText(QtGui.QApplication.translate("MainWindow", "Еще поспать", None, QtGui.QApplication.UnicodeUTF8))

