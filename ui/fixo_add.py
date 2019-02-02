# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fixo_add.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(718, 560)
        Form.setMinimumSize(QtCore.QSize(718, 486))
        Form.setMaximumSize(QtCore.QSize(718, 560))
        self.calendarWidget = QtWidgets.QCalendarWidget(Form)
        self.calendarWidget.setGeometry(QtCore.QRect(20, 160, 311, 181))
        self.calendarWidget.setGridVisible(False)
        self.calendarWidget.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.ShortDayNames)
        self.calendarWidget.setNavigationBarVisible(True)
        self.calendarWidget.setDateEditEnabled(True)
        self.calendarWidget.setObjectName("calendarWidget")
        self.labelGasto = QtWidgets.QLabel(Form)
        self.labelGasto.setGeometry(QtCore.QRect(30, 10, 61, 17))
        self.labelGasto.setObjectName("labelGasto")
        self.inputGasto = QtWidgets.QLineEdit(Form)
        self.inputGasto.setGeometry(QtCore.QRect(30, 30, 321, 25))
        self.inputGasto.setObjectName("inputGasto")
        self.textComentario = QtWidgets.QTextEdit(Form)
        self.textComentario.setGeometry(QtCore.QRect(20, 390, 681, 111))
        self.textComentario.setObjectName("textComentario")
        self.labelComentario = QtWidgets.QLabel(Form)
        self.labelComentario.setGeometry(QtCore.QRect(20, 360, 81, 17))
        self.labelComentario.setObjectName("labelComentario")
        self.labelValor = QtWidgets.QLabel(Form)
        self.labelValor.setGeometry(QtCore.QRect(380, 10, 41, 17))
        self.labelValor.setObjectName("labelValor")
        self.labelPrevisao = QtWidgets.QLabel(Form)
        self.labelPrevisao.setGeometry(QtCore.QRect(40, 130, 71, 17))
        self.labelPrevisao.setObjectName("labelPrevisao")
        self.botaoHoje = QtWidgets.QPushButton(Form)
        self.botaoHoje.setGeometry(QtCore.QRect(290, 130, 41, 25))
        self.botaoHoje.setObjectName("botaoHoje")
        self.botaoOk = QtWidgets.QPushButton(Form)
        self.botaoOk.setGeometry(QtCore.QRect(230, 520, 80, 25))
        self.botaoOk.setObjectName("botaoOk")
        self.botaoCancela = QtWidgets.QPushButton(Form)
        self.botaoCancela.setGeometry(QtCore.QRect(390, 520, 80, 25))
        self.botaoCancela.setObjectName("botaoCancela")
        self.spinValor = QtWidgets.QDoubleSpinBox(Form)
        self.spinValor.setGeometry(QtCore.QRect(395, 30, 71, 26))
        self.spinValor.setDecimals(2)
        self.spinValor.setMaximum(99999.99)
        self.spinValor.setProperty("value", 0.0)
        self.spinValor.setObjectName("spinValor")
        self.labelValor_2 = QtWidgets.QLabel(Form)
        self.labelValor_2.setGeometry(QtCore.QRect(380, 35, 16, 17))
        self.labelValor_2.setObjectName("labelValor_2")
        self.botaoHoje_2 = QtWidgets.QPushButton(Form)
        self.botaoHoje_2.setEnabled(False)
        self.botaoHoje_2.setGeometry(QtCore.QRect(660, 130, 41, 25))
        self.botaoHoje_2.setObjectName("botaoHoje_2")
        self.labelPago = QtWidgets.QLabel(Form)
        self.labelPago.setEnabled(False)
        self.labelPago.setGeometry(QtCore.QRect(410, 130, 71, 17))
        self.labelPago.setObjectName("labelPago")
        self.calendarWidget_2 = QtWidgets.QCalendarWidget(Form)
        self.calendarWidget_2.setEnabled(False)
        self.calendarWidget_2.setGeometry(QtCore.QRect(390, 160, 311, 181))
        self.calendarWidget_2.setFirstDayOfWeek(QtCore.Qt.Sunday)
        self.calendarWidget_2.setGridVisible(False)
        self.calendarWidget_2.setHorizontalHeaderFormat(QtWidgets.QCalendarWidget.ShortDayNames)
        self.calendarWidget_2.setNavigationBarVisible(True)
        self.calendarWidget_2.setDateEditEnabled(True)
        self.calendarWidget_2.setObjectName("calendarWidget_2")
        self.checkPago = QtWidgets.QCheckBox(Form)
        self.checkPago.setGeometry(QtCore.QRect(490, 30, 82, 23))
        self.checkPago.setObjectName("checkPago")
        self.comboSub = QtWidgets.QComboBox(Form)
        self.comboSub.setGeometry(QtCore.QRect(410, 90, 171, 25))
        self.comboSub.setObjectName("comboSub")
        self.labelSub = QtWidgets.QLabel(Form)
        self.labelSub.setGeometry(QtCore.QRect(410, 70, 91, 17))
        self.labelSub.setObjectName("labelSub")
        self.labelCategoria = QtWidgets.QLabel(Form)
        self.labelCategoria.setGeometry(QtCore.QRect(210, 70, 71, 17))
        self.labelCategoria.setObjectName("labelCategoria")
        self.comboCategoria = QtWidgets.QComboBox(Form)
        self.comboCategoria.setGeometry(QtCore.QRect(210, 90, 171, 25))
        self.comboCategoria.setObjectName("comboCategoria")
        self.comboPagamento = QtWidgets.QComboBox(Form)
        self.comboPagamento.setEnabled(False)
        self.comboPagamento.setGeometry(QtCore.QRect(30, 90, 151, 25))
        self.comboPagamento.setObjectName("comboPagamento")
        self.labelPagamento = QtWidgets.QLabel(Form)
        self.labelPagamento.setEnabled(False)
        self.labelPagamento.setGeometry(QtCore.QRect(30, 70, 151, 17))
        self.labelPagamento.setObjectName("labelPagamento")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.inputGasto, self.spinValor)
        Form.setTabOrder(self.spinValor, self.textComentario)
        Form.setTabOrder(self.textComentario, self.calendarWidget)
        Form.setTabOrder(self.calendarWidget, self.botaoHoje)
        Form.setTabOrder(self.botaoHoje, self.botaoOk)
        Form.setTabOrder(self.botaoOk, self.botaoCancela)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Adicionar Gasto"))
        self.labelGasto.setText(_translate("Form", "Saída"))
        self.labelComentario.setText(_translate("Form", "Comentário"))
        self.labelValor.setText(_translate("Form", "Valor"))
        self.labelPrevisao.setText(_translate("Form", "Vencimento"))
        self.botaoHoje.setText(_translate("Form", "Hoje"))
        self.botaoOk.setText(_translate("Form", "Ok"))
        self.botaoCancela.setText(_translate("Form", "Cancela"))
        self.labelValor_2.setText(_translate("Form", "R$"))
        self.botaoHoje_2.setText(_translate("Form", "Hoje"))
        self.labelPago.setText(_translate("Form", "Pago"))
        self.checkPago.setText(_translate("Form", "Pago"))
        self.labelSub.setText(_translate("Form", "Sub-categoria"))
        self.labelCategoria.setText(_translate("Form", "Categoria"))
        self.labelPagamento.setText(_translate("Form", "Forma de pagamento"))

