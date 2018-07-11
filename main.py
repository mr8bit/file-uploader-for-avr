#!/usr/bin/python

import sys
from PyQt5 import QtWidgets
import os  # Отсюда нам понадобятся методы для отображения содержимого директорий
import serial.tools.list_ports
import getopt
import os
import sys
import design
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


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.path_file = ''
        self.boud = ''
        self.com_port = ''
        self.pushButton.clicked.connect(self.browse_folder)
        for item in serial.tools.list_ports.comports():
            self.listWidget.addItem(item.device)
        for boud in baudrates:
            self.listWidget_2.addItem(str(boud))
        self.label_2.setWordWrap(True)

        self.pushButton_2.clicked.connect(self.get_param)

    def get_param(self):
        try:
            self.boud = self.listWidget_2.currentItem().text()
        except:
            buttonReply = QtWidgets.QMessageBox.question(self, 'Ошибка', "Выберите скорость предачи.",
                                                         QtWidgets.QMessageBox.Ok)
        try:
            self.com_port = self.listWidget.currentItem().text()
        except:
            buttonReply = QtWidgets.QMessageBox.question(self, 'Ошибка', "Выберите COM порт.",
                                                         QtWidgets.QMessageBox.Ok)
        if not self.path_file:
            buttonReply = QtWidgets.QMessageBox.question(self, 'Ошибка', "Выберите файл для прошивки.",
                                                         QtWidgets.QMessageBox.Ok)
        else:
            if self.path_file.endswith('.hex'):
                in_file = self.path_file
                out_file = '{0}.bin'.format(self.path_file.split('.')[0])
                hex2bin(in_file, out_file)
            else:
                out_file = self.path_file
            ser = serial.Serial()
            ser.baudrate = int(self.boud)
            ser.port = self.com_port
            if not ser.is_open:
                ser.open()
            with open(out_file, "rb") as f:
                byte = f.read(16)
                while byte != b'': # Окончание бинарного файла
                    byte = f.read(16)
                    ser.write(byte)
            ser.close()
            buttonReply = QtWidgets.QMessageBox.question(self, 'Успешно', "Отправка данных успешно завершена",
                                                         QtWidgets.QMessageBox.Ok)
    def browse_folder(self):
        self.label_2.clear()  # На случай, если в списке уже есть элементы
        file = QtWidgets.QFileDialog.getOpenFileName(self, "Выберите файл")
        # открыть диалог выбора директории и установить значение переменной
        # равной пути к выбранной директории
        self.label_2.setText(file[0])
        self.path_file = file[0]


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
