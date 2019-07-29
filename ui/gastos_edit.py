# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gastos_edit.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(584, 411)
        self.calendarWidget = QtWidgets.QCalendarWidget(Form)
        self.calendarWidget.setGeometry(QtCore.QRect(40, 170, 311, 181))
        self.calendarWidget.setGridVisible(False)
        self.calendarWidget.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.ShortDayNames)
        self.calendarWidget.setNavigationBarVisible(True)
        self.calendarWidget.setDateEditEnabled(True)
        self.calendarWidget.setObjectName("calendarWidget")
        self.labelGasto = QtWidgets.QLabel(Form)
        self.labelGasto.setGeometry(QtCore.QRect(20, 10, 41, 17))
        self.labelGasto.setObjectName("labelGasto")
        self.inputGasto = QtWidgets.QLineEdit(Form)
        self.inputGasto.setGeometry(QtCore.QRect(20, 30, 441, 25))
        self.inputGasto.setObjectName("inputGasto")
        self.textComentario = QtWidgets.QTextEdit(Form)
        self.textComentario.setGeometry(QtCore.QRect(370, 170, 191, 181))
        self.textComentario.setObjectName("textComentario")
        self.labelComentario = QtWidgets.QLabel(Form)
        self.labelComentario.setGeometry(QtCore.QRect(370, 150, 81, 17))
        self.labelComentario.setObjectName("labelComentario")
        self.labelValor = QtWidgets.QLabel(Form)
        self.labelValor.setGeometry(QtCore.QRect(480, 10, 41, 17))
        self.labelValor.setObjectName("labelValor")
        self.labelCategoria = QtWidgets.QLabel(Form)
        self.labelCategoria.setGeometry(QtCore.QRect(20, 70, 71, 17))
        self.labelCategoria.setObjectName("labelCategoria")
        self.comboCategoria = QtWidgets.QComboBox(Form)
        self.comboCategoria.setGeometry(QtCore.QRect(20, 90, 171, 25))
        self.comboCategoria.setObjectName("comboCategoria")
        self.labelSub = QtWidgets.QLabel(Form)
        self.labelSub.setGeometry(QtCore.QRect(220, 70, 91, 17))
        self.labelSub.setObjectName("labelSub")
        self.comboSub = QtWidgets.QComboBox(Form)
        self.comboSub.setGeometry(QtCore.QRect(220, 90, 171, 25))
        self.comboSub.setObjectName("comboSub")
        self.labelData = QtWidgets.QLabel(Form)
        self.labelData.setGeometry(QtCore.QRect(40, 150, 71, 17))
        self.labelData.setObjectName("labelData")
        self.botaoHoje = QtWidgets.QPushButton(Form)
        self.botaoHoje.setGeometry(QtCore.QRect(310, 140, 41, 25))
        self.botaoHoje.setObjectName("botaoHoje")
        self.spinValor = QtWidgets.QDoubleSpinBox(Form)
        self.spinValor.setGeometry(QtCore.QRect(495, 30, 71, 26))
        self.spinValor.setDecimals(2)
        self.spinValor.setMaximum(99999.99)
        self.spinValor.setProperty("value", 0.0)
        self.spinValor.setObjectName("spinValor")
        self.labelValor_2 = QtWidgets.QLabel(Form)
        self.labelValor_2.setGeometry(QtCore.QRect(480, 35, 16, 17))
        self.labelValor_2.setObjectName("labelValor_2")
        self.checkDivida = QtWidgets.QCheckBox(Form)
        self.checkDivida.setGeometry(QtCore.QRect(460, 90, 82, 23))
        self.checkDivida.setObjectName("checkDivida")
        self.buttonBox = QtWidgets.QDialogButtonBox(Form)
        self.buttonBox.setGeometry(QtCore.QRect(5, 370, 581, 23))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.inputGasto, self.spinValor)
        Form.setTabOrder(self.spinValor, self.comboCategoria)
        Form.setTabOrder(self.comboCategoria, self.comboSub)
        Form.setTabOrder(self.comboSub, self.textComentario)
        Form.setTabOrder(self.textComentario, self.calendarWidget)
        Form.setTabOrder(self.calendarWidget, self.botaoHoje)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Adicionar Gasto"))
        self.labelGasto.setText(_translate("Form", "Gasto"))
        self.labelGasto.setProperty("class", _translate("Form", "obrigatorio"))
        self.labelComentario.setText(_translate("Form", "Comentário"))
        self.labelValor.setText(_translate("Form", "Valor"))
        self.labelCategoria.setText(_translate("Form", "Categoria"))
        self.labelSub.setText(_translate("Form", "Sub-categoria"))
        self.labelData.setText(_translate("Form", "Data"))
        self.botaoHoje.setText(_translate("Form", "Hoje"))
        self.labelValor_2.setText(_translate("Form", "R$"))
        self.checkDivida.setText(_translate("Form", "Dívida"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
