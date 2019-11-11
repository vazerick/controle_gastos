# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'relatorio.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1300, 600)
        Form.setMinimumSize(QtCore.QSize(1300, 600))
        Form.setMaximumSize(QtCore.QSize(1500, 750))
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.radioTodos = QtWidgets.QRadioButton(Form)
        self.radioTodos.setChecked(True)
        self.radioTodos.setObjectName("radioTodos")
        self.horizontalLayout.addWidget(self.radioTodos)
        self.radioTotal = QtWidgets.QRadioButton(Form)
        self.radioTotal.setObjectName("radioTotal")
        self.horizontalLayout.addWidget(self.radioTotal)
        self.radioPercent = QtWidgets.QRadioButton(Form)
        self.radioPercent.setObjectName("radioPercent")
        self.horizontalLayout.addWidget(self.radioPercent)
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout.addWidget(self.radioButton)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.boxFiltro = QtWidgets.QFrame(Form)
        self.boxFiltro.setObjectName("boxFiltro")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.boxFiltro)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.checkRelSub = QtWidgets.QCheckBox(self.boxFiltro)
        self.checkRelSub.setObjectName("checkRelSub")
        self.gridLayout_3.addWidget(self.checkRelSub, 0, 3, 1, 1)
        self.checkRelFim = QtWidgets.QCheckBox(self.boxFiltro)
        self.checkRelFim.setObjectName("checkRelFim")
        self.gridLayout_3.addWidget(self.checkRelFim, 0, 5, 1, 1)
        self.comboCategoria = QtWidgets.QComboBox(self.boxFiltro)
        self.comboCategoria.setObjectName("comboCategoria")
        self.gridLayout_3.addWidget(self.comboCategoria, 1, 2, 1, 1)
        self.dateFim = QtWidgets.QDateEdit(self.boxFiltro)
        self.dateFim.setCalendarPopup(True)
        self.dateFim.setObjectName("dateFim")
        self.gridLayout_3.addWidget(self.dateFim, 1, 5, 1, 1)
        self.checkRelCat = QtWidgets.QCheckBox(self.boxFiltro)
        self.checkRelCat.setObjectName("checkRelCat")
        self.gridLayout_3.addWidget(self.checkRelCat, 0, 2, 1, 1)
        self.checkRelInicio = QtWidgets.QCheckBox(self.boxFiltro)
        self.checkRelInicio.setObjectName("checkRelInicio")
        self.gridLayout_3.addWidget(self.checkRelInicio, 0, 4, 1, 1)
        self.comboSub = QtWidgets.QComboBox(self.boxFiltro)
        self.comboSub.setObjectName("comboSub")
        self.gridLayout_3.addWidget(self.comboSub, 1, 3, 1, 1)
        self.inputFiltro = QtWidgets.QLineEdit(self.boxFiltro)
        self.inputFiltro.setObjectName("inputFiltro")
        self.gridLayout_3.addWidget(self.inputFiltro, 1, 1, 1, 1)
        self.dateInicio = QtWidgets.QDateEdit(self.boxFiltro)
        self.dateInicio.setCalendarPopup(True)
        self.dateInicio.setObjectName("dateInicio")
        self.gridLayout_3.addWidget(self.dateInicio, 1, 4, 1, 1)
        self.checkRelTipo = QtWidgets.QCheckBox(self.boxFiltro)
        self.checkRelTipo.setObjectName("checkRelTipo")
        self.gridLayout_3.addWidget(self.checkRelTipo, 0, 0, 1, 1)
        self.comboTipo = QtWidgets.QComboBox(self.boxFiltro)
        self.comboTipo.setObjectName("comboTipo")
        self.comboTipo.addItem("")
        self.comboTipo.addItem("")
        self.comboTipo.addItem("")
        self.comboTipo.addItem("")
        self.gridLayout_3.addWidget(self.comboTipo, 1, 0, 1, 1)
        self.checkRelNome = QtWidgets.QCheckBox(self.boxFiltro)
        self.checkRelNome.setObjectName("checkRelNome")
        self.gridLayout_3.addWidget(self.checkRelNome, 0, 1, 1, 1)
        self.botaoFiltro = QtWidgets.QPushButton(self.boxFiltro)
        self.botaoFiltro.setObjectName("botaoFiltro")
        self.gridLayout_3.addWidget(self.botaoFiltro, 1, 6, 1, 1)
        self.botaoLimpa = QtWidgets.QPushButton(self.boxFiltro)
        self.botaoLimpa.setObjectName("botaoLimpa")
        self.gridLayout_3.addWidget(self.botaoLimpa, 0, 6, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_3)
        self.treeFiltro = QtWidgets.QTreeWidget(self.boxFiltro)
        self.treeFiltro.setAlternatingRowColors(True)
        self.treeFiltro.setRootIsDecorated(True)
        self.treeFiltro.setUniformRowHeights(False)
        self.treeFiltro.setItemsExpandable(False)
        self.treeFiltro.setWordWrap(True)
        self.treeFiltro.setHeaderHidden(True)
        self.treeFiltro.setObjectName("treeFiltro")
        self.treeFiltro.header().setVisible(False)
        self.treeFiltro.header().setCascadingSectionResizes(False)
        self.treeFiltro.header().setHighlightSections(False)
        self.verticalLayout.addWidget(self.treeFiltro)
        self.frame = QtWidgets.QFrame(self.boxFiltro)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem4)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.labelSomaFiltro = QtWidgets.QLabel(self.frame)
        self.labelSomaFiltro.setObjectName("labelSomaFiltro")
        self.horizontalLayout_3.addWidget(self.labelSomaFiltro)
        self.verticalLayout.addWidget(self.frame)
        self.horizontalLayout_2.addWidget(self.boxFiltro)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.grafico = PlotRelatorio(Form)
        self.grafico.setMinimumSize(QtCore.QSize(600, 250))
        self.grafico.setObjectName("grafico")
        self.verticalLayout_2.addWidget(self.grafico)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.radioTodos.setText(_translate("Form", "Todos"))
        self.radioTotal.setText(_translate("Form", "Saída absoluto"))
        self.radioPercent.setText(_translate("Form", "Saída percentual"))
        self.radioButton.setText(_translate("Form", "Entrada e Saída"))
        self.checkRelSub.setText(_translate("Form", "Sub-categoria"))
        self.checkRelFim.setText(_translate("Form", "Fim"))
        self.checkRelCat.setText(_translate("Form", "Categoria"))
        self.checkRelInicio.setText(_translate("Form", "Início"))
        self.checkRelTipo.setText(_translate("Form", "Tipo"))
        self.comboTipo.setItemText(0, _translate("Form", "gasto"))
        self.comboTipo.setItemText(1, _translate("Form", "fixo"))
        self.comboTipo.setItemText(2, _translate("Form", "gasto+fixo"))
        self.comboTipo.setItemText(3, _translate("Form", "entrada"))
        self.checkRelNome.setText(_translate("Form", "Nome"))
        self.botaoFiltro.setText(_translate("Form", "Filtro"))
        self.botaoLimpa.setText(_translate("Form", "Limpa"))
        self.treeFiltro.setSortingEnabled(True)
        self.treeFiltro.headerItem().setText(0, _translate("Form", "Tipo"))
        self.treeFiltro.headerItem().setText(1, _translate("Form", "Item"))
        self.treeFiltro.headerItem().setText(2, _translate("Form", "Data"))
        self.treeFiltro.headerItem().setText(3, _translate("Form", "Categoria"))
        self.treeFiltro.headerItem().setText(4, _translate("Form", "Sub-categoria"))
        self.treeFiltro.headerItem().setText(5, _translate("Form", "Valor"))
        self.treeFiltro.headerItem().setText(6, _translate("Form", "Comentários"))
        self.label.setText(_translate("Form", "Soma: "))
        self.labelSomaFiltro.setText(_translate("Form", "R$0,00"))

from ui.plotcanvas import PlotRelatorio

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

