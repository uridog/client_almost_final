# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'log_in_screen1.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import time

from PyQt5 import QtCore, QtGui, QtWidgets
import sys


class Ui_LogInWindow(object):
    def __init__(self, Client):
        self.client = Client

    def setupUi(self, LogInWindow):
        LogInWindow.setObjectName("LogInWindow")
        LogInWindow.resize(800, 750)
        LogInWindow.setMinimumSize(QtCore.QSize(760, 750))
        LogInWindow.setStyleSheet("background-color:rgb(18, 18, 18);\n"
                                  "")
        self.centralwidget = QtWidgets.QWidget(LogInWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, -20, 721, 381))
        self.label.setMinimumSize(QtCore.QSize(721, 381))
        self.label.setPixmap(QtGui.QPixmap(":/photos/gamelogo.png"))
        self.label.setObjectName("label")
        self.password = QtWidgets.QTextEdit(self.centralwidget)
        self.password.setGeometry(QtCore.QRect(220, 450, 351, 71))
        self.password.setStyleSheet(";background-color: rgb(162, 47, 255);\n"
                                    "font: 75 8pt \"Magneto\"; font-size: 35px;height: 20px;width: 45px;")
        self.password
        self.password.setObjectName("password")
        self.username = QtWidgets.QTextEdit(self.centralwidget)
        self.username.setGeometry(QtCore.QRect(220, 370, 351, 71))
        self.username.setStyleSheet(";background-color: rgb(162, 47, 255);\n"
                                    "font: 75 8pt \"Magneto\"; font-size: 35px;height: 20px;width: 45px;\n"
                                    "")
        self.username.setObjectName("username")
        self.log_in_data = QtWidgets.QPushButton(self.centralwidget)
        self.log_in_data.setGeometry(QtCore.QRect(590, 450, 121, 71))
        self.log_in_data.setStyleSheet("background-color: rgb(0, 255, 255);\n"
                                       "font: 75 8pt \"Magneto\"; font-size: 35px;height: 20px;width: 45px;\n"
                                       "")
        self.log_in_data.setObjectName("log_in_data")
        self.robot_checkbox = QtWidgets.QCheckBox(self.centralwidget)
        self.robot_checkbox.setGeometry(QtCore.QRect(590, 420, 121, 20))
        self.robot_checkbox.setStyleSheet(";background-color: rgb(253, 253, 253);")
        self.robot_checkbox.setObjectName("robot_checkbox")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(290, 530, 191, 31))
        self.label_2.setStyleSheet(";background-color: rgb(253, 253, 253);")
        self.label_2.setObjectName("label_2")
        self.label_2.hide()
        LogInWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(LogInWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        LogInWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(LogInWindow)
        self.statusbar.setObjectName("statusbar")
        LogInWindow.setStatusBar(self.statusbar)

        self.retranslateUi(LogInWindow)
        QtCore.QMetaObject.connectSlotsByName(LogInWindow)
        self.check_for_button_log(LogInWindow)

    def retranslateUi(self, LogInWindow):
        _translate = QtCore.QCoreApplication.translate
        LogInWindow.setWindowTitle(_translate("LogInWindow", "MainWindow"))
        self.label.setText(
            _translate("LogInWindow", "<html><head/><body><p><img src=\":/photos2/logo.png\"/></p></body></html>"))
        self.password.setHtml(_translate("LogInWindow",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'Magneto\'; font-size:35px; font-weight:72; font-style:normal;\">\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:35px;\">enter password</span></p></body></html>"))
        self.username.setHtml(_translate("LogInWindow",
                                         "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                         "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                         "p, li { white-space: pre-wrap; }\n"
                                         "</style></head><body style=\" font-family:\'Magneto\'; font-size:35px; font-weight:72; font-style:normal;\">\n"
                                         "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:35px;\">enter username</span></p></body></html>"))
        self.log_in_data.setText(_translate("LogInWindow", "log-in"))
        self.robot_checkbox.setText(_translate("LogInWindow", "I am not a robot"))
        self.label_2.setText(_translate("LogInWindow", " username or password are incorrect!"))

    def check_for_button_log(self, MainWindow):
        self.log_in_data.clicked.connect(lambda: self.log_in_pressed(MainWindow))

    def log_in_pressed(self, MainWindow):
        print("log-in pressed")
        self.client.username = self.username.toPlainText()
        self.client.password = self.password.toPlainText()
        time.sleep(1)
        if self.client.client_singed is True:
            MainWindow.close()

import photos2


def show_window(window):
    app2 = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    window.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app2.exec_())


