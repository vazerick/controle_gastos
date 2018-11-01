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
        Form.resize(260, 250)
        Form.setMinimumSize(QtCore.QSize(260, 200))
        Form.setMaximumSize(QtCore.QSize(260, 250))
        Form.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.inputNome = QtWidgets.QLineEdit(Form)
        self.inputNome.setGeometry(QtCore.QRect(10, 22, 211, 25))
        self.inputNome.setObjectName("inputNome")
        self.labelNome = QtWidgets.QLabel(Form)
        self.labelNome.setGeometry(QtCore.QRect(20, 2, 54, 17))
        self.labelNome.setObjectName("labelNome")
        self.botaoOk = QtWidgets.QPushButton(Form)
        self.botaoOk.setGeometry(QtCore.QRect(40, 210, 80, 25))
        self.botaoOk.setObjectName("botaoOk")
        self.botaoCancela = QtWidgets.QPushButton(Form)
        self.botaoCancela.setGeometry(QtCore.QRect(150, 210, 80, 25))
        self.botaoCancela.setObjectName("botaoCancela")
        self.botaoMais = QtWidgets.QPushButton(Form)
        self.botaoMais.setGeometry(QtCore.QRect(230, 22, 25, 25))
        self.botaoMais.setMinimumSize(QtCore.QSize(25, 25))
        self.botaoMais.setMaximumSize(QtCore.QSize(20, 20))
        self.botaoMais.setObjectName("botaoMais")
        self.comboSub = QtWidgets.QComboBox(Form)
        self.comboSub.setGeometry(QtCore.QRect(10, 170, 241, 25))
        self.comboSub.setObjectName("comboSub")
        self.labelAntes = QtWidgets.QLabel(Form)
        self.labelAntes.setGeometry(QtCore.QRect(20, 150, 111, 17))
        self.labelAntes.setObjectName("labelAntes")
        self.labelCategoria = QtWidgets.QLabel(Form)
        self.labelCategoria.setGeometry(QtCore.QRect(20, 100, 111, 17))
        self.labelCategoria.setObjectName("labelCategoria")
        self.comboCat = QtWidgets.QComboBox(Form)
        self.comboCat.setGeometry(QtCore.QRect(10, 120, 241, 25))
        self.comboCat.setObjectName("comboCat")
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setGeometry(QtCore.QRect(10, 60, 241, 31))
        self.listWidget.setObjectName("listWidget")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Nova Sub-Categoria"))
        self.labelNome.setText(_translate("Form", "Nome"))
        self.botaoOk.setText(_translate("Form", "Ok"))
        self.botaoCancela.setText(_translate("Form", "Cancela"))
        self.botaoMais.setText(_translate("Form", "+"))
        self.labelAntes.setText(_translate("Form", "Adicionar antes de"))
        self.labelCategoria.setText(_translate("Form", "Categoria"))

