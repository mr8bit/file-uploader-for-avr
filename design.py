# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(343, 478)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 70, 301, 30))
        self.pushButton.setObjectName("pushButton")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(20, 200, 141, 101))
        self.listWidget.setObjectName("listWidget")
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(180, 200, 141, 101))
        self.listWidget_2.setObjectName("listWidget_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 320, 301, 51))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 150, 141, 51))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 20, 291, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 150, 141, 51))
        self.label_3.setObjectName("label_3")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(20, 110, 291, 31))
        self.checkBox.setObjectName("checkBox")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 390, 301, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 343, 25))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        self.menu_3 = QtWidgets.QMenu(self.menuBar)
        self.menu_3.setObjectName("menu_3")
        self.menu_4 = QtWidgets.QMenu(self.menuBar)
        self.menu_4.setObjectName("menu_4")

        MainWindow.setMenuBar(self.menuBar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_4")

        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_3)
        self.menu_4.addAction(self.action_4)
        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menu_3.menuAction())
        self.menuBar.addAction(self.menu_4.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Прошиватор"))
        self.pushButton.setText(_translate("MainWindow", "Выберите файл"))
        self.pushButton_2.setText(_translate("MainWindow", "Прошить"))
        self.label.setText(_translate("MainWindow", "Cкорость передачи \n"
" в бодах"))
        self.label_2.setText(_translate("MainWindow", "Файл не выбран"))
        self.label_3.setText(_translate("MainWindow", "Доступные COM \n"
" порты"))
        self.checkBox.setText(_translate("MainWindow", "Сравнить при отправке"))
        self.pushButton_3.setText(_translate("MainWindow", "Сравнить"))
        self.menu.setTitle(_translate("MainWindow", "Настройки"))
        self.menu_3.setTitle(_translate("MainWindow", "Команды"))
        self.action_4.setText(_translate("MainWindow", "Начать ввод"))

        self.menu_4.setTitle(_translate("MainWindow", "Ручной ввод"))
        self.action.setText(_translate("MainWindow", "Добавить команды"))
        self.action_2.setText(_translate("MainWindow", "Репозиторий"))
        self.action_3.setText(_translate("MainWindow", "О программе"))