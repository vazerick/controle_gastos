# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'janela.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1259, 600)
        Form.setMinimumSize(QtCore.QSize(1000, 600))
        Form.setMaximumSize(QtCore.QSize(10000, 600))
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(Form)
        self.tabWidget.setObjectName("tabWidget")
        self.Hoje = QtWidgets.QWidget()
        self.Hoje.setObjectName("Hoje")
        self.boxStatus = QtWidgets.QFrame(self.Hoje)
        self.boxStatus.setGeometry(QtCore.QRect(120, 0, 561, 231))
        self.boxStatus.setObjectName("boxStatus")
        self.frame = QtWidgets.QFrame(self.boxStatus)
        self.frame.setGeometry(QtCore.QRect(10, 80, 531, 141))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.boxHoje = QtWidgets.QGroupBox(self.frame)
        self.boxHoje.setGeometry(QtCore.QRect(10, 0, 141, 131))
        self.boxHoje.setStyleSheet("")
        self.boxHoje.setObjectName("boxHoje")
        self.frameHojeGasto = QtWidgets.QFrame(self.boxHoje)
        self.frameHojeGasto.setGeometry(QtCore.QRect(10, 30, 121, 21))
        self.frameHojeGasto.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameHojeGasto.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameHojeGasto.setObjectName("frameHojeGasto")
        self.labelHojeGasto = QtWidgets.QLabel(self.frameHojeGasto)
        self.labelHojeGasto.setGeometry(QtCore.QRect(0, 0, 54, 17))
        self.labelHojeGasto.setObjectName("labelHojeGasto")
        self.labelHojeGastoV = QtWidgets.QLabel(self.frameHojeGasto)
        self.labelHojeGastoV.setGeometry(QtCore.QRect(50, 0, 71, 17))
        self.labelHojeGastoV.setObjectName("labelHojeGastoV")
        self.frameHojeLimite = QtWidgets.QFrame(self.boxHoje)
        self.frameHojeLimite.setGeometry(QtCore.QRect(10, 50, 121, 21))
        self.frameHojeLimite.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameHojeLimite.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameHojeLimite.setObjectName("frameHojeLimite")
        self.labelHojeLimite = QtWidgets.QLabel(self.frameHojeLimite)
        self.labelHojeLimite.setGeometry(QtCore.QRect(0, 0, 54, 17))
        self.labelHojeLimite.setObjectName("labelHojeLimite")
        self.labelHojeLimiteV = QtWidgets.QLabel(self.frameHojeLimite)
        self.labelHojeLimiteV.setGeometry(QtCore.QRect(50, 0, 71, 17))
        self.labelHojeLimiteV.setObjectName("labelHojeLimiteV")
        self.frameHojeResto = QtWidgets.QFrame(self.boxHoje)
        self.frameHojeResto.setGeometry(QtCore.QRect(10, 70, 121, 21))
        self.frameHojeResto.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameHojeResto.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameHojeResto.setObjectName("frameHojeResto")
        self.labelHojeResto = QtWidgets.QLabel(self.frameHojeResto)
        self.labelHojeResto.setGeometry(QtCore.QRect(0, 0, 54, 17))
        self.labelHojeResto.setObjectName("labelHojeResto")
        self.labelHojeRestaV = QtWidgets.QLabel(self.frameHojeResto)
        self.labelHojeRestaV.setGeometry(QtCore.QRect(50, 0, 71, 17))
        self.labelHojeRestaV.setObjectName("labelHojeRestaV")
        self.progressBarHoje = QtWidgets.QProgressBar(self.boxHoje)
        self.progressBarHoje.setGeometry(QtCore.QRect(0, 100, 141, 31))
        self.progressBarHoje.setMaximum(100)
        self.progressBarHoje.setProperty("value", 24)
        self.progressBarHoje.setObjectName("progressBarHoje")
        self.boxMes = QtWidgets.QGroupBox(self.frame)
        self.boxMes.setGeometry(QtCore.QRect(180, 0, 141, 131))
        self.boxMes.setObjectName("boxMes")
        self.frameMesGasto = QtWidgets.QFrame(self.boxMes)
        self.frameMesGasto.setGeometry(QtCore.QRect(10, 30, 121, 21))
        self.frameMesGasto.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameMesGasto.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameMesGasto.setObjectName("frameMesGasto")
        self.labelMesGasto = QtWidgets.QLabel(self.frameMesGasto)
        self.labelMesGasto.setGeometry(QtCore.QRect(0, 0, 54, 17))
        self.labelMesGasto.setObjectName("labelMesGasto")
        self.labelMesGastoV = QtWidgets.QLabel(self.frameMesGasto)
        self.labelMesGastoV.setGeometry(QtCore.QRect(50, 0, 71, 17))
        self.labelMesGastoV.setObjectName("labelMesGastoV")
        self.frameMesLimite = QtWidgets.QFrame(self.boxMes)
        self.frameMesLimite.setGeometry(QtCore.QRect(10, 50, 121, 21))
        self.frameMesLimite.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameMesLimite.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameMesLimite.setObjectName("frameMesLimite")
        self.labelMesLimite = QtWidgets.QLabel(self.frameMesLimite)
        self.labelMesLimite.setGeometry(QtCore.QRect(0, 0, 54, 17))
        self.labelMesLimite.setObjectName("labelMesLimite")
        self.labelMesLimiteV = QtWidgets.QLabel(self.frameMesLimite)
        self.labelMesLimiteV.setGeometry(QtCore.QRect(50, 0, 71, 17))
        self.labelMesLimiteV.setObjectName("labelMesLimiteV")
        self.frameMesResta = QtWidgets.QFrame(self.boxMes)
        self.frameMesResta.setGeometry(QtCore.QRect(10, 70, 121, 21))
        self.frameMesResta.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameMesResta.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameMesResta.setObjectName("frameMesResta")
        self.labelMesResta = QtWidgets.QLabel(self.frameMesResta)
        self.labelMesResta.setGeometry(QtCore.QRect(0, 0, 54, 17))
        self.labelMesResta.setObjectName("labelMesResta")
        self.labelMesRestaV = QtWidgets.QLabel(self.frameMesResta)
        self.labelMesRestaV.setGeometry(QtCore.QRect(50, 0, 71, 17))
        self.labelMesRestaV.setObjectName("labelMesRestaV")
        self.progressBarMes = QtWidgets.QProgressBar(self.boxMes)
        self.progressBarMes.setGeometry(QtCore.QRect(0, 100, 141, 31))
        self.progressBarMes.setProperty("value", 24)
        self.progressBarMes.setObjectName("progressBarMes")
        self.boxMedia = QtWidgets.QGroupBox(self.frame)
        self.boxMedia.setGeometry(QtCore.QRect(350, 10, 141, 41))
        self.boxMedia.setAlignment(QtCore.Qt.AlignCenter)
        self.boxMedia.setObjectName("boxMedia")
        self.labelMedia = QtWidgets.QLabel(self.boxMedia)
        self.labelMedia.setGeometry(QtCore.QRect(80, 20, 61, 17))
        self.labelMedia.setObjectName("labelMedia")
        self.boxLimiteDia = QtWidgets.QGroupBox(self.frame)
        self.boxLimiteDia.setGeometry(QtCore.QRect(350, 50, 141, 41))
        self.boxLimiteDia.setAlignment(QtCore.Qt.AlignCenter)
        self.boxLimiteDia.setObjectName("boxLimiteDia")
        self.labelLimiteDia = QtWidgets.QLabel(self.boxLimiteDia)
        self.labelLimiteDia.setGeometry(QtCore.QRect(80, 20, 61, 17))
        self.labelLimiteDia.setObjectName("labelLimiteDia")
        self.boxAjuste = QtWidgets.QGroupBox(self.frame)
        self.boxAjuste.setGeometry(QtCore.QRect(350, 90, 141, 41))
        self.boxAjuste.setAlignment(QtCore.Qt.AlignCenter)
        self.boxAjuste.setObjectName("boxAjuste")
        self.labelAjuste = QtWidgets.QLabel(self.boxAjuste)
        self.labelAjuste.setGeometry(QtCore.QRect(80, 20, 61, 17))
        self.labelAjuste.setObjectName("labelAjuste")
        self.groupDia = QtWidgets.QGroupBox(self.boxStatus)
        self.groupDia.setGeometry(QtCore.QRect(10, 20, 531, 55))
        self.groupDia.setObjectName("groupDia")
        self.frameTotalEntrada = QtWidgets.QFrame(self.groupDia)
        self.frameTotalEntrada.setGeometry(QtCore.QRect(10, 30, 151, 21))
        self.frameTotalEntrada.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameTotalEntrada.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameTotalEntrada.setObjectName("frameTotalEntrada")
        self.labelTotalEntrada = QtWidgets.QLabel(self.frameTotalEntrada)
        self.labelTotalEntrada.setGeometry(QtCore.QRect(20, 0, 54, 17))
        self.labelTotalEntrada.setObjectName("labelTotalEntrada")
        self.labelTotalEntradaV = QtWidgets.QLabel(self.frameTotalEntrada)
        self.labelTotalEntradaV.setGeometry(QtCore.QRect(80, 0, 71, 17))
        self.labelTotalEntradaV.setObjectName("labelTotalEntradaV")
        self.frameTotalFixo = QtWidgets.QFrame(self.groupDia)
        self.frameTotalFixo.setGeometry(QtCore.QRect(180, 30, 171, 21))
        self.frameTotalFixo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameTotalFixo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameTotalFixo.setObjectName("frameTotalFixo")
        self.labelTotalFixo = QtWidgets.QLabel(self.frameTotalFixo)
        self.labelTotalFixo.setGeometry(QtCore.QRect(20, 0, 81, 17))
        self.labelTotalFixo.setObjectName("labelTotalFixo")
        self.labelTotalFixoV = QtWidgets.QLabel(self.frameTotalFixo)
        self.labelTotalFixoV.setGeometry(QtCore.QRect(100, 0, 71, 17))
        self.labelTotalFixoV.setObjectName("labelTotalFixoV")
        self.frameTotalReserva = QtWidgets.QFrame(self.groupDia)
        self.frameTotalReserva.setGeometry(QtCore.QRect(370, 30, 151, 21))
        self.frameTotalReserva.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameTotalReserva.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameTotalReserva.setObjectName("frameTotalReserva")
        self.labelTotalReserva = QtWidgets.QLabel(self.frameTotalReserva)
        self.labelTotalReserva.setGeometry(QtCore.QRect(20, 0, 54, 17))
        self.labelTotalReserva.setObjectName("labelTotalReserva")
        self.labelTotalReservaV = QtWidgets.QLabel(self.frameTotalReserva)
        self.labelTotalReservaV.setGeometry(QtCore.QRect(80, 0, 71, 17))
        self.labelTotalReservaV.setObjectName("labelTotalReservaV")
        self.botaoGasto = QtWidgets.QPushButton(self.Hoje)
        self.botaoGasto.setGeometry(QtCore.QRect(10, 40, 91, 25))
        self.botaoGasto.setObjectName("botaoGasto")
        self.stackedWidget = QtWidgets.QStackedWidget(self.Hoje)
        self.stackedWidget.setEnabled(True)
        self.stackedWidget.setGeometry(QtCore.QRect(130, 240, 511, 291))
        self.stackedWidget.setMouseTracking(False)
        self.stackedWidget.setAutoFillBackground(False)
        self.stackedWidget.setObjectName("stackedWidget")
        self.pageGastos = QtWidgets.QWidget()
        self.pageGastos.setObjectName("pageGastos")
        self.boxGastos = QtWidgets.QGroupBox(self.pageGastos)
        self.boxGastos.setGeometry(QtCore.QRect(0, 0, 511, 291))
        self.boxGastos.setObjectName("boxGastos")
        self.treeSaida = QtWidgets.QTreeWidget(self.boxGastos)
        self.treeSaida.setGeometry(QtCore.QRect(0, 20, 511, 271))
        self.treeSaida.setAlternatingRowColors(True)
        self.treeSaida.setRootIsDecorated(True)
        self.treeSaida.setUniformRowHeights(False)
        self.treeSaida.setItemsExpandable(False)
        self.treeSaida.setWordWrap(True)
        self.treeSaida.setHeaderHidden(True)
        self.treeSaida.setObjectName("treeSaida")
        self.treeSaida.header().setVisible(False)
        self.treeSaida.header().setCascadingSectionResizes(False)
        self.treeSaida.header().setHighlightSections(False)
        self.stackedWidget.addWidget(self.pageGastos)
        self.pageEntrada = QtWidgets.QWidget()
        self.pageEntrada.setObjectName("pageEntrada")
        self.boxEntrada = QtWidgets.QGroupBox(self.pageEntrada)
        self.boxEntrada.setGeometry(QtCore.QRect(0, 0, 511, 291))
        self.boxEntrada.setObjectName("boxEntrada")
        self.treeEntrada = QtWidgets.QTreeWidget(self.boxEntrada)
        self.treeEntrada.setGeometry(QtCore.QRect(0, 20, 511, 271))
        self.treeEntrada.setAlternatingRowColors(True)
        self.treeEntrada.setWordWrap(True)
        self.treeEntrada.setObjectName("treeEntrada")
        self.treeEntrada.header().setVisible(False)
        self.stackedWidget.addWidget(self.pageEntrada)
        self.pageFixo = QtWidgets.QWidget()
        self.pageFixo.setObjectName("pageFixo")
        self.boxFixo = QtWidgets.QGroupBox(self.pageFixo)
        self.boxFixo.setGeometry(QtCore.QRect(0, 0, 511, 291))
        self.boxFixo.setObjectName("boxFixo")
        self.treeFixo = QtWidgets.QTreeWidget(self.boxFixo)
        self.treeFixo.setGeometry(QtCore.QRect(0, 20, 511, 271))
        self.treeFixo.setAlternatingRowColors(True)
        self.treeFixo.setRootIsDecorated(True)
        self.treeFixo.setUniformRowHeights(False)
        self.treeFixo.setItemsExpandable(False)
        self.treeFixo.setWordWrap(True)
        self.treeFixo.setHeaderHidden(True)
        self.treeFixo.setObjectName("treeFixo")
        self.treeFixo.header().setVisible(False)
        self.treeFixo.header().setCascadingSectionResizes(False)
        self.treeFixo.header().setHighlightSections(False)
        self.stackedWidget.addWidget(self.pageFixo)
        self.pageReserva = QtWidgets.QWidget()
        self.pageReserva.setObjectName("pageReserva")
        self.boxSaidas_2 = QtWidgets.QGroupBox(self.pageReserva)
        self.boxSaidas_2.setGeometry(QtCore.QRect(0, 0, 521, 291))
        self.boxSaidas_2.setObjectName("boxSaidas_2")
        self.treeReserva = QtWidgets.QTreeWidget(self.boxSaidas_2)
        self.treeReserva.setGeometry(QtCore.QRect(0, 20, 511, 271))
        self.treeReserva.setAlternatingRowColors(True)
        self.treeReserva.setRootIsDecorated(True)
        self.treeReserva.setUniformRowHeights(False)
        self.treeReserva.setItemsExpandable(False)
        self.treeReserva.setWordWrap(True)
        self.treeReserva.setHeaderHidden(False)
        self.treeReserva.setObjectName("treeReserva")
        self.treeReserva.header().setVisible(True)
        self.treeReserva.header().setCascadingSectionResizes(False)
        self.treeReserva.header().setHighlightSections(False)
        self.stackedWidget.addWidget(self.pageReserva)
        self.botaoEntrada = QtWidgets.QPushButton(self.Hoje)
        self.botaoEntrada.setGeometry(QtCore.QRect(10, 70, 91, 25))
        self.botaoEntrada.setObjectName("botaoEntrada")
        self.botaoFixo = QtWidgets.QPushButton(self.Hoje)
        self.botaoFixo.setGeometry(QtCore.QRect(10, 100, 91, 25))
        self.botaoFixo.setObjectName("botaoFixo")
        self.botaoReserva = QtWidgets.QPushButton(self.Hoje)
        self.botaoReserva.setGeometry(QtCore.QRect(10, 130, 91, 25))
        self.botaoReserva.setObjectName("botaoReserva")
        self.listMenu = QtWidgets.QListWidget(self.Hoje)
        self.listMenu.setGeometry(QtCore.QRect(60, 260, 71, 192))
        self.listMenu.setAlternatingRowColors(False)
        self.listMenu.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.listMenu.setProperty("isWrapping", True)
        self.listMenu.setObjectName("listMenu")
        item = QtWidgets.QListWidgetItem()
        self.listMenu.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listMenu.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listMenu.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listMenu.addItem(item)
        self.graficoPizza = PlotPizza(self.Hoje)
        self.graficoPizza.setGeometry(QtCore.QRect(670, 10, 551, 261))
        self.graficoPizza.setObjectName("graficoPizza")
        self.graficoBarra = PlotBarra(self.Hoje)
        self.graficoBarra.setGeometry(QtCore.QRect(670, 270, 551, 261))
        self.graficoBarra.setObjectName("graficoBarra")
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
        self.stackedWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Controle de Gastos"))
        self.boxHoje.setAccessibleName(_translate("Form", "progresso"))
        self.boxHoje.setTitle(_translate("Form", "Diário"))
        self.labelHojeGasto.setText(_translate("Form", "Gasto:"))
        self.labelHojeGastoV.setText(_translate("Form", "R$1000,00"))
        self.labelHojeLimite.setText(_translate("Form", "Limite:"))
        self.labelHojeLimiteV.setText(_translate("Form", "R$1000,00"))
        self.labelHojeResto.setText(_translate("Form", "Resta:"))
        self.labelHojeRestaV.setText(_translate("Form", "R$1000,00"))
        self.boxMes.setAccessibleName(_translate("Form", "progresso"))
        self.boxMes.setTitle(_translate("Form", "Mensal"))
        self.labelMesGasto.setText(_translate("Form", "Gasto:"))
        self.labelMesGastoV.setText(_translate("Form", "R$1000,00"))
        self.labelMesLimite.setText(_translate("Form", "Limite:"))
        self.labelMesLimiteV.setText(_translate("Form", "R$1000,00"))
        self.labelMesResta.setText(_translate("Form", "Resta:"))
        self.labelMesRestaV.setText(_translate("Form", "R$1000,00"))
        self.boxMedia.setAccessibleName(_translate("Form", "quadro"))
        self.boxMedia.setTitle(_translate("Form", "Média de gasto por dia"))
        self.labelMedia.setText(_translate("Form", "R$100,00"))
        self.boxLimiteDia.setAccessibleName(_translate("Form", "quadro"))
        self.boxLimiteDia.setTitle(_translate("Form", "Limite por dia"))
        self.labelLimiteDia.setText(_translate("Form", "R$100,00"))
        self.boxAjuste.setAccessibleName(_translate("Form", "quadro"))
        self.boxAjuste.setTitle(_translate("Form", "{ajuste}"))
        self.labelAjuste.setText(_translate("Form", "R$100,00"))
        self.groupDia.setTitle(_translate("Form", "Dia: 02 de 28 (07%)"))
        self.labelTotalEntrada.setText(_translate("Form", "Entrada:"))
        self.labelTotalEntradaV.setText(_translate("Form", "R$1000,00"))
        self.labelTotalFixo.setText(_translate("Form", "Gastos Fixos:"))
        self.labelTotalFixoV.setText(_translate("Form", "R$1000,00"))
        self.labelTotalReserva.setText(_translate("Form", "Reserva:"))
        self.labelTotalReservaV.setText(_translate("Form", "R$1000,00"))
        self.botaoGasto.setText(_translate("Form", "Novo Gasto"))
        self.boxGastos.setTitle(_translate("Form", "Gastos"))
        self.treeSaida.setSortingEnabled(True)
        self.treeSaida.headerItem().setText(0, _translate("Form", "Data"))
        self.treeSaida.headerItem().setText(1, _translate("Form", "Item"))
        self.treeSaida.headerItem().setText(2, _translate("Form", "Categoria"))
        self.treeSaida.headerItem().setText(3, _translate("Form", "Sub-categoria"))
        self.treeSaida.headerItem().setText(4, _translate("Form", "Valor"))
        self.boxEntrada.setTitle(_translate("Form", "Entrada"))
        self.treeEntrada.setSortingEnabled(True)
        self.treeEntrada.headerItem().setText(0, _translate("Form", "Item"))
        self.treeEntrada.headerItem().setText(1, _translate("Form", "Previsão"))
        self.treeEntrada.headerItem().setText(2, _translate("Form", "Data"))
        self.treeEntrada.headerItem().setText(3, _translate("Form", "Valor"))
        self.boxFixo.setTitle(_translate("Form", "Saídas do Mês"))
        self.treeFixo.setSortingEnabled(True)
        self.treeFixo.headerItem().setText(0, _translate("Form", "Item"))
        self.treeFixo.headerItem().setText(1, _translate("Form", "Data"))
        self.treeFixo.headerItem().setText(2, _translate("Form", "Item"))
        self.treeFixo.headerItem().setText(3, _translate("Form", "Categoria"))
        self.treeFixo.headerItem().setText(4, _translate("Form", "Sub-categoria"))
        self.treeFixo.headerItem().setText(5, _translate("Form", "Valor"))
        self.boxSaidas_2.setTitle(_translate("Form", "Reserva"))
        self.treeReserva.setSortingEnabled(True)
        self.treeReserva.headerItem().setText(0, _translate("Form", "Item"))
        self.treeReserva.headerItem().setText(1, _translate("Form", "Valor"))
        self.treeReserva.headerItem().setText(2, _translate("Form", "Comentário"))
        self.botaoEntrada.setText(_translate("Form", "Nova Entrada"))
        self.botaoFixo.setText(_translate("Form", "Novo Fixo"))
        self.botaoReserva.setText(_translate("Form", "Nova Reserva"))
        self.listMenu.setAccessibleName(_translate("Form", "selecao"))
        __sortingEnabled = self.listMenu.isSortingEnabled()
        self.listMenu.setSortingEnabled(False)
        item = self.listMenu.item(0)
        item.setText(_translate("Form", "Gastos"))
        item = self.listMenu.item(1)
        item.setText(_translate("Form", "Entrada"))
        item = self.listMenu.item(2)
        item.setText(_translate("Form", "Fixo"))
        item = self.listMenu.item(3)
        item.setText(_translate("Form", "Reserva"))
        self.listMenu.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Hoje), _translate("Form", "Hoje"))
        self.textBrowser_2.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Noto Sans\'; font-size:9pt;\">Lista e cadastro dos gastos gerais (mensais e etc)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Noto Sans\'; font-size:9pt;\">    Padrão de gastos (percentuais)</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Noto Sans\'; font-size:9pt;\">Lista dos investimentos</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Noto Sans\'; font-size:9pt;\">Informações do ano</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Noto Sans\'; font-size:9pt;\">Geração de relatórios</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Noto Sans\'; font-size:9pt;\"><br /></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Noto Sans\'; font-size:9pt;\"><br /></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Geral), _translate("Form", "Geral"))
        self.textBrowser_3.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Noto Sans\'; font-size:9pt;\">Lista de dívidas</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Noto Sans\'; font-size:9pt;\">    O que eu devo</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Noto Sans\'; font-size:9pt;\">    O que me devem</span></p></body></html>"))
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

from ui.plotcanvas import PlotBarra, PlotPizza

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

