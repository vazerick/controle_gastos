import sys
from PyQt5.QtWidgets import QApplication, QDialog

# interface gráfica
from src.form import Ui_Form

# classes
from src.lista import Lista

# declarações da interface gráfica
app = QApplication(sys.argv)
window = QDialog()
ui = Ui_Form()
ui.setupUi(window)

# inicializa a janela
# window.show()

print("Teste")
Pessoa = Lista("pessoa")
print("Nome:", Pessoa.id)
print("Nome:", Pessoa.id[0])
print("Nome:", Pessoa.id[0]['nome'])
Pessoa.salva()
# sys.exit(app.exec_())
