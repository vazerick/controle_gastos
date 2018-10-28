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

        self.altura=110
        self.extra=0
        self.fator=15
        self.lista=''

        self.wSubCategoriasAdd = QDialog()
        self.uiSubCategoriasAdd = SubCategoriasAdd()
        self.uiSubCategoriasAdd.setupUi(self.wSubCategoriasAdd)
# seta a mesma folha de estilos para todas as janelas
        arquivo = open("ui/style.css")
        self.style = arquivo.read()
        arquivo.close()
        for janela in [
            self.window,
            self.wPessoasAdd,
            self.wCategoriasAdd
        ]:
            janela.setStyleSheet(self.style)


# inicializa a janela
        self.window.show()

    def subcategorias_extra(self, nome):
        self.lista = self.lista+nome+'\n'
        self.extra += 1
        self.wSubCategoriasAdd.resize(
            260,
            self.altura+(self.extra*self.fator)
        )
        self.uiSubCategoriasAdd.botaoOk.setGeometry(QtCore.QRect(40, 70+(self.extra*self.fator), 80, 25))
        self.uiSubCategoriasAdd.botaoCancela.setGeometry(QtCore.QRect(150, 70 + (self.extra*self.fator), 80, 25))
        self.uiSubCategoriasAdd.botaoMais.setGeometry(QtCore.QRect(230, 30 + (self.extra*self.fator), 25, 25))
        self.uiSubCategoriasAdd.labelNome.setGeometry(QtCore.QRect(20, 10 + (self.extra*self.fator), 54, 17))
        self.uiSubCategoriasAdd.inputNome.setGeometry(QtCore.QRect(10, 30 + (self.extra*self.fator), 211, 25))
        self.uiSubCategoriasAdd.lista.setGeometry(QtCore.QRect(20, 5, 201, 20 + (self.extra * self.fator)))
        self.uiSubCategoriasAdd.lista.setText(self.lista)
        print(self.lista)


    def subcategorias_reseta(self):
        self.lista = ''
        self.extra = 0
        self.wSubCategoriasAdd.resize(260, 118)
        self.uiSubCategoriasAdd.botaoOk.setGeometry(QtCore.QRect(40, 70, 80, 25))
        self.uiSubCategoriasAdd.botaoCancela.setGeometry(QtCore.QRect(150, 70, 80, 25))
        self.uiSubCategoriasAdd.botaoMais.setGeometry(QtCore.QRect(230, 30, 25, 25))
        self.uiSubCategoriasAdd.labelNome.setGeometry(QtCore.QRect(20, 10, 54, 17))
        self.uiSubCategoriasAdd.inputNome.setGeometry(QtCore.QRect(10, 30, 211, 25))
        self.uiSubCategoriasAdd.lista.setGeometry(QtCore.QRect(20, 5, 201, 20))
        self.uiSubCategoriasAdd.lista.setText('')
