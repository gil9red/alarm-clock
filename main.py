#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


if __name__ == '__main__':
    import sys
    from PySide.QtGui import QApplication
    from mainwindow import MainWindow

    app = QApplication(sys.argv)

    mw = MainWindow('Пилигрим - Стереть.mp3')
    mw.setWindowTitle('Будильник')
    mw.show()

    sys.exit(app.exec_())
