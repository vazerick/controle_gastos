# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ajustar.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(202, 101)
        Form.setMinimumSize(QtCore.QSize(0, 0))
        Form.setMaximumSize(QtCore.QSize(1666666, 16966))
        Form.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelAjuste = QtWidgets.QLabel(Form)
        self.labelAjuste.setObjectName("labelAjuste")
        self.horizontalLayout.addWidget(self.labelAjuste)
        self.spinAjuste = QtWidgets.QDoubleSpinBox(Form)
        self.spinAjuste.setMinimum(-9999999.0)
        self.spinAjuste.setMaximum(9999999.99)
        self.spinAjuste.setObjectName("spinAjuste")
        self.horizontalLayout.addWidget(self.spinAjuste)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.labelHistorico = QtWidgets.QLabel(Form)
        self.labelHistorico.setObjectName("labelHistorico")
        self.horizontalLayout_2.addWidget(self.labelHistorico)
        self.spinHistorico = QtWidgets.QDoubleSpinBox(Form)
        self.spinHistorico.setMaximum(99999.99)
        self.spinHistorico.setObjectName("spinHistorico")
        self.horizontalLayout_2.addWidget(self.spinHistorico)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        spacerItem1 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.buttonBox = QtWidgets.QDialogButtonBox(Form)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_2.addWidget(self.buttonBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Ajustes"))
        self.labelAjuste.setText(_translate("Form", "Ajuste de erro: R$"))
        self.labelHistorico.setText(_translate("Form", "Uso de Reserva: R$"))

