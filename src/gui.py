import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5 import QtCore, QtWidgets
from ui.form import Ui_Form
from ui.pessoas_add import Ui_Form as PessoasAdd
from ui.categorias_add import Ui_Form as CategoriasAdd
from ui.subcategorias_add import Ui_Form as SubCategoriasAdd


class gui:

    def __init__(self):
# declarações da interface gráfica

        self.app = QApplication(sys.argv)

# formulário de testes
        self.window = QDialog()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window)

# janela para adicionar novas pessoas
        self.wPessoasAdd = QDialog()
        self.uiPessoasAdd = PessoasAdd()
        self.uiPessoasAdd.setupUi(self.wPessoasAdd)

# janela para adicionar novas categoiras
        self.wCategoriasAdd = QDialog()
        self.uiCategoriasAdd = CategoriasAdd()
        self.uiCategoriasAdd.setupUi(self.wCategoriasAdd)

# janela para adicionar novas sub-categorias
        self.altura=250
        self.extra=0
        self.fator=10
        self.lista=''

        self.wSubCategoriasAdd = QDialog()
        self.uiSubCategoriasAdd = SubCategoriasAdd()
        self.uiSubCategoriasAdd.setupUi(self.wSubCategoriasAdd)
        self.uiSubCategoriasAdd.listWidget.hide()

# seta a mesma folha de estilos para todas as janelas
        arquivo = open("ui/style.css")
        self.style = arquivo.read()
        arquivo.close()
        for janela in [
            self.window,
            self.wPessoasAdd,
            self.wCategoriasAdd,
            self.wSubCategoriasAdd
        ]:
            janela.setStyleSheet(self.style)


# inicializa a janela
        self.window.show()

    def subcategorias_extra(self, nome):
        self.extra += 1

        self.wSubCategoriasAdd.setMaximumSize(QtCore.QSize(
            260,
            self.altura + (self.extra * self.fator))
        )
        self.wSubCategoriasAdd.resize(
            260,
            self.altura+(self.extra*self.fator)
        )
        self.uiSubCategoriasAdd.botaoOk.setGeometry(QtCore.QRect(40, 210+(self.extra*self.fator), 80, 25))
        self.uiSubCategoriasAdd.botaoCancela.setGeometry(QtCore.QRect(150, 210 + (self.extra*self.fator), 80, 25))

        self.uiSubCategoriasAdd.comboSub.setGeometry(QtCore.QRect(10, 170 + (self.extra * self.fator), 241, 25))
        self.uiSubCategoriasAdd.labelAntes.setGeometry(QtCore.QRect(20, 150 + (self.extra * self.fator), 111, 17))
        self.uiSubCategoriasAdd.labelCategoria.setGeometry(QtCore.QRect(20, 100 + (self.extra * self.fator), 111, 17))
        self.uiSubCategoriasAdd.comboCat.setGeometry(QtCore.QRect(10, 120 + (self.extra * self.fator), 241, 25))

        self.uiSubCategoriasAdd.listWidget.setGeometry(QtCore.QRect(10, 60, 241, 31 + (self.extra * self.fator)))
        self.uiSubCategoriasAdd.listWidget.addItem(nome)
        self.uiSubCategoriasAdd.listWidget.show()

    def subcategorias_remove(self):
        self.extra -= 1

        self.wSubCategoriasAdd.setMaximumSize(QtCore.QSize(
            260,
            self.altura + (self.extra * self.fator))
        )
        self.wSubCategoriasAdd.resize(
            260,
            self.altura+(self.extra*self.fator)
        )
        self.uiSubCategoriasAdd.botaoOk.setGeometry(QtCore.QRect(40, 210+(self.extra*self.fator), 80, 25))
        self.uiSubCategoriasAdd.botaoCancela.setGeometry(QtCore.QRect(150, 210 + (self.extra*self.fator), 80, 25))

        self.uiSubCategoriasAdd.comboSub.setGeometry(QtCore.QRect(10, 170 + (self.extra * self.fator), 241, 25))
        self.uiSubCategoriasAdd.labelAntes.setGeometry(QtCore.QRect(20, 150 + (self.extra * self.fator), 111, 17))
        self.uiSubCategoriasAdd.labelCategoria.setGeometry(QtCore.QRect(20, 100 + (self.extra * self.fator), 111, 17))
        self.uiSubCategoriasAdd.comboCat.setGeometry(QtCore.QRect(10, 120 + (self.extra * self.fator), 241, 25))

        self.uiSubCategoriasAdd.listWidget.setGeometry(QtCore.QRect(10, 60, 241, 31 + (self.extra * self.fator)))
        self.uiSubCategoriasAdd.listWidget.takeItem(self.uiSubCategoriasAdd.listWidget.currentRow())
        self.uiSubCategoriasAdd.listWidget.show()


    def subcategorias_reseta(self):
        self.lista = ''
        self.extra = 0

        self.wSubCategoriasAdd.setMaximumSize(QtCore.QSize(
            260,
            self.altura)
        )
        self.wSubCategoriasAdd.resize(
            260,
            self.altura
        )
        self.uiSubCategoriasAdd.botaoOk.setGeometry(QtCore.QRect(40, 210, 80, 25))
        self.uiSubCategoriasAdd.botaoCancela.setGeometry(QtCore.QRect(150, 210, 80, 25))

        self.uiSubCategoriasAdd.comboSub.setGeometry(QtCore.QRect(10, 170, 241, 25))
        self.uiSubCategoriasAdd.labelAntes.setGeometry(QtCore.QRect(20, 150, 111, 17))
        self.uiSubCategoriasAdd.labelCategoria.setGeometry(QtCore.QRect(20, 100, 111, 17))
        self.uiSubCategoriasAdd.comboCat.setGeometry(QtCore.QRect(10, 120, 241, 25))

        self.uiSubCategoriasAdd.listWidget.setGeometry(QtCore.QRect(10, 60, 241, 31))
        self.uiSubCategoriasAdd.listWidget.clear()
        self.uiSubCategoriasAdd.listWidget.hide()
