# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reserva_edit.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(572, 228)
        self.labelReserva = QtWidgets.QLabel(Form)
        self.labelReserva.setGeometry(QtCore.QRect(20, 10, 51, 17))
        self.labelReserva.setMinimumSize(QtCore.QSize(51, 17))
        self.labelReserva.setMaximumSize(QtCore.QSize(51, 17))
        self.labelReserva.setObjectName("labelReserva")
        self.inputReserva = QtWidgets.QLineEdit(Form)
        self.inputReserva.setGeometry(QtCore.QRect(20, 30, 321, 25))
        self.inputReserva.setObjectName("inputReserva")
        self.textComentario = QtWidgets.QTextEdit(Form)
        self.textComentario.setGeometry(QtCore.QRect(20, 100, 541, 71))
        self.textComentario.setObjectName("textComentario")
        self.labelComentario = QtWidgets.QLabel(Form)
        self.labelComentario.setGeometry(QtCore.QRect(20, 70, 81, 17))
        self.labelComentario.setObjectName("labelComentario")
        self.labelValor = QtWidgets.QLabel(Form)
        self.labelValor.setGeometry(QtCore.QRect(370, 10, 41, 17))
        self.labelValor.setObjectName("labelValor")
        self.spinValor = QtWidgets.QDoubleSpinBox(Form)
        self.spinValor.setGeometry(QtCore.QRect(385, 30, 71, 26))
        self.spinValor.setDecimals(2)
        self.spinValor.setMaximum(99999.99)
        self.spinValor.setProperty("value", 0.0)
        self.spinValor.setObjectName("spinValor")
        self.labelValor_2 = QtWidgets.QLabel(Form)
        self.labelValor_2.setGeometry(QtCore.QRect(370, 35, 16, 17))
        self.labelValor_2.setObjectName("labelValor_2")
        self.buttonBox = QtWidgets.QDialogButtonBox(Form)
        self.buttonBox.setGeometry(QtCore.QRect(10, 190, 551, 23))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(470, 10, 91, 81))
        self.groupBox.setObjectName("groupBox")
        self.buttonGasto = QtWidgets.QPushButton(self.groupBox)
        self.buttonGasto.setGeometry(QtCore.QRect(10, 20, 75, 23))
        self.buttonGasto.setObjectName("buttonGasto")
        self.buttonFixo = QtWidgets.QPushButton(self.groupBox)
        self.buttonFixo.setGeometry(QtCore.QRect(10, 50, 75, 23))
        self.buttonFixo.setObjectName("buttonFixo")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.inputReserva, self.spinValor)
        Form.setTabOrder(self.spinValor, self.textComentario)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Adicionar Gasto"))
        self.labelReserva.setText(_translate("Form", "Reserva"))
        self.labelComentario.setText(_translate("Form", "Comentário"))
        self.labelValor.setText(_translate("Form", "Valor"))
        self.labelValor_2.setText(_translate("Form", "R$"))
        self.groupBox.setTitle(_translate("Form", "Converter"))
        self.buttonGasto.setText(_translate("Form", "Gasto"))
        self.buttonFixo.setText(_translate("Form", "Fixo"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

