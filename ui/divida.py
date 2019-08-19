# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'divida.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(350, 218)
        Form.setMinimumSize(QtCore.QSize(350, 0))
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout.addWidget(self.radioButton_2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelReserva = QtWidgets.QLabel(Form)
        self.labelReserva.setMinimumSize(QtCore.QSize(51, 17))
        self.labelReserva.setMaximumSize(QtCore.QSize(51, 17))
        self.labelReserva.setObjectName("labelReserva")
        self.horizontalLayout_2.addWidget(self.labelReserva)
        self.inputReserva = QtWidgets.QLineEdit(Form)
        self.inputReserva.setObjectName("inputReserva")
        self.horizontalLayout_2.addWidget(self.inputReserva)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labelReserva_2 = QtWidgets.QLabel(Form)
        self.labelReserva_2.setMinimumSize(QtCore.QSize(51, 17))
        self.labelReserva_2.setMaximumSize(QtCore.QSize(51, 17))
        self.labelReserva_2.setObjectName("labelReserva_2")
        self.horizontalLayout_3.addWidget(self.labelReserva_2)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setMinimumSize(QtCore.QSize(130, 0))
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_3.addWidget(self.comboBox)
        self.labelValor = QtWidgets.QLabel(Form)
        self.labelValor.setObjectName("labelValor")
        self.horizontalLayout_3.addWidget(self.labelValor)
        self.labelValor_2 = QtWidgets.QLabel(Form)
        self.labelValor_2.setObjectName("labelValor_2")
        self.horizontalLayout_3.addWidget(self.labelValor_2)
        self.spinValor = QtWidgets.QDoubleSpinBox(Form)
        self.spinValor.setDecimals(2)
        self.spinValor.setMaximum(99999.99)
        self.spinValor.setProperty("value", 0.0)
        self.spinValor.setObjectName("spinValor")
        self.horizontalLayout_3.addWidget(self.spinValor)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.labelComentario = QtWidgets.QLabel(Form)
        self.labelComentario.setObjectName("labelComentario")
        self.verticalLayout.addWidget(self.labelComentario)
        self.textComentario = QtWidgets.QTextEdit(Form)
        self.textComentario.setObjectName("textComentario")
        self.verticalLayout.addWidget(self.textComentario)
        self.buttonBox = QtWidgets.QDialogButtonBox(Form)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.inputReserva, self.spinValor)
        Form.setTabOrder(self.spinValor, self.textComentario)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Dívida"))
        self.radioButton.setText(_translate("Form", "Eu devo..."))
        self.radioButton_2.setText(_translate("Form", "Me devem..."))
        self.labelReserva.setText(_translate("Form", "Motivo"))
        self.labelReserva_2.setText(_translate("Form", "Pessoa"))
        self.labelValor.setText(_translate("Form", "Valor"))
        self.labelValor_2.setText(_translate("Form", "R$"))
        self.labelComentario.setText(_translate("Form", "Comentário"))

