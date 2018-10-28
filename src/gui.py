import sys
from PyQt5.QtWidgets import QApplication, QDialog
from ui.form import Ui_Form
from ui.pessoas_add import Ui_Form as PessoasAdd


class gui:

    def __init__(self):
        # declarações da interface gráfica

        self.app = QApplication(sys.argv)

        self.window = QDialog()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window)

        self.wPessoasAdd = QDialog()
        self.uiPessoasAdd = PessoasAdd()
        self.uiPessoasAdd.setupUi(self.wPessoasAdd)

        arquivo = open("ui/style.css")
        self.style = arquivo.read()
        arquivo.close()
        for janela in [
            self.window,
            self.wPessoasAdd
        ]:
            janela.setStyleSheet(self.style)

        # inicializa a janela
        self.window.show()



