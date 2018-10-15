import sys
from PyQt5.QtWidgets import QApplication, QDialog

from src.lista import Lista

from src.form import Ui_Form


#declarações da interface gráfica
app = QApplication(sys.argv)
window = QDialog()
ui = Ui_Form()
ui.setupUi(window)

# inicializa a janela
#window.show()

print("Teste")
Pessoa = Lista("pessoa")
print("Nome:",Pessoa.id)
print("Nome:",Pessoa.id[0])
print("Nome:",Pessoa.id[0]['nome'])
#sys.exit(app.exec_())
