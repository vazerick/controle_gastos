# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gastos_edit.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(350, 230)
        Form.setMinimumSize(QtCore.QSize(300, 230))
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelGasto = QtWidgets.QLabel(Form)
        self.labelGasto.setObjectName("labelGasto")
        self.horizontalLayout.addWidget(self.labelGasto)
        self.inputGasto = QtWidgets.QLineEdit(Form)
        self.inputGasto.setObjectName("inputGasto")
        self.horizontalLayout.addWidget(self.inputGasto)
        self.labelValor = QtWidgets.QLabel(Form)
        self.labelValor.setObjectName("labelValor")
        self.horizontalLayout.addWidget(self.labelValor)
        self.labelValor_2 = QtWidgets.QLabel(Form)
        self.labelValor_2.setObjectName("labelValor_2")
        self.horizontalLayout.addWidget(self.labelValor_2)
        self.spinValor = QtWidgets.QDoubleSpinBox(Form)
        self.spinValor.setDecimals(2)
        self.spinValor.setMaximum(99999.99)
        self.spinValor.setProperty("value", 0.0)
        self.spinValor.setObjectName("spinValor")
        self.horizontalLayout.addWidget(self.spinValor)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelCategoria = QtWidgets.QLabel(Form)
        self.labelCategoria.setObjectName("labelCategoria")
        self.horizontalLayout_2.addWidget(self.labelCategoria)
        self.comboCategoria = QtWidgets.QComboBox(Form)
        self.comboCategoria.setObjectName("comboCategoria")
        self.horizontalLayout_2.addWidget(self.comboCategoria)
        self.labelSub = QtWidgets.QLabel(Form)
        self.labelSub.setObjectName("labelSub")
        self.horizontalLayout_2.addWidget(self.labelSub)
        self.comboSub = QtWidgets.QComboBox(Form)
        self.comboSub.setObjectName("comboSub")
        self.horizontalLayout_2.addWidget(self.comboSub)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.labelData = QtWidgets.QLabel(Form)
        self.labelData.setObjectName("labelData")
        self.horizontalLayout_3.addWidget(self.labelData)
        self.dateEdit = QtWidgets.QDateEdit(Form)
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.setObjectName("dateEdit")
        self.horizontalLayout_3.addWidget(self.dateEdit)
        self.botaoHoje = QtWidgets.QPushButton(Form)
        self.botaoHoje.setObjectName("botaoHoje")
        self.horizontalLayout_3.addWidget(self.botaoHoje)
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
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.inputGasto, self.spinValor)
        Form.setTabOrder(self.spinValor, self.comboCategoria)
        Form.setTabOrder(self.comboCategoria, self.comboSub)
        Form.setTabOrder(self.comboSub, self.dateEdit)
        Form.setTabOrder(self.dateEdit, self.botaoHoje)
        Form.setTabOrder(self.botaoHoje, self.textComentario)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Editar Gasto"))
        self.labelGasto.setText(_translate("Form", "Gasto"))
        self.labelGasto.setProperty("class", _translate("Form", "obrigatorio"))
        self.labelValor.setText(_translate("Form", "Valor"))
        self.labelValor_2.setText(_translate("Form", "R$"))
        self.labelCategoria.setText(_translate("Form", "Categoria"))
        self.labelSub.setText(_translate("Form", "Sub-categoria"))
        self.labelData.setText(_translate("Form", "Data"))
        self.botaoHoje.setText(_translate("Form", "Hoje"))
        self.labelComentario.setText(_translate("Form", "Comentário"))

