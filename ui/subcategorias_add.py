# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'subcategorias_add.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(260, 118)
        Form.setMinimumSize(QtCore.QSize(260, 110))
        Form.setMaximumSize(QtCore.QSize(2000, 2000))
        Form.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.inputNome = QtWidgets.QLineEdit(Form)
        self.inputNome.setGeometry(QtCore.QRect(10, 42, 211, 25))
        self.inputNome.setObjectName("inputNome")
        self.labelNome = QtWidgets.QLabel(Form)
        self.labelNome.setGeometry(QtCore.QRect(20, 22, 54, 17))
        self.labelNome.setObjectName("labelNome")
        self.botaoOk = QtWidgets.QPushButton(Form)
        self.botaoOk.setGeometry(QtCore.QRect(40, 82, 80, 25))
        self.botaoOk.setObjectName("botaoOk")
        self.botaoCancela = QtWidgets.QPushButton(Form)
        self.botaoCancela.setGeometry(QtCore.QRect(150, 82, 80, 25))
        self.botaoCancela.setObjectName("botaoCancela")
        self.botaoMais = QtWidgets.QPushButton(Form)
        self.botaoMais.setGeometry(QtCore.QRect(230, 42, 25, 25))
        self.botaoMais.setMinimumSize(QtCore.QSize(25, 25))
        self.botaoMais.setMaximumSize(QtCore.QSize(20, 20))
        self.botaoMais.setObjectName("botaoMais")
        self.lista = QtWidgets.QLabel(Form)
        self.lista.setGeometry(QtCore.QRect(20, 5, 201, 20))
        self.lista.setText("")
        self.lista.setObjectName("lista")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Nova Categoria"))
        self.labelNome.setText(_translate("Form", "Nome"))
        self.botaoOk.setText(_translate("Form", "Ok"))
        self.botaoCancela.setText(_translate("Form", "Cancela"))
        self.botaoMais.setText(_translate("Form", "+"))

