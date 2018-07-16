# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_window.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(783, 340)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(660, 270, 99, 27))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(200, 270, 451, 27))
        self.lineEdit.setObjectName("lineEdit")
        self.listView = QtWidgets.QListView(self.centralwidget)
        self.listView.setGeometry(QtCore.QRect(200, 50, 561, 211))
        self.listView.setObjectName("listView")
        self.listView_2 = QtWidgets.QListView(self.centralwidget)
        self.listView_2.setGeometry(QtCore.QRect(10, 50, 171, 101))
        self.listView_2.setObjectName("listView_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 171, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 160, 171, 41))
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label_2")
        self.listView_3 = QtWidgets.QListView(self.centralwidget)
        self.listView_3.setGeometry(QtCore.QRect(10, 210, 171, 91))
        self.listView_3.setObjectName("listView_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(200, 20, 171, 17))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Отправить"))
        self.label.setText(_translate("MainWindow", "Выберите COM порт"))
        self.label_2.setText(_translate("MainWindow", "Выберите скорость передачи"))
        self.label_3.setText(_translate("MainWindow", "Вывод COM порта"))

