# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'categorias_edit.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(230, 200)
        Form.setMinimumSize(QtCore.QSize(230, 200))
        Form.setMaximumSize(QtCore.QSize(230, 200))
        Form.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.inputNome = QtWidgets.QLineEdit(Form)
        self.inputNome.setGeometry(QtCore.QRect(10, 60, 211, 25))
        self.inputNome.setObjectName("inputNome")
        self.labelNome = QtWidgets.QLabel(Form)
        self.labelNome.setGeometry(QtCore.QRect(20, 40, 54, 17))
        self.labelNome.setObjectName("labelNome")
        self.labelAntes = QtWidgets.QLabel(Form)
        self.labelAntes.setGeometry(QtCore.QRect(20, 90, 151, 17))
        self.labelAntes.setObjectName("labelAntes")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(10, 110, 211, 25))
        self.comboBox.setObjectName("comboBox")
        self.labelTitulo = QtWidgets.QLabel(Form)
        self.labelTitulo.setGeometry(QtCore.QRect(20, 20, 191, 17))
        self.labelTitulo.setAlignment(QtCore.Qt.AlignCenter)
        self.labelTitulo.setObjectName("labelTitulo")
        self.buttonBox = QtWidgets.QDialogButtonBox(Form)
        self.buttonBox.setGeometry(QtCore.QRect(0, 160, 231, 23))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Editar Categoria"))
        self.labelNome.setText(_translate("Form", "Nome"))
        self.labelAntes.setText(_translate("Form", "Adicionar antes de"))
        self.labelTitulo.setText(_translate("Form", "Editar [nome]"))

