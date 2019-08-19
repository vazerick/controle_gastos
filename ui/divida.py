# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'divida.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(291, 270)
        self.labelReserva = QtWidgets.QLabel(Form)
        self.labelReserva.setGeometry(QtCore.QRect(10, 30, 51, 17))
        self.labelReserva.setMinimumSize(QtCore.QSize(51, 17))
        self.labelReserva.setMaximumSize(QtCore.QSize(51, 17))
        self.labelReserva.setObjectName("labelReserva")
        self.inputReserva = QtWidgets.QLineEdit(Form)
        self.inputReserva.setGeometry(QtCore.QRect(10, 50, 271, 25))
        self.inputReserva.setObjectName("inputReserva")
        self.textComentario = QtWidgets.QTextEdit(Form)
        self.textComentario.setGeometry(QtCore.QRect(10, 160, 271, 71))
        self.textComentario.setObjectName("textComentario")
        self.labelComentario = QtWidgets.QLabel(Form)
        self.labelComentario.setGeometry(QtCore.QRect(10, 130, 81, 17))
        self.labelComentario.setObjectName("labelComentario")
        self.labelValor = QtWidgets.QLabel(Form)
        self.labelValor.setGeometry(QtCore.QRect(190, 80, 41, 17))
        self.labelValor.setObjectName("labelValor")
        self.spinValor = QtWidgets.QDoubleSpinBox(Form)
        self.spinValor.setGeometry(QtCore.QRect(205, 100, 71, 26))
        self.spinValor.setDecimals(2)
        self.spinValor.setMaximum(99999.99)
        self.spinValor.setProperty("value", 0.0)
        self.spinValor.setObjectName("spinValor")
        self.labelValor_2 = QtWidgets.QLabel(Form)
        self.labelValor_2.setGeometry(QtCore.QRect(190, 105, 16, 17))
        self.labelValor_2.setObjectName("labelValor_2")
        self.buttonBox = QtWidgets.QDialogButtonBox(Form)
        self.buttonBox.setGeometry(QtCore.QRect(0, 240, 291, 23))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(40, 10, 82, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(150, 10, 91, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.labelReserva_2 = QtWidgets.QLabel(Form)
        self.labelReserva_2.setGeometry(QtCore.QRect(10, 80, 51, 17))
        self.labelReserva_2.setMinimumSize(QtCore.QSize(51, 17))
        self.labelReserva_2.setMaximumSize(QtCore.QSize(51, 17))
        self.labelReserva_2.setObjectName("labelReserva_2")
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(10, 100, 151, 22))
        self.comboBox.setObjectName("comboBox")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.inputReserva, self.spinValor)
        Form.setTabOrder(self.spinValor, self.textComentario)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Dívida"))
        self.labelReserva.setText(_translate("Form", "Motivo"))
        self.labelComentario.setText(_translate("Form", "Comentário"))
        self.labelValor.setText(_translate("Form", "Valor"))
        self.labelValor_2.setText(_translate("Form", "R$"))
        self.radioButton.setText(_translate("Form", "Eu devo..."))
        self.radioButton_2.setText(_translate("Form", "Me devem..."))
        self.labelReserva_2.setText(_translate("Form", "Pessoa"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

