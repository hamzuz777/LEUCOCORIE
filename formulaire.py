# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formulaire.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
import mysql.connector
from PyQt5 import uic

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
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setFixedSize(729, 882)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(100, 90, 491, 51))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(50, 170, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_3.setObjectName("label_3")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(290, 181, 121, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(420, 180, 121, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(320, 220, 51, 21))
        self.label_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_2.setLineWidth(0)
        self.label_2.setMidLineWidth(0)
        self.label_2.setTextFormat(QtCore.Qt.MarkdownText)
        self.label_2.setIndent(-1)
        self.label_2.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(430, 220, 101, 21))
        self.label_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_4.setLineWidth(0)
        self.label_4.setMidLineWidth(0)
        self.label_4.setTextFormat(QtCore.Qt.MarkdownText)
        self.label_4.setIndent(-1)
        self.label_4.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByMouse)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(50, 390, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_5.setObjectName("label_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(290, 400, 231, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(50, 250, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_6.setObjectName("label_6")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(290, 260, 231, 31))
        self.comboBox.setPlaceholderText("")
        self.comboBox.setDuplicatesEnabled(True)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(0, 0, 731, 901))
        self.label_7.setStyleSheet("background-image: url(:/image/white.jpg);")
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(":/image/white.jpg"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(290, 260, 211, 31))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(50, 320, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Form)
        self.label_9.setGeometry(QtCore.QRect(310, 10, 81, 71))
        self.label_9.setStyleSheet("background-image: url(:/image/6.png);")
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap(":/image/6.png"))
        self.label_9.setScaledContents(True)
        self.label_9.setObjectName("label_9")
        self.calendarWidget = QtWidgets.QCalendarWidget(Form)
        self.calendarWidget.setGeometry(QtCore.QRect(130, 250, 392, 236))
        self.calendarWidget.setMinimumSize(QtCore.QSize(392, 0))
        self.calendarWidget.setGridVisible(True)
        self.calendarWidget.setSelectionMode(QtWidgets.QCalendarWidget.SingleSelection)
        self.calendarWidget.setVerticalHeaderFormat(
            QtWidgets.QCalendarWidget.NoVerticalHeader
        )
        self.calendarWidget.setObjectName("calendarWidget")
        self.dateEdit = QtWidgets.QDateEdit(Form)
        self.dateEdit.setGeometry(QtCore.QRect(290, 330, 231, 31))
        self.dateEdit.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.dateEdit.setObjectName("dateEdit")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(490, 330, 31, 31))
        self.pushButton.setStyleSheet("image: url(:/image/calendrier.png);")
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(290, 460, 231, 31))
        self.lineEdit_5.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.lineEdit_5.setText("")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.label_10 = QtWidgets.QLabel(Form)
        self.label_10.setGeometry(QtCore.QRect(50, 450, 241, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Form)
        self.label_11.setGeometry(QtCore.QRect(50, 510, 421, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_11.setObjectName("label_11")
        self.calendarWidget_2 = QtWidgets.QCalendarWidget(Form)
        self.calendarWidget_2.setGeometry(QtCore.QRect(130, 570, 391, 211))
        self.calendarWidget_2.setObjectName("calendarWidget_2")
        self.dateEdit_2 = QtWidgets.QDateEdit(Form)
        self.dateEdit_2.setGeometry(QtCore.QRect(380, 520, 231, 31))
        self.dateEdit_2.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(580, 520, 31, 31))
        self.pushButton_2.setStyleSheet("image: url(:/image/calendrier.png);")
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_12 = QtWidgets.QLabel(Form)
        self.label_12.setGeometry(QtCore.QRect(50, 560, 421, 51))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet("color: rgb(0, 0, 0);")
        self.label_12.setObjectName("label_12")
        self.lineEdit_6 = QtWidgets.QLineEdit(Form)
        self.lineEdit_6.setGeometry(QtCore.QRect(80, 630, 491, 171))
        self.lineEdit_6.setCursorPosition(0)
        self.lineEdit_6.setAlignment(
            QtCore.Qt.AlignLeading | QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop
        )
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(200, 830, 111, 41))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_9 = QtWidgets.QPushButton(Form)
        self.pushButton_9.setGeometry(QtCore.QRect(350, 830, 111, 41))
        self.pushButton_9.setObjectName("pushButton_9")
        self.calendarWidget.raise_()
        self.calendarWidget_2.raise_()
        self.label_7.raise_()
        self.label.raise_()
        self.label_3.raise_()
        self.lineEdit.raise_()
        self.lineEdit_2.raise_()
        self.label_2.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.lineEdit_3.raise_()
        self.label_6.raise_()
        self.comboBox.raise_()
        self.lineEdit_4.raise_()
        self.label_8.raise_()
        self.label_9.raise_()
        self.dateEdit.raise_()
        self.pushButton.raise_()
        self.lineEdit_5.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.dateEdit_2.raise_()
        self.pushButton_2.raise_()
        self.label_12.raise_()
        self.lineEdit_6.raise_()
        self.pushButton_3.raise_()
        self.pushButton_9.raise_()

        self.retranslateUi(Form)
        self.comboBox.setCurrentIndex(-1)
        self.comboBox.currentIndexChanged["QString"].connect(self.lineEdit_4.setText)
        self.calendarWidget.clicked["QDate"].connect(self.calendarWidget.hide)
        self.calendarWidget.clicked["QDate"].connect(self.dateEdit.setDate)
        self.pushButton.clicked.connect(self.calendarWidget.raise_)
        self.pushButton.clicked.connect(self.calendarWidget.show)
        self.calendarWidget_2.clicked["QDate"].connect(self.calendarWidget_2.hide)
        self.calendarWidget_2.clicked["QDate"].connect(self.dateEdit_2.setDate)
        self.pushButton_2.clicked.connect(self.calendarWidget_2.raise_)
        self.pushButton_2.clicked.connect(self.calendarWidget_2.show)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Appointment Form"))
        self.label.setText(_translate("Form", "Request an Appointment"))
        self.label_3.setText(_translate("Form", "Full Name:"))
        self.label_2.setText(_translate("Form", "First Name"))
        self.label_4.setText(_translate("Form", "Last Name"))
        self.label_5.setText(_translate("Form", "Phone Number:"))
        self.label_6.setText(_translate("Form", "Gender:"))
        self.comboBox.setItemText(0, _translate("Form", "Male"))
        self.comboBox.setItemText(1, _translate("Form", "Female"))
        self.lineEdit_4.setPlaceholderText(_translate("Form", "choose your gender"))
        self.label_8.setText(_translate("Form", "Date of Birth:"))
        self.lineEdit_5.setPlaceholderText(_translate("Form", "example@example.com"))
        self.label_10.setText(_translate("Form", "Email:"))
        self.label_11.setText(_translate("Form", "Select an Appointment Date:"))
        self.label_12.setText(_translate("Form", "Comments:"))
        self.pushButton_3.setText(_translate("Form", "Send"))
        self.pushButton_3.clicked.connect(self.log)
        self.pushButton_9.setText(_translate("Form", "Logout"))
        self.pushButton_9.clicked.connect(self.deconnect)

    def deconnect(self):
        Form.destroy()
        call(
            [
                "python",
                "C://Users/asus/Desktop/projet/Projet_Leucocorie_Khaled_Aziz_Hamza/login.py",
            ]
        )

    def connecting(self):
        try:
            self.mydb = mysql.connector.connect(
                host="localhost", user="root", passwd="", db="formulaire"
            )
            self.mysqlcursor = self.mydb.cursor()
        except mysql.connector.errors.ProgrammingError as error:
            print("Review the Error -->", error)

    def log(self):
        self.connecting()

        name = self.lineEdit_2.text()
        first_name = self.lineEdit.text()
        gender = self.lineEdit_4.text()
        date_of_birth = self.dateEdit.text()
        phone_number = self.lineEdit_3.text()
        email = self.lineEdit_5.text()
        appointment_date = self.dateEdit.text()
        comment = self.lineEdit_6.text()

        get_data = (
            name,
            first_name,
            gender,
            phone_number,
            date_of_birth,
            email,
            comment,
            appointment_date,
        )
        query = "INSERT INTO rdv (name, first_name, gender, phone_number, date_of_birth, email, comment, appointment_date) VALUES (%s,%s,%s,%s,%s, %s,%s,%s)"

        self.mysqlcursor.execute(query, get_data)
        self.mydb.commit()
        QMessageBox.warning(
            None, "Account", "Congratulations, request sent ", QMessageBox.Ok
        )
        Form.destroy()
        call(
            [
                "python",
                "C://Users/asus/Desktop/projet/Projet_Leucocorie_Khaled_Aziz_Hamza/formulaire.py",
            ]
        )


import image_rc


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())