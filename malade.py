# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'malade.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from subprocess import call


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(838, 404)
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(-10, 0, 851, 411))
        self.label_7.setStyleSheet("background-image: url(:/image/white.jpg);")
        self.label_7.setText("")
        self.label_7.setPixmap(QtGui.QPixmap(":/image/white.jpg"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(370, 0, 81, 71))
        self.label_6.setStyleSheet("background-image: url(:/image/6.png);")
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap(":/image/6.png"))
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(0, 90, 831, 171))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(200, 240, 111, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_1 = QtWidgets.QPushButton(Form)
        self.pushButton_1.setGeometry(QtCore.QRect(500, 240, 111, 41))
        self.pushButton_1.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(350, 240, 111, 41))
        self.pushButton_2.setObjectName("pushButton")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(
            _translate(
                "Form",
                '<html><head/><body><p align="center"><span style=" font-size:22pt;">Unfortunately, you may be ill</span></p><p align="center"><span style=" font-size:16pt;">We suggest you to visit a doctor, here is a form to fill:</span></p></body></html>',
            )
        )
        self.pushButton.setText(_translate("Form", "Disconnect"))
        self.pushButton_1.setText(_translate("Form", "Form"))
        self.pushButton_2.setText(_translate("Form", "New Test"))
        self.pushButton_1.clicked.connect(self.call)
        self.pushButton.clicked.connect(self.deconnect)
        self.pushButton_2.clicked.connect(self.back)

    def call(self):
        Form.destroy()
        call(
            [
                "python",
                "C://Users/asus/Desktop/projet/Projet_Leucocorie_Khaled_Aziz_Hamza/formulaire.py",
            ]
        )

    def deconnect(self):
        Form.destroy()
        call(
            [
                "python",
                "C://Users/asus/Desktop/projet/Projet_Leucocorie_Khaled_Aziz_Hamza/login.py",
            ]
        )

    def back(self):
        Form.destroy()
        call(
            [
                "python",
                "C://Users/asus/Desktop/projet/Projet_Leucocorie_Khaled_Aziz_Hamza/bienvenue.py",
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
