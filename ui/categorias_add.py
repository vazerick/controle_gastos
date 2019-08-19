# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'categorias_add.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(230, 190)
        Form.setMinimumSize(QtCore.QSize(230, 170))
        Form.setMaximumSize(QtCore.QSize(1666666, 16966))
        Form.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.inputNome = QtWidgets.QLineEdit(Form)
        self.inputNome.setGeometry(QtCore.QRect(10, 30, 211, 25))
        self.inputNome.setObjectName("inputNome")
        self.labelNome = QtWidgets.QLabel(Form)
        self.labelNome.setGeometry(QtCore.QRect(20, 10, 54, 17))
        self.labelNome.setObjectName("labelNome")
        self.labelAntes = QtWidgets.QLabel(Form)
        self.labelAntes.setGeometry(QtCore.QRect(20, 60, 151, 17))
        self.labelAntes.setObjectName("labelAntes")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(10, 80, 211, 25))
        self.comboBox.setObjectName("comboBox")
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(30, 110, 171, 23))
        self.checkBox.setObjectName("checkBox")
        self.buttonBox = QtWidgets.QDialogButtonBox(Form)
        self.buttonBox.setGeometry(QtCore.QRect(5, 160, 221, 23))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Nova Categoria"))
        self.labelNome.setText(_translate("Form", "Nome"))
        self.labelAntes.setText(_translate("Form", "Adicionar antes de"))
        self.checkBox.setText(_translate("Form", "Adicionar subcategorias"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

