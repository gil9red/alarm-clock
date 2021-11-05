#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


# TODO: добавить батник сборки ехе через pyinstaller


import sys

from PyQt5.QtWidgets import QApplication
from ui.mainwindow import MainWindow


app = QApplication(sys.argv)

mw = MainWindow(r'C:\Users\ipetrash\Music\Эпоха – Ценой великих жертв.mp3')
mw.show()

sys.exit(app.exec_())
