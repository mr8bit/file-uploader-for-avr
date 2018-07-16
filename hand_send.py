#!/usr/bin/python

import sys
from PyQt5 import QtWidgets
import os  # Отсюда нам понадобятся методы для отображения содержимого директорий
import serial.tools.list_ports
import getopt
import os
import sys
import new_window
from intelhex import hex2bin
import serial

baudrates = [
    300,
    600,
    1200,
    2400,
    4800,
    9600,
    19200,
    38400,
    57600,
    115200,
    230400,
    460800,
    921600
]

class HandSendWindow(QtWidgets.QMainWindow, new_window.Ui_MainWindow):
     def __init__(self, parent):
        super(HandSendWindow, self).__init__(parent)
        self.setupUi(self)
        for item in serial.tools.list_ports.comports():
            self.listWidget_3.addItem(item.device)
        for boud in baudrates:
            self.listWidget_2.addItem(str(boud))