# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'investimento.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(350, 165)
        Form.setMinimumSize(QtCore.QSize(300, 165))
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.labelReserva = QtWidgets.QLabel(Form)
        self.labelReserva.setMinimumSize(QtCore.QSize(51, 17))
        self.labelReserva.setMaximumSize(QtCore.QSize(51, 17))
        self.labelReserva.setObjectName("labelReserva")
        self.horizontalLayout.addWidget(self.labelReserva)
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
        Form.setTabOrder(self.inputGasto, self.spinValor)
        Form.setTabOrder(self.spinValor, self.textComentario)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Investimento"))
        self.labelReserva.setText(_translate("Form", "Nome"))
        self.labelValor.setText(_translate("Form", "Valor"))
        self.labelValor_2.setText(_translate("Form", "R$"))
        self.labelComentario.setText(_translate("Form", "Comentário"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

