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
        Form.resize(1000, 600)
        Form.setMinimumSize(QtCore.QSize(1000, 600))
        Form.setMaximumSize(QtCore.QSize(1000, 600))
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setObjectName("tabWidget")
        self.Hoje = QtWidgets.QWidget()
        self.Hoje.setObjectName("Hoje")
        self.textBrowser = QtWidgets.QTextBrowser(self.Hoje)
        self.textBrowser.setGeometry(QtCore.QRect(10, 10, 321, 141))
        self.textBrowser.setObjectName("textBrowser")
        self.tabWidget.addTab(self.Hoje, "")
        self.Geral = QtWidgets.QWidget()
        self.Geral.setObjectName("Geral")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.Geral)
        self.textBrowser_2.setGeometry(QtCore.QRect(10, 10, 301, 141))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.tabWidget.addTab(self.Geral, "")
        self.Dividas = QtWidgets.QWidget()
        self.Dividas.setObjectName("Dividas")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.Dividas)
        self.textBrowser_3.setGeometry(QtCore.QRect(10, 10, 256, 111))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.tabWidget.addTab(self.Dividas, "")
        self.Config = QtWidgets.QWidget()
        self.Config.setObjectName("Config")
        self.boxConfig = QtWidgets.QGroupBox(self.Config)
        self.boxConfig.setGeometry(QtCore.QRect(50, 30, 881, 171))
        self.boxConfig.setObjectName("boxConfig")
        self.boxCategorias = QtWidgets.QGroupBox(self.Config)
        self.boxCategorias.setGeometry(QtCore.QRect(90, 230, 381, 241))
        self.boxCategorias.setObjectName("boxCategorias")
        self.treeCategorias = QtWidgets.QTreeWidget(self.boxCategorias)
        self.treeCategorias.setGeometry(QtCore.QRect(0, 20, 381, 221))
        self.treeCategorias.setAlternatingRowColors(True)
        self.treeCategorias.setObjectName("treeCategorias")
        self.treeCategorias.header().setVisible(False)
        self.boxPessoas = QtWidgets.QGroupBox(self.Config)
        self.boxPessoas.setGeometry(QtCore.QRect(510, 230, 380, 241))
        self.boxPessoas.setObjectName("boxPessoas")
        self.treePessoas = QtWidgets.QTreeWidget(self.boxPessoas)
        self.treePessoas.setGeometry(QtCore.QRect(0, 20, 380, 221))
        self.treePessoas.setAlternatingRowColors(True)
        self.treePessoas.setObjectName("treePessoas")
        self.treePessoas.header().setVisible(False)
        self.treePessoas.header().setDefaultSectionSize(100)
        self.botaoCategoriaAdicionar = QtWidgets.QPushButton(self.Config)
        self.botaoCategoriaAdicionar.setGeometry(QtCore.QRect(140, 480, 131, 25))
        self.botaoCategoriaAdicionar.setObjectName("botaoCategoriaAdicionar")
        self.botaoPessoaAdicionar = QtWidgets.QPushButton(self.Config)
        self.botaoPessoaAdicionar.setGeometry(QtCore.QRect(560, 490, 111, 25))
        self.botaoPessoaAdicionar.setObjectName("botaoPessoaAdicionar")
        self.botaoCategoriaEditar = QtWidgets.QPushButton(self.Config)
        self.botaoCategoriaEditar.setGeometry(QtCore.QRect(330, 490, 80, 31))
        self.botaoCategoriaEditar.setObjectName("botaoCategoriaEditar")
        self.botaoPessoaEditar = QtWidgets.QPushButton(self.Config)
        self.botaoPessoaEditar.setGeometry(QtCore.QRect(750, 490, 80, 25))
        self.botaoPessoaEditar.setObjectName("botaoPessoaEditar")
        self.botaoSubAdicionar = QtWidgets.QPushButton(self.Config)
        self.botaoSubAdicionar.setGeometry(QtCore.QRect(130, 510, 151, 25))
        self.botaoSubAdicionar.setObjectName("botaoSubAdicionar")
        self.tabWidget.addTab(self.Config, "")
        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        self.retranslateUi(Form)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Controle de Gastos"))
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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Hoje), _translate("Form", "Hoje"))
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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Geral), _translate("Form", "Geral"))
        self.textBrowser_3.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Noto Sans\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Lista de dívidas</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    O que eu devo</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">    O que me devem</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Dividas), _translate("Form", "Dívidas"))
        self.boxConfig.setTitle(_translate("Form", "Configurações"))
        self.boxCategorias.setTitle(_translate("Form", "Categorias"))
        self.treeCategorias.headerItem().setText(0, _translate("Form", "nome"))
        self.treeCategorias.headerItem().setText(1, _translate("Form", "status"))
        self.boxPessoas.setTitle(_translate("Form", "Pessoas"))
        self.treePessoas.headerItem().setText(0, _translate("Form", "nome"))
        self.treePessoas.headerItem().setText(1, _translate("Form", "status"))
        self.botaoCategoriaAdicionar.setText(_translate("Form", "Adicionar Categoria"))
        self.botaoPessoaAdicionar.setText(_translate("Form", "Adicionar Pessoa"))
        self.botaoCategoriaEditar.setText(_translate("Form", "Editar"))
        self.botaoPessoaEditar.setText(_translate("Form", "Editar"))
        self.botaoSubAdicionar.setText(_translate("Form", "Adicionar Sub-Categoria"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Config), _translate("Form", "Configurações"))

