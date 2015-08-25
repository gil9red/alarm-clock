#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'ipetrash'

from PySide.QtGui import *
from PySide.QtCore import *
from PySide.phonon import Phonon

from mainwindow_ui import Ui_MainWindow


class MainWindow(QMainWindow, QObject):
    def __init__(self, audio_file_name):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

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

        self._woke_up = False
        self._alarm_time = None

        self._timer_inc_volume = QTimer()
        self._timer_inc_volume.setInterval(500)
        self._timer_inc_volume.timeout.connect(self._inc_volume_tick)

        self.audio_file_name = audio_file_name

        self.audio = Phonon.MediaObject()
        self.audio.setCurrentSource(Phonon.MediaSource(audio_file_name))
        self.audio.finished.connect(self._restart_audio)

        self.output = Phonon.AudioOutput(Phonon.MusicCategory)

        Phonon.createPath(self.audio, self.output)

        self._update_states()

    def _restart_audio(self):
        self.audio.setCurrentSource(Phonon.MediaSource(self.audio_file_name))
        self.audio.play()

    def _update_states(self):
        self.ui.at_time.setEnabled(self.ui.at_time_rb.isChecked())
        self.ui.through_time.setEnabled(self.ui.through_time_rb.isChecked())
        self.ui.i_woke_up.setVisible(self._woke_up)
        self.ui.more_sleep.setVisible(self._woke_up)

        if self._woke_up:
            self.ui.start_stop.setChecked(False)

        self.ui.start_stop.setVisible(not self._woke_up)
        if self.ui.start_stop.isChecked():
            self.ui.start_stop.setText('Стоп')
        else:
            self.ui.start_stop.setText('Запустить')

        self.resize(self.minimumSize())

    def _inc_volume_tick(self):
        if self.output.volume() >= 1.0:
            self._timer_inc_volume.stop()

        self.output.setVolume(self.output.volume() + 0.01)

    def _tick(self):
        cur_time = QTime.currentTime()
        remain = cur_time.secsTo(self._alarm_time)
        if remain < 0:
            remain += 24 * 3600
        elif remain == 0:
            self._woke_up = True
            self._timer.stop()
            self._update_states()

            self.output.setVolume(0.01)
            self.audio.play()
            self._timer_inc_volume.start()

        h = int(remain / 3600)
        m = int((remain - h * 3600) / 60)
        s = remain % 60

        remain = h, m, s

        alarm_str = self._alarm_time.toString('hh:mm:ss')
        self.ui.time_remaining.setText('Звонок в {}. Осталось: {:0>2}:{:0>2}:{:0>2}'.format(alarm_str, *remain))

    def _i_woke_up(self):
        self._woke_up = False
        self.audio.stop()
        self._update_states()

    def _start(self):
        self._woke_up = False

        if self.ui.at_time_rb.isChecked():
            self._alarm_time = self.ui.at_time.time()
        elif self.ui.through_time_rb.isChecked():
            cur_time = QTime.currentTime()

            t = self.ui.through_time.time()
            secs = t.hour() * 3600 + t.minute() * 60 + t.second()
            self._alarm_time = cur_time.addSecs(secs)

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

        self._alarm_time = self._alarm_time.addSecs(15 * 60)
        self._timer.start()
        self.ui.start_stop.setChecked(True)
        self._update_states()
