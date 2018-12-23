# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'janela.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(611, 464)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser.setGeometry(QtCore.QRect(100, 70, 321, 141))
        self.textBrowser.setObjectName("textBrowser")
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab_2)
        self.textBrowser_2.setGeometry(QtCore.QRect(160, 100, 301, 141))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.tab_3)
        self.textBrowser_3.setGeometry(QtCore.QRect(140, 80, 256, 111))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.boxConfig = QtWidgets.QGroupBox(self.tab_4)
        self.boxConfig.setGeometry(QtCore.QRect(20, 30, 541, 121))
        self.boxConfig.setObjectName("boxConfig")
        self.boxCategorias = QtWidgets.QGroupBox(self.tab_4)
        self.boxCategorias.setGeometry(QtCore.QRect(20, 170, 251, 201))
        self.boxCategorias.setObjectName("boxCategorias")
        self.treeCategorias = QtWidgets.QTreeWidget(self.boxCategorias)
        self.treeCategorias.setGeometry(QtCore.QRect(0, 20, 251, 181))
        self.treeCategorias.setAlternatingRowColors(True)
        self.treeCategorias.setObjectName("treeCategorias")
        self.treeCategorias.header().setVisible(False)
        self.boxPessoas = QtWidgets.QGroupBox(self.tab_4)
        self.boxPessoas.setGeometry(QtCore.QRect(310, 170, 251, 201))
        self.boxPessoas.setObjectName("boxPessoas")
        self.treePessoas = QtWidgets.QTreeWidget(self.boxPessoas)
        self.treePessoas.setGeometry(QtCore.QRect(0, 20, 251, 181))
        self.treePessoas.setAlternatingRowColors(True)
        self.treePessoas.setObjectName("treePessoas")
        self.treePessoas.header().setVisible(False)
        self.treePessoas.header().setDefaultSectionSize(100)
        self.botaoCategoriaAdicionar = QtWidgets.QPushButton(self.tab_4)
        self.botaoCategoriaAdicionar.setGeometry(QtCore.QRect(50, 380, 80, 25))
        self.botaoCategoriaAdicionar.setObjectName("botaoCategoriaAdicionar")
        self.botaoPessoaAdicionar = QtWidgets.QPushButton(self.tab_4)
        self.botaoPessoaAdicionar.setGeometry(QtCore.QRect(340, 380, 80, 25))
        self.botaoPessoaAdicionar.setObjectName("botaoPessoaAdicionar")
        self.botaoCategoriaEditar = QtWidgets.QPushButton(self.tab_4)
        self.botaoCategoriaEditar.setGeometry(QtCore.QRect(160, 380, 80, 25))
        self.botaoCategoriaEditar.setObjectName("botaoCategoriaEditar")
        self.pushButton_4 = QtWidgets.QPushButton(self.tab_4)
        self.pushButton_4.setGeometry(QtCore.QRect(450, 380, 80, 25))
        self.pushButton_4.setObjectName("pushButton_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.textBrowser.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Gasto no dia, valor disponível no dia</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">gasto no mês</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Padrão de gastos (percentuais)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">adição de novos gastos</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Lista dos últimos gastos</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">informações mais essenciais</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Ver os gastos do mês</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Form", "Hoje"))
        self.textBrowser_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Lista e cadastro dos gastos gerais (mensais e etc)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    Padrão de gastos (percentuais)</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Lista dos investimentos</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Informações do ano</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Geração de relatórios</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Form", "Geral"))
        self.textBrowser_3.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Lista de dívidas</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    O que eu devo</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    O que me devem</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("Form", "Dívidas"))
        self.boxConfig.setTitle(_translate("Form", "Configurações"))
        self.boxCategorias.setTitle(_translate("Form", "Categorias"))
        self.treeCategorias.headerItem().setText(0, _translate("Form", "nome"))
        self.treeCategorias.headerItem().setText(1, _translate("Form", "status"))
        self.boxPessoas.setTitle(_translate("Form", "Pessoas"))
        self.treePessoas.headerItem().setText(0, _translate("Form", "nome"))
        self.treePessoas.headerItem().setText(1, _translate("Form", "status"))
        self.botaoCategoriaAdicionar.setText(_translate("Form", "Adicionar"))
        self.botaoPessoaAdicionar.setText(_translate("Form", "Adicionar"))
        self.botaoCategoriaEditar.setText(_translate("Form", "Editar"))
        self.pushButton_4.setText(_translate("Form", "Editar"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("Form", "Configurações"))

