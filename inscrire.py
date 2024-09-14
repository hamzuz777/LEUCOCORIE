# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sing.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
import mysql.connector
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (
    QDialog,
    QPushButton,
    QMessageBox,
    QVBoxLayout,
    QMainWindow,
    QApplication,
)
from subprocess import call


class Ui_Form(object):
    def setupUi(self, Forms):
        Forms.setObjectName("Forms")
        Forms.setFixedSize(721, 421)
        self.label_2 = QtWidgets.QLabel(Forms)
        self.label_2.setGeometry(QtCore.QRect(-10, -10, 301, 441))
        self.label_2.setStyleSheet("background-image: url(:/image/2.png);")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap(":/newPrefix/2.png"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.pushButton_3 = QtWidgets.QPushButton(Forms)
        self.pushButton_3.setGeometry(QtCore.QRect(90, 250, 111, 41))
        self.pushButton_3.setStyleSheet(
            "QPushButton{\n"
            "border-radius: 20px ;\n"
            "    background-color: rgb(255, 255, 255);\n"
            "}"
        )
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_3 = QtWidgets.QLabel(Forms)
        self.label_3.setGeometry(QtCore.QRect(20, 120, 261, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(Forms)
        self.label.setGeometry(QtCore.QRect(300, 80, 401, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Forms)
        self.lineEdit.setGeometry(QtCore.QRect(310, 220, 161, 41))
        self.lineEdit.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit.setStyleSheet(
            "QLineEdit{\n"
            "    background-color: rgb(236, 236, 236);\n"
            "\n"
            "border-radius: 20px ;\n"
            "}"
        )
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_4 = QtWidgets.QLabel(Forms)
        self.label_4.setGeometry(QtCore.QRect(10, 180, 271, 61))
        self.label_4.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(Forms)
        self.pushButton.setGeometry(QtCore.QRect(430, 300, 111, 41))
        self.pushButton.setStyleSheet(
            "QPushButton{\n"
            "    color: rgb(0, 0, 0);\n"
            "border-radius: 20px ;\n"
            "    background-image: url(:/image/2.png);\n"
            "}\n"
            ""
        )
        self.pushButton.setCheckable(True)
        self.pushButton.setChecked(True)
        self.pushButton.setAutoRepeatDelay(1000)
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_3 = QtWidgets.QLineEdit(Forms)
        self.lineEdit_3.setGeometry(QtCore.QRect(500, 220, 161, 41))
        self.lineEdit_3.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_3.setStyleSheet(
            "QLineEdit{\n"
            "    background-color: rgb(236, 236, 236);\n"
            "\n"
            "border-radius: 20px ;\n"
            "}"
        )
        self.lineEdit_3.setText("")
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(Forms)
        self.lineEdit_2.setGeometry(QtCore.QRect(500, 170, 161, 41))
        self.lineEdit_2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_2.setStyleSheet(
            "QLineEdit{\n"
            "    background-color: rgb(236, 236, 236);\n"
            "\n"
            "border-radius: 20px ;\n"
            "}"
        )
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_4 = QtWidgets.QLineEdit(Forms)
        self.lineEdit_4.setGeometry(QtCore.QRect(310, 170, 161, 41))
        self.lineEdit_4.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_4.setStyleSheet(
            "QLineEdit{\n"
            "    background-color: rgb(236, 236, 236);\n"
            "\n"
            "border-radius: 20px ;\n"
            "}"
        )
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_6 = QtWidgets.QLabel(Forms)
        self.label_6.setGeometry(QtCore.QRect(450, 10, 81, 71))
        self.label_6.setStyleSheet("background-image: url(:/image/6.png);")
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(":/image/6.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label_5 = QtWidgets.QLabel(Forms)
        self.label_5.setGeometry(QtCore.QRect(290, -5, 441, 431))
        self.label_5.setStyleSheet("background-image: url(:/image/white.jpg);")
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap(":/image/white.jpg"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.label_5.raise_()
        self.label_2.raise_()
        self.pushButton_3.raise_()
        self.label_3.raise_()
        self.label.raise_()
        self.lineEdit.raise_()
        self.label_4.raise_()
        self.pushButton.raise_()
        self.lineEdit_3.raise_()
        self.lineEdit_2.raise_()
        self.lineEdit_4.raise_()
        self.label_6.raise_()

        self.retranslateUi(Forms)
        QtCore.QMetaObject.connectSlotsByName(Forms)
        Forms.setTabOrder(self.lineEdit_4, self.lineEdit_2)
        Forms.setTabOrder(self.lineEdit_2, self.lineEdit)
        Forms.setTabOrder(self.lineEdit, self.lineEdit_3)
        Forms.setTabOrder(self.lineEdit_3, self.pushButton)
        Forms.setTabOrder(self.pushButton, self.pushButton_3)

    def retranslateUi(self, Forms):
        _translate = QtCore.QCoreApplication.translate
        Forms.setWindowTitle(_translate("Forms", "Forms"))
        self.pushButton_3.setText(_translate("Forms", "Sign in"))
        self.label_3.setText(_translate("Forms", "One of Us?"))
        self.label.setText(
            _translate(
                "Forms",
                '<html><head/><body><p align="center">Create an account</p></body></html>',
            )
        )
        self.lineEdit.setPlaceholderText(_translate("Form", "Email"))
        self.label_4.setText(
            _translate(
                "Forms",
                '<html><head/><body><p align="center">If you already have an account, just log in.</p></body></html>',
            )
        )
        self.pushButton.setText(_translate("Forms", "Sign up"))
        self.lineEdit_3.setPlaceholderText(_translate("Forms", "Password"))
        self.lineEdit_2.setPlaceholderText(_translate("Forms", "First Name"))
        self.lineEdit_4.setPlaceholderText(_translate("Forms", "Last Name"))
        self.pushButton_3.clicked.connect(self.Button_clickede)
        self.pushButton.clicked.connect(self.log)

    def connecting(self):
        try:
            self.mydb = mysql.connector.connect(
                host="localhost", user="root", passwd="", db="login"
            )
            self.mysqlcursor = self.mydb.cursor()
        except mysql.connector.errors.ProgrammingError as error:
            print("Review the Error -->", error)

    def log(self):
        self.connecting()
        nom = self.lineEdit_4.text()
        prenom = self.lineEdit_2.text()
        email = self.lineEdit.text()
        password = self.lineEdit_3.text()
        get_data = (nom, prenom, email, password)
        query = "INSERT INTO usuario (nome, prenom, email, password) VALUES (%s, %s, %s, %s)"
        self.mysqlcursor.execute(query, get_data)
        self.mydb.commit()
        QMessageBox.warning(
            None, "Account", "Congratulations, the account is created", QMessageBox.Ok
        )
        Forms.destroy()
        call(
            [
                "python",
                "C://Users/asus/Desktop/projet/Projet_Leucocorie_Khaled_Aziz_Hamza/inscrire.py",
            ]
        )

    def Button_clickede(self):
        Forms.destroy()
        call(
            [
                "python",
                "C://Users/asus/Desktop/projet/Projet_Leucocorie_Khaled_Aziz_Hamza/login.py",
            ]
        )


import image_rc


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Forms = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Forms)
    Forms.show()
    sys.exit(app.exec_())
