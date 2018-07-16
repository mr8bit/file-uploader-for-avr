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
    def check_folder_and_file_settings(self):
        """
            Проверка существования папки с файлом настроек. И создание в случаем из отсутсвия.
        """
        self.home_dir = os.path.expanduser("~") # Получение папки пользователя
        self.programm_name = 'Proshivator' # Название программы 
        self.setting_file = 'settings.txt' # Название файла с настройками
        self.program_path = '{0}/{1}/{2}'.format(self.home_dir, '/',  self.programm_name) # Путь к папке с настройками
        try:
            os.makedirs(self.program_path) # Пытаемся создасть папку для файла с настройками
        except OSError as e: # Папка есть, пропускаем ошибку 
            pass
        if not os.path.isfile("{0}/{1}".format(self.program_path, self.setting_file)): # Проверяем существование файла с настройками
            f = open("{0}/{1}".format(self.program_path, self.setting_file), "w+") # Открываем файл для первоначальной иницализации
            f.write("Пример") # Заполняем файл
            f.close() # Закрываем

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.path_file = ''
        self.boud = ''
        self.com_port = ''
        self.check_folder_and_file_settings()
        self.pushButton.clicked.connect(self.browse_folder)
        for item in serial.tools.list_ports.comports():
            self.listWidget.addItem(item.device)
        for boud in baudrates:
            self.listWidget_2.addItem(str(boud))
        self.label_2.setWordWrap(True)
        self.pushButton_2.clicked.connect(self.get_param)

        # Получить папку пользователя
        
    
        f = open("{0}/settings.txt".format(self.program_path), "r")
        contents = f.readlines()
        for command in contents:
            extractAction = QtWidgets.QAction(command.split('\n')[0], self)
            self.menu_3.addAction(extractAction)

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
                while byte != b'':  # Окончание бинарного файла
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
