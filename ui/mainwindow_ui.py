# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(324, 214)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.at_time_rb = QtWidgets.QRadioButton(self.centralwidget)
        self.at_time_rb.setChecked(True)
        self.at_time_rb.setObjectName("at_time_rb")
        self.gridLayout.addWidget(self.at_time_rb, 0, 0, 1, 1)
        self.at_time = QtWidgets.QTimeEdit(self.centralwidget)
        self.at_time.setTime(QtCore.QTime(9, 0, 0))
        self.at_time.setObjectName("at_time")
        self.gridLayout.addWidget(self.at_time, 0, 1, 1, 1)
        self.through_time_rb = QtWidgets.QRadioButton(self.centralwidget)
        self.through_time_rb.setObjectName("through_time_rb")
        self.gridLayout.addWidget(self.through_time_rb, 1, 0, 1, 1)
        self.through_time = QtWidgets.QTimeEdit(self.centralwidget)
        self.through_time.setCurrentSection(QtWidgets.QDateTimeEdit.HourSection)
        self.through_time.setTime(QtCore.QTime(0, 10, 0))
        self.through_time.setObjectName("through_time")
        self.gridLayout.addWidget(self.through_time, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.time_remaining = QtWidgets.QLabel(self.centralwidget)
        self.time_remaining.setObjectName("time_remaining")
        self.verticalLayout.addWidget(self.time_remaining)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.start_stop = QtWidgets.QPushButton(self.centralwidget)
        self.start_stop.setCheckable(True)
        self.start_stop.setObjectName("start_stop")
        self.verticalLayout.addWidget(self.start_stop)
        self.i_woke_up = QtWidgets.QPushButton(self.centralwidget)
        self.i_woke_up.setObjectName("i_woke_up")
        self.verticalLayout.addWidget(self.i_woke_up)
        self.more_sleep = QtWidgets.QPushButton(self.centralwidget)
        self.more_sleep.setObjectName("more_sleep")
        self.verticalLayout.addWidget(self.more_sleep)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Будильник"))
        self.at_time_rb.setText(_translate("MainWindow", "В заданное время"))
        self.at_time.setDisplayFormat(_translate("MainWindow", "HH:mm:ss"))
        self.through_time_rb.setText(_translate("MainWindow", "Через заданное время"))
        self.through_time.setDisplayFormat(_translate("MainWindow", "HH:mm:ss"))
        self.time_remaining.setText(_translate("MainWindow", "Осталось: "))
        self.start_stop.setText(_translate("MainWindow", "Запустить"))
        self.i_woke_up.setText(_translate("MainWindow", "Я проснулся"))
        self.more_sleep.setText(_translate("MainWindow", "Еще поспать"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
