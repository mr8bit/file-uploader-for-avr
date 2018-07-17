import webbrowser
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
from hand_send import HandSendWindow
import platform
from difflib import ndiff

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
        self.setFixedSize(343, 478)
        self.setupUi(self)
        self.path_file = ''
        self.boud = ''
        self.com_port = ''
        self.check_folder_and_file_settings() #Вызов функции для проверки существования файла настроек.
        self.filling_the_menu() #Вызов функции для заполнения команд
        self.action_4.triggered.connect(self.open_hand_sender)
        self.action.triggered.connect(self.open_setting_with_program) #При нажатии на кнопку отрываем файл настроек
        self.attach_list_widget()
        self.action_3.triggered.connect(self.open_repository)
        self.pushButton.clicked.connect(self.browse_folder) 
        self.pushButton_2.clicked.connect(self.send_file)
        self.pushButton_3.clicked.connect(self.check_two_bin_file)
        
    def open_repository(self):
        webbrowser.open('https://github.com/mr8bit/file-uploader-for-avr')

    def check_two_bin_file(self):
        with open('./sample/intel_hex.bin', "rb") as f ,open('./sample/intel_hex1.bin', "rb") as f1 :
                byte = f.read(16)
                byte1 = f1.read(16)
                while byte != b'':  # Окончание бинарного файла
                    byte = f.read(16)
                    byte1 = f1.read(16)
                    if byte != byte1:
                        print("SHIT")
        print('end')

    def check_folder_and_file_settings(self):
        """
            Проверка существования папки с файлом настроек.
            И создание в случаем из отсутсвия.
        """
        self.home_dir = os.path.expanduser("~") # Получение папки пользователя
        self.programm_name = 'Proshivator' # Название программы 
        self.setting_file = 'settings.txt' # Название файла с настройками
        self.program_path = '{0}/{1}/{2}'.format(self.home_dir, '/',  self.programm_name) # Путь к папке с настройками
        self.setting_path = "{0}/{1}".format(self.program_path, self.setting_file) # Путь к программе
        try:
            os.makedirs(self.program_path) # Пытаемся создасть папку для файла с настройками
        except OSError as e: # Папка есть, пропускаем ошибку 
            pass
        if not os.path.isfile(self.setting_path): # Проверяем существование файла с настройками
            f = open(self.setting_path, "w+") # Открываем файл для первоначальной иницализации
            f.write("Пример") # Заполняем файл
            f.close() # Закрываем

    def filling_the_menu(self):
        """
            Заполнение список команд.
        """
        f = open(self.setting_path, "r") # Открываем файл
        contents = f.readlines() # Читаем все строки
        for command in contents: # Идем по строкам 
            extractAction = QtWidgets.QAction(command.split('\n')[0], self) # Создаем элементы
            extractAction.triggered.connect(self.send_command) #Обработчик функции при нажатии на команду
            self.menu_3.addAction(extractAction) # Добавляем в меню
    
    def attach_list_widget(self):
        """
            Добавить листы в виджет списка.
        """
        for item in serial.tools.list_ports.comports():
            self.listWidget.addItem(item.device) #Добавить элмент в выбор COM порта
        for boud in baudrates: 
            self.listWidget_2.addItem(str(boud)) #Добавить элменет в выбор скорости передачи
        
    def open_setting_with_program(self):
        """
            Открыть файл настроек в соответсвии с операционной системой.
        """
        if platform.system() == 'Linux':
            os.system("open "+self.setting_path)
        elif platform.system() == 'Darwin':
            os.system("open "+self.setting_path)
        elif platform.system() == 'Windows':
            os.system("start "+self.setting_path)

    def open_hand_sender(self):
        """
            Открыть окно ручного ввода.
        """
        self.nd = HandSendWindow(self)
        self.nd.show()

    def send_command(self):
        """
            Отправить команду из меню.
        """
        sender = self.sender() # Принимаем нажатый элемент
        command_to_send = sender.text() #  Извлекаем название элменета
        print("Команда для отправки | {0}".format(command_to_send)) # Выполняем команду отправки элемента 

    def send_file(self):
        
        """
            Отправка файла в COM порт. 
        """
        try: #Проверка на скорость передачи
            self.boud = self.listWidget_2.currentItem().text()
        except:
            buttonReply = QtWidgets.QMessageBox.warning(self, 'Ошибка', "Выберите скорость предачи.",
                                                         QtWidgets.QMessageBox.Ok)
        try: #Проверка на выбранный порт
            self.com_port = self.listWidget.currentItem().text()
        except:
            buttonReply = QtWidgets.QMessageBox.warning(self, 'Ошибка', "Выберите COM порт.",
                                                         QtWidgets.QMessageBox.Ok)
        if not self.path_file: #Проверка на выбранный файл
            buttonReply = QtWidgets.QMessageBox.warning(self, 'Ошибка', "Выберите файл для прошивки.",
                                                         QtWidgets.QMessageBox.Ok)
        else:
            if self.path_file.endswith('.hex'):#Если файл hex
                in_file = self.path_file
                out_file = '{0}.bin'.format(self.path_file.split('.')[0])
                hex2bin(in_file, out_file) #Конвертирование 
            else:
                out_file = self.path_file
            ser = serial.Serial() #Создаем экземпляр подключения к порту
            ser.baudrate = int(self.boud) #Задаем скорость передачи
            ser.port = self.com_port #Задаем порт для подключения
            if not ser.is_open: 
                ser.open() # Если не открыт порт, то открываем.
            with open(out_file, "rb") as f:
                byte = f.read(16)
                while byte != b'':  # Окончание бинарного файла
                    byte = f.read(16)
                    ser.write(byte)
            ser.close() #Закрываем порт
            buttonReply = QtWidgets.QMessageBox.question(self, 'Успешно', "Отправка данных успешно завершена",
                                                         QtWidgets.QMessageBox.Ok) #Выводим сообщение об отправке

    def browse_folder(self):
        """
            Открыть выбор файла.
        """
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
