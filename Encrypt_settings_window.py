# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Encrypt_settings_window.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Encrypt_settings_window(object):
    def setupUi(self, Encrypt_settings_window):
        Encrypt_settings_window.setObjectName("Encrypt_settings_window")
        Encrypt_settings_window.resize(860, 616)
        self.plainText1Edit = QtWidgets.QPlainTextEdit(Encrypt_settings_window)
        self.plainText1Edit.setGeometry(QtCore.QRect(10, 40, 391, 141))
        self.plainText1Edit.setObjectName("plainText1Edit")
        self.label_Text1 = QtWidgets.QLabel(Encrypt_settings_window)
        self.label_Text1.setGeometry(QtCore.QRect(11, 4, 51, 31))
        self.label_Text1.setObjectName("label_Text1")
        self.label = QtWidgets.QLabel(Encrypt_settings_window)
        self.label.setGeometry(QtCore.QRect(450, 10, 51, 21))
        self.label.setObjectName("label")
        self.text1Key1Edit = QtWidgets.QTextEdit(Encrypt_settings_window)
        self.text1Key1Edit.setGeometry(QtCore.QRect(440, 60, 391, 91))
        self.text1Key1Edit.setObjectName("text1Key1Edit")
        self.label_Text2 = QtWidgets.QLabel(Encrypt_settings_window)
        self.label_Text2.setGeometry(QtCore.QRect(10, 240, 51, 31))
        self.label_Text2.setObjectName("label_Text2")
        self.plainText2Edit = QtWidgets.QPlainTextEdit(Encrypt_settings_window)
        self.plainText2Edit.setGeometry(QtCore.QRect(10, 280, 371, 151))
        self.plainText2Edit.setObjectName("plainText2Edit")
        self.text1Key2Edit = QtWidgets.QTextEdit(Encrypt_settings_window)
        self.text1Key2Edit.setGeometry(QtCore.QRect(440, 300, 381, 81))
        self.text1Key2Edit.setObjectName("text1Key2Edit")
        self.label_2 = QtWidgets.QLabel(Encrypt_settings_window)
        self.label_2.setGeometry(QtCore.QRect(450, 250, 51, 31))
        self.label_2.setObjectName("label_2")
        self.pushButtonEncryptFinally = QtWidgets.QPushButton(Encrypt_settings_window)
        self.pushButtonEncryptFinally.setGeometry(QtCore.QRect(340, 550, 161, 51))
        self.pushButtonEncryptFinally.setObjectName("pushButtonEncryptFinally")

        self.retranslateUi(Encrypt_settings_window)
        QtCore.QMetaObject.connectSlotsByName(Encrypt_settings_window)

    def retranslateUi(self, Encrypt_settings_window):
        _translate = QtCore.QCoreApplication.translate
        Encrypt_settings_window.setWindowTitle(_translate("Encrypt_settings_window", "Dialog"))
        self.label_Text1.setText(_translate("Encrypt_settings_window", "Text1"))
        self.label.setText(_translate("Encrypt_settings_window", "Key1"))
        self.label_Text2.setText(_translate("Encrypt_settings_window", "Text2"))
        self.label_2.setText(_translate("Encrypt_settings_window", "Key2"))
        self.pushButtonEncryptFinally.setText(_translate("Encrypt_settings_window", "Encrypt!"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Encrypt_settings_window = QtWidgets.QDialog()
    ui = Ui_Encrypt_settings_window()
    ui.setupUi(Encrypt_settings_window)
    Encrypt_settings_window.show()
    sys.exit(app.exec_())