# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Tue Aug 25 14:01:48 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(234, 122)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.radioButton = QtGui.QRadioButton(self.centralwidget)
        self.radioButton.setChecked(True)
        self.radioButton.setObjectName("radioButton")
        self.gridLayout.addWidget(self.radioButton, 0, 0, 1, 1)
        self.atTime = QtGui.QTimeEdit(self.centralwidget)
        self.atTime.setTime(QtCore.QTime(7, 0, 0))
        self.atTime.setObjectName("atTime")
        self.gridLayout.addWidget(self.atTime, 0, 1, 1, 1)
        self.radioButton_2 = QtGui.QRadioButton(self.centralwidget)
        self.radioButton_2.setObjectName("radioButton_2")
        self.gridLayout.addWidget(self.radioButton_2, 1, 0, 1, 1)
        self.throughTime = QtGui.QTimeEdit(self.centralwidget)
        self.throughTime.setTime(QtCore.QTime(0, 45, 0))
        self.throughTime.setObjectName("throughTime")
        self.gridLayout.addWidget(self.throughTime, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.timeRemaining = QtGui.QLabel(self.centralwidget)
        self.timeRemaining.setObjectName("timeRemaining")
        self.verticalLayout.addWidget(self.timeRemaining)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.startStop = QtGui.QPushButton(self.centralwidget)
        self.startStop.setCheckable(True)
        self.startStop.setObjectName("startStop")
        self.horizontalLayout.addWidget(self.startStop)
        self.moreSleep = QtGui.QPushButton(self.centralwidget)
        self.moreSleep.setObjectName("moreSleep")
        self.horizontalLayout.addWidget(self.moreSleep)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton.setText(QtGui.QApplication.translate("MainWindow", "В заданное время", None, QtGui.QApplication.UnicodeUTF8))
        self.radioButton_2.setText(QtGui.QApplication.translate("MainWindow", "Через заданное время", None, QtGui.QApplication.UnicodeUTF8))
        self.timeRemaining.setText(QtGui.QApplication.translate("MainWindow", "Осталось: ", None, QtGui.QApplication.UnicodeUTF8))
        self.startStop.setText(QtGui.QApplication.translate("MainWindow", "Запустить", None, QtGui.QApplication.UnicodeUTF8))
        self.moreSleep.setText(QtGui.QApplication.translate("MainWindow", "Еще поспать", None, QtGui.QApplication.UnicodeUTF8))

