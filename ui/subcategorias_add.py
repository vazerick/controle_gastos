# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'subcategorias_add.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(260, 200)
        Form.setMinimumSize(QtCore.QSize(260, 200))
        Form.setMaximumSize(QtCore.QSize(260, 250))
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
        self.botaoMais = QtWidgets.QPushButton(Form)
        self.botaoMais.setMinimumSize(QtCore.QSize(25, 25))
        self.botaoMais.setMaximumSize(QtCore.QSize(20, 20))
        self.botaoMais.setObjectName("botaoMais")
        self.horizontalLayout.addWidget(self.botaoMais)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.listWidget = QtWidgets.QListWidget(Form)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.labelCategoria = QtWidgets.QLabel(Form)
        self.labelCategoria.setObjectName("labelCategoria")
        self.verticalLayout.addWidget(self.labelCategoria)
        self.comboCat = QtWidgets.QComboBox(Form)
        self.comboCat.setObjectName("comboCat")
        self.verticalLayout.addWidget(self.comboCat)
        self.buttonBox = QtWidgets.QDialogButtonBox(Form)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Nova Sub-Categoria"))
        self.labelNome.setText(_translate("Form", "Nome"))
        self.botaoMais.setText(_translate("Form", "+"))
        self.labelCategoria.setText(_translate("Form", "Categoria"))

