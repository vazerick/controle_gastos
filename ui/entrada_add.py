# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'entrada_add.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(718, 486)
        Form.setMinimumSize(QtCore.QSize(718, 486))
        Form.setMaximumSize(QtCore.QSize(718, 486))
        self.calendarWidget = QtWidgets.QCalendarWidget(Form)
        self.calendarWidget.setGeometry(QtCore.QRect(20, 100, 311, 181))
        self.calendarWidget.setGridVisible(False)
        self.calendarWidget.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.ShortDayNames)
        self.calendarWidget.setNavigationBarVisible(True)
        self.calendarWidget.setDateEditEnabled(True)
        self.calendarWidget.setObjectName("calendarWidget")
        self.labelEntrada = QtWidgets.QLabel(Form)
        self.labelEntrada.setGeometry(QtCore.QRect(20, 10, 61, 17))
        self.labelEntrada.setObjectName("labelEntrada")
        self.inputEntrada = QtWidgets.QLineEdit(Form)
        self.inputEntrada.setGeometry(QtCore.QRect(20, 30, 321, 25))
        self.inputEntrada.setObjectName("inputEntrada")
        self.textComentario = QtWidgets.QTextEdit(Form)
        self.textComentario.setGeometry(QtCore.QRect(20, 320, 681, 111))
        self.textComentario.setObjectName("textComentario")
        self.labelComentario = QtWidgets.QLabel(Form)
        self.labelComentario.setGeometry(QtCore.QRect(20, 290, 81, 17))
        self.labelComentario.setObjectName("labelComentario")
        self.labelValor = QtWidgets.QLabel(Form)
        self.labelValor.setGeometry(QtCore.QRect(370, 10, 41, 17))
        self.labelValor.setObjectName("labelValor")
        self.labelPrevisao = QtWidgets.QLabel(Form)
        self.labelPrevisao.setGeometry(QtCore.QRect(40, 70, 71, 17))
        self.labelPrevisao.setObjectName("labelPrevisao")
        self.botaoHoje = QtWidgets.QPushButton(Form)
        self.botaoHoje.setGeometry(QtCore.QRect(290, 70, 41, 25))
        self.botaoHoje.setObjectName("botaoHoje")
        self.spinValor = QtWidgets.QDoubleSpinBox(Form)
        self.spinValor.setGeometry(QtCore.QRect(385, 30, 71, 26))
        self.spinValor.setDecimals(2)
        self.spinValor.setMaximum(99999.99)
        self.spinValor.setProperty("value", 0.0)
        self.spinValor.setObjectName("spinValor")
        self.labelValor_2 = QtWidgets.QLabel(Form)
        self.labelValor_2.setGeometry(QtCore.QRect(370, 35, 16, 17))
        self.labelValor_2.setObjectName("labelValor_2")
        self.botaoHoje_2 = QtWidgets.QPushButton(Form)
        self.botaoHoje_2.setEnabled(False)
        self.botaoHoje_2.setGeometry(QtCore.QRect(660, 70, 41, 25))
        self.botaoHoje_2.setObjectName("botaoHoje_2")
        self.labelPago = QtWidgets.QLabel(Form)
        self.labelPago.setEnabled(False)
        self.labelPago.setGeometry(QtCore.QRect(410, 70, 71, 17))
        self.labelPago.setObjectName("labelPago")
        self.calendarWidget_2 = QtWidgets.QCalendarWidget(Form)
        self.calendarWidget_2.setEnabled(False)
        self.calendarWidget_2.setGeometry(QtCore.QRect(390, 100, 311, 181))
        self.calendarWidget_2.setFirstDayOfWeek(QtCore.Qt.Sunday)
        self.calendarWidget_2.setGridVisible(False)
        self.calendarWidget_2.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.ShortDayNames)
        self.calendarWidget_2.setNavigationBarVisible(True)
        self.calendarWidget_2.setDateEditEnabled(True)
        self.calendarWidget_2.setObjectName("calendarWidget_2")
        self.checkPago = QtWidgets.QCheckBox(Form)
        self.checkPago.setGeometry(QtCore.QRect(480, 30, 82, 23))
        self.checkPago.setObjectName("checkPago")
        self.buttonBox = QtWidgets.QDialogButtonBox(Form)
        self.buttonBox.setGeometry(QtCore.QRect(0, 450, 721, 23))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.inputEntrada, self.spinValor)
        Form.setTabOrder(self.spinValor, self.textComentario)
        Form.setTabOrder(self.textComentario, self.calendarWidget)
        Form.setTabOrder(self.calendarWidget, self.botaoHoje)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Adicionar Gasto"))
        self.labelEntrada.setText(_translate("Form", "Entrada"))
        self.labelComentario.setText(_translate("Form", "Comentário"))
        self.labelValor.setText(_translate("Form", "Valor"))
        self.labelPrevisao.setText(_translate("Form", "Previsão"))
        self.botaoHoje.setText(_translate("Form", "Hoje"))
        self.labelValor_2.setText(_translate("Form", "R$"))
        self.botaoHoje_2.setText(_translate("Form", "Hoje"))
        self.labelPago.setText(_translate("Form", "Pago"))
        self.checkPago.setText(_translate("Form", "Pago"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

