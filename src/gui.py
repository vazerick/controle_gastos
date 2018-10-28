import sys
from PyQt5.QtWidgets import QApplication, QDialog
from ui.form import Ui_Form
from ui.pessoas_add import Ui_Form as PessoasAdd
from ui.categorias_add import Ui_Form as CategoriasAdd


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
# seta a mesma fohla de estilos para todas as janelas
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



