#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "ipetrash"


import sys
from argparse import ArgumentParser
from pathlib import Path

from PyQt6.QtWidgets import QApplication

from alarm_clock.config import MUSIC_PATH
from alarm_clock.ui.mainwindow import MainWindow


def main() -> None:
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

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
