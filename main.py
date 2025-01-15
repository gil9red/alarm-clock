#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "ipetrash"


# TODO: добавить батник сборки ехе через pyinstaller


import sys
from argparse import ArgumentParser
from pathlib import Path

from PyQt5.QtWidgets import QApplication

from config import MUSIC_PATH
from ui.mainwindow import MainWindow


arg_parser = ArgumentParser()
arg_parser.add_argument(
    "--music_file",
    type=Path,
    default=MUSIC_PATH,
)

parsed_args = arg_parser.parse_args()

app = QApplication(sys.argv)

font = app.font()
font.setPointSize(font.pointSize() + 8)
app.setFont(font)

mw = MainWindow(parsed_args.music_file)
mw.show()

sys.exit(app.exec_())
