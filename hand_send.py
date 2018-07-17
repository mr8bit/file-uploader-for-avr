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
        self.setFixedSize(774, 340)
        self.attach_list_widget()
        self.pushButton.clicked.connect(self.send_commad_from_input) 

    def send_commad_from_input(self):
        self.to_send = self.lineEdit.text()
        if not self.to_send:
            buttonReply = QtWidgets.QMessageBox.warning(self, 'Внимание', "Вы не ввели команду",
                                                         QtWidgets.QMessageBox.Ok) 
        if self.check_selected_com_boud():
            ser = serial.Serial() #Создаем экземпляр подключения к порту
            ser.baudrate = int(self.boud) #Задаем скорость передачи
            ser.port = self.com_port #Задаем порт для подключения
            if not ser.is_open: 
                ser.open() # Если не открыт порт, то открываем.
            ser.write(self.to_send)
            ser.close()
        
    def read_from_com_port(self):
        if self.check_selected_com_boud():
            ser = serial.Serial() #Создаем экземпляр подключения к порту
            ser.baudrate = int(self.boud) #Задаем скорость передачи
            ser.port = self.com_port #Задаем порт для подключения
            if not ser.is_open: 
                ser.open() # Если не открыт порт, то открываем.
            while True:
                for c in ser.read():
                    self.self.listWidget.addItem(str(c))
                    if c == '\n':
                        print("Line: " + ''.join(line))
                        break

    def check_selected_com_boud(self):
        try: #Проверка на скорость передачи
            self.boud = self.listWidget_2.currentItem().text()
        except:
            buttonReply = QtWidgets.QMessageBox.warning(self, 'Ошибка', "Выберите скорость предачи.",
                                                         QtWidgets.QMessageBox.Ok)
            return False
        try: #Проверка на выбранный порт
            self.com_port = self.listWidget_3.currentItem().text()
        except:
            buttonReply = QtWidgets.QMessageBox.warning(self, 'Ошибка', "Выберите COM порт.",
                                                         QtWidgets.QMessageBox.Ok)
            return False
        return True
            
    def attach_list_widget(self):
        """
            Добавить листы в виджет списка.
        """
        for item in serial.tools.list_ports.comports():
            self.listWidget_3.addItem(item.device)
        for boud in baudrates:
            self.listWidget_2.addItem(str(boud))