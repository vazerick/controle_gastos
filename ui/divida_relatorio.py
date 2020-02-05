# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'divida_relatorio.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(690, 580)
        Form.setMinimumSize(QtCore.QSize(690, 330))
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.treeDividas = QtWidgets.QTreeWidget(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeDividas.sizePolicy().hasHeightForWidth())
        self.treeDividas.setSizePolicy(sizePolicy)
        self.treeDividas.setMinimumSize(QtCore.QSize(300, 0))
        self.treeDividas.setAlternatingRowColors(True)
        self.treeDividas.setRootIsDecorated(True)
        self.treeDividas.setUniformRowHeights(False)
        self.treeDividas.setItemsExpandable(False)
        self.treeDividas.setWordWrap(True)
        self.treeDividas.setHeaderHidden(True)
        self.treeDividas.setObjectName("treeDividas")
        self.treeDividas.header().setVisible(False)
        self.treeDividas.header().setCascadingSectionResizes(False)
        self.treeDividas.header().setHighlightSections(False)
        self.verticalLayout.addWidget(self.treeDividas)
        self.buttonBox = QtWidgets.QDialogButtonBox(Form)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Adicionar Gasto"))
        self.treeDividas.setSortingEnabled(True)
        self.treeDividas.headerItem().setText(0, _translate("Form", "Movimento"))
        self.treeDividas.headerItem().setText(1, _translate("Form", "Pessoa"))
        self.treeDividas.headerItem().setText(2, _translate("Form", "Data"))
        self.treeDividas.headerItem().setText(3, _translate("Form", "Item"))
        self.treeDividas.headerItem().setText(4, _translate("Form", "Valor"))
        self.treeDividas.headerItem().setText(5, _translate("Form", "Comentário"))

