#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'

from PySide.QtGui import *
from PySide.QtCore import *

from mainwindow_ui import Ui_MainWindow


# Возможности:
#  - Установка времени звонка
#  - Через сколько позвонить
#  - Обратный отсчет
#  - Зацикливание звонка пока не отключен
#  - Постепенное увеличение громкости: от 0 до 100


class MainWindow(QMainWindow, QObject):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
