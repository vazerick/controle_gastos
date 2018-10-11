import sys
from PyQt5.QtWidgets import QApplication, QDialog

from src.lista import ListaPessoa

from src.form import Ui_Form


#declarações da interface gráfica
app = QApplication(sys.argv)
window = QDialog()
ui = Ui_Form()
ui.setupUi(window)

#inicializa a janela
#window.show()

print("Teste")
Pessoa = ListaPessoa("pessoas")
print("Nome: %i" % Pessoa.id[2].ordem)
sys.exit(app.exec_())

