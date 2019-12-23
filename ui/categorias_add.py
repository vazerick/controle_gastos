# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'categorias_add.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(230, 92)
        Form.setMinimumSize(QtCore.QSize(0, 0))
        Form.setMaximumSize(QtCore.QSize(1666666, 16966))
        Form.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelNome = QtWidgets.QLabel(Form)
        self.labelNome.setObjectName("labelNome")
        self.horizontalLayout.addWidget(self.labelNome)
        self.inputNome = QtWidgets.QLineEdit(Form)
        self.inputNome.setObjectName("inputNome")
        self.horizontalLayout.addWidget(self.inputNome)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout.addWidget(self.checkBox)
        self.buttonBox = QtWidgets.QDialogButtonBox(Form)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Nova Categoria"))
        self.labelNome.setText(_translate("Form", "Nome"))
        self.checkBox.setText(_translate("Form", "Adicionar subcategorias"))

