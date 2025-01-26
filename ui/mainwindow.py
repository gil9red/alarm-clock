#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "ipetrash"


import sys
import traceback
from pathlib import Path

from PyQt5.QtCore import Qt, QTimer, QTime, QUrl, QSettings, QEvent
from PyQt5.QtGui import QCloseEvent, QIcon
from PyQt5.QtMultimedia import QMediaPlaylist, QMediaPlayer, QMediaContent
from PyQt5.QtWidgets import (
    QMainWindow,
    QButtonGroup,
    QSystemTrayIcon,
    QMenu,
    QMessageBox,
    QWidget,
    QSlider,
    QLabel,
    QToolButton,
    QStyle,
    QHBoxLayout,
    QVBoxLayout,
)

from ui.mainwindow_ui import Ui_MainWindow

from config import SETTINGS_FILE_NAME, DIR_ICONS


def log_uncaught_exceptions(ex_cls, ex, tb):
    text = f"{ex_cls.__name__}: {ex}:\n"
    text += "".join(traceback.format_tb(tb))

    print(text)
    QMessageBox.critical(None, "Error", text)
    sys.exit(1)


sys.excepthook = log_uncaught_exceptions


def get_total_seconds(t: QTime) -> int:
    return t.hour() * 3600 + t.minute() * 60 + t.second()


def add_to_current_time(t: QTime) -> QTime:
    secs = get_total_seconds(t)
    return QTime.currentTime().addSecs(secs)


class PlayerView(QWidget):
    def __init__(self, player: QMediaPlayer):
        super().__init__()

        self.duration_slider = QSlider(Qt.Horizontal)
        self.duration_slider.setEnabled(False)

        self.duration_label = QLabel()

        self.mute_button = QToolButton()
        self.mute_button.setEnabled(False)
        self.mute_button.setAutoRaise(True)
        self.mute_button.setIcon(self.style().standardIcon(QStyle.SP_MediaVolume))

        self.volume_slider = QSlider(Qt.Horizontal)
        self.volume_slider.setEnabled(False)
        self.volume_slider.setRange(0, 100)

        self.player = player
        self.player.durationChanged.connect(
            lambda duration: self.duration_slider.setRange(0, duration // 1000)
        )
        self.player.positionChanged.connect(self._position_changed)
        self.player.volumeChanged.connect(self.volume_slider.setValue)

        layout = QHBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.duration_slider)
        layout.addWidget(self.duration_label)

        layout_buttons = QHBoxLayout()
        layout_buttons.setContentsMargins(0, 0, 0, 0)
        layout_buttons.setSpacing(0)
        layout_buttons.addWidget(self.mute_button)
        layout_buttons.addWidget(self.volume_slider)

        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.addLayout(layout)
        main_layout.addLayout(layout_buttons)
        self.setLayout(main_layout)

    def _position_changed(self, pos: int):
        # TODO: с этим условием при кликах на тело слайдера, ползунок слайдера сдвинется
        # но медиа не будет перемотано
        if not self.duration_slider.isSliderDown():
            self.duration_slider.setValue(pos // 1000)

        self._update_duration_info()

    def _update_duration_info(self):
        ms_pattern = "{:0>2}:{:0>2}"
        hms_pattern = "{}:" + ms_pattern

        seconds = self.duration_slider.value()
        current_minutes, current_seconds = divmod(seconds, 60)
        current_hours, current_minutes = divmod(current_minutes, 60)
        if current_hours > 0:
            current = hms_pattern.format(
                current_hours, current_minutes, current_seconds
            )
        else:
            current = ms_pattern.format(current_minutes, current_seconds)

        total_seconds = self.duration_slider.maximum()
        total_minutes, total_seconds = divmod(total_seconds, 60)
        total_hours, total_minutes = divmod(total_minutes, 60)
        if total_hours > 0:
            total = hms_pattern.format(total_hours, total_minutes, total_seconds)
        else:
            total = ms_pattern.format(total_minutes, total_seconds)

        self.duration_label.setText(current + " / " + total)


class MainWindow(QMainWindow):
    def __init__(self, audio_file_name: Path):
        super().__init__()

        if not audio_file_name.exists():
            QMessageBox.warning(
                self,
                "Файл не существует",
                f'Не найден файл "{audio_file_name}"',
            )
            sys.exit(1)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.time_remaining.clear()

        self.icon_alarm_clock = QIcon(str(DIR_ICONS / "alarm-clock.png"))

        self.setWindowIcon(self.icon_alarm_clock)

        menu_tray = QMenu()
        action_exit = menu_tray.addAction("Выйти")
        action_exit.triggered.connect(super().close)

        self.tray = QSystemTrayIcon(self.icon_alarm_clock)
        self.tray.setContextMenu(menu_tray)
        self.tray.setToolTip(self.windowTitle())
        self.tray.activated.connect(self._on_tray_activated)
        self.tray.show()

        self.read_settings()

        self._button_group = QButtonGroup()
        self._button_group.addButton(self.ui.at_time_rb)
        self._button_group.addButton(self.ui.through_time_rb)
        self._button_group.buttonClicked.connect(self._update_states)

        self.ui.start_stop.clicked.connect(self._start_stop)
        self.ui.more_sleep.clicked.connect(self._more_sleep)
        self.ui.i_woke_up.clicked.connect(self._i_woke_up)

        self._timer = QTimer()
        self._timer.setInterval(100)
        self._timer.timeout.connect(self._tick)

        self._timer_inc_volume = QTimer()
        self._timer_inc_volume.setInterval(500)
        self._timer_inc_volume.timeout.connect(self._inc_volume_tick)

        self._woke_up = False
        self._alarm_time: QTime = None

        self.playlist = QMediaPlaylist()
        self.playlist.setPlaybackMode(QMediaPlaylist.Loop)

        url = QUrl.fromLocalFile(str(audio_file_name))
        self.playlist.addMedia(QMediaContent(url))

        self.player = QMediaPlayer()
        self.player.setPlaylist(self.playlist)

        self.player_controls_view = PlayerView(self.player)
        self.ui.gridLayout.addWidget(
            self.player_controls_view,
            self.ui.gridLayout.rowCount(),  # row
            0,  # column
            2,  # rowSpan
            0,  # columnSpan
        )

        self._update_states()

    def _update_states(self):
        self.ui.at_time.setEnabled(self.ui.at_time_rb.isChecked())
        self.ui.through_time.setEnabled(self.ui.through_time_rb.isChecked())
        self.ui.i_woke_up.setVisible(self._woke_up)
        self.ui.more_sleep.setVisible(self._woke_up)

        if self._woke_up:
            self.ui.start_stop.setChecked(False)

        self.ui.start_stop.setVisible(not self._woke_up)
        if self.ui.start_stop.isChecked():
            self.ui.start_stop.setText("Стоп")
        else:
            self.ui.start_stop.setText("Запустить")

        self.player_controls_view.setVisible(self._woke_up)

        # Корректируем высоту окна после возможного скрытия кнопок
        self.resize(self.width(), self.minimumHeight())

    def _inc_volume_tick(self):
        if self.player.volume() >= 100:
            self._timer_inc_volume.stop()

        self.player.setVolume(self.player.volume() + 1)

    def _tick(self):
        remain = QTime.currentTime().secsTo(self._alarm_time)
        if remain < 0:
            remain += 24 * 3600
        elif remain == 0:
            self._woke_up = True
            self._timer.stop()
            self._update_states()

            self.player.setVolume(1)
            self.player.play()
            self._timer_inc_volume.start()
            self._set_visible(True)

        hh, mm = divmod(remain, 3600)
        mm, ss = divmod(mm, 60)

        alarm_str = self._alarm_time.toString("hh:mm:ss")
        self.ui.time_remaining.setText(
            f"Звонок в {alarm_str}. Осталось: {hh:0>2}:{mm:0>2}:{ss:0>2}"
        )

    def _i_woke_up(self):
        self._woke_up = False
        self.player.stop()
        self._update_states()

    def _start(self):
        self._woke_up = False

        if self.ui.at_time_rb.isChecked():
            self._alarm_time = self.ui.at_time.time()
        elif self.ui.through_time_rb.isChecked():
            t = self.ui.through_time.time()
            self._alarm_time = add_to_current_time(t)

        self._timer.start()
        self._update_states()

    def _stop(self):
        self._woke_up = False
        self._timer.stop()
        self._update_states()

    def _start_stop(self):
        if self.ui.start_stop.isChecked():
            self._start()
        else:
            self._stop()

    def _more_sleep(self):
        self._i_woke_up()

        t = self.ui.through_time.time()
        self._alarm_time = add_to_current_time(t)

        self._timer.start()
        self.ui.start_stop.setChecked(True)
        self._update_states()

    def _set_visible(self, visible: bool):
        self.setVisible(visible)

        if visible:
            self.showNormal()
            self.activateWindow()

    def _on_tray_activated(self, reason: QSystemTrayIcon.ActivationReason):
        if reason == QSystemTrayIcon.ActivationReason.Context:
            return

        self._set_visible(not self.isVisible())

    def changeEvent(self, event: QEvent):
        if event.type() == QEvent.WindowStateChange:
            # Если окно свернули
            if self.isMinimized():
                # Прячем окно с панели задач
                QTimer.singleShot(0, self.hide)

    def read_settings(self):
        ini = QSettings(SETTINGS_FILE_NAME, QSettings.IniFormat)

        if state := ini.value("MainWindow_State"):
            self.restoreState(state)

        if geometry := ini.value("MainWindow_Geometry"):
            self.restoreGeometry(geometry)

        if at_time_rb := ini.value("at_time_rb", type=bool):
            self.ui.at_time_rb.setChecked(at_time_rb)

        if through_time_rb := ini.value("through_time_rb", type=bool):
            self.ui.through_time_rb.setChecked(through_time_rb)

        if at_time := ini.value("at_time"):
            self.ui.at_time.setTime(at_time)

        if through_time := ini.value("through_time"):
            self.ui.through_time.setTime(through_time)

    def write_settings(self):
        ini = QSettings(SETTINGS_FILE_NAME, QSettings.IniFormat)
        ini.setValue("MainWindow_State", self.saveState())
        ini.setValue("MainWindow_Geometry", self.saveGeometry())

        ini.setValue("at_time_rb", self.ui.at_time_rb.isChecked())
        ini.setValue("through_time_rb", self.ui.through_time_rb.isChecked())
        ini.setValue("at_time", self.ui.at_time.time())
        ini.setValue("through_time", self.ui.through_time.time())

    def closeEvent(self, event: QCloseEvent):
        self.write_settings()
        self._i_woke_up()
