#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'


# TODO: сделать версию функции для PySide/PyQt4/PyQt5
def load_qt4_plugins():
    """
    Функция загружает Qt плагины.

    """

    import PySide
    import os

    qApp = PySide.QtGui.QApplication.instance()

    for plugins_dir in [os.path.join(p, "plugins") for p in PySide.__path__]:
        qApp.addLibraryPath(plugins_dir)


if __name__ == '__main__':
    import sys
    from PySide.QtGui import QApplication
    from mainwindow import MainWindow

    app = QApplication(sys.argv)

    load_qt4_plugins()

    mw = MainWindow('Пилигрим - Стереть.mp3')
    mw.setWindowTitle('Будильник')
    mw.show()

    sys.exit(app.exec_())
