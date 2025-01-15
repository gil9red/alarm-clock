#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = "ipetrash"


from pathlib import Path


DIR = Path(__file__).resolve().parent

SETTINGS_FILE_NAME: str = str(DIR / "settings.ini")

DIR_RESOURCES: DIR = DIR / "resources"
DIR_ICONS: DIR = DIR_RESOURCES / "icons"

MUSIC_PATH: Path = DIR_RESOURCES / "musics" / "Der Tag - mondmatt.mp3"
