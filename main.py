import sys
from PyQt5.QtWidgets import QApplication, QDialog

# interface gráfica
from src.form import Ui_Form

# classes
from src.lista import Lista, ListaPessoa, ListaCategoria
from src.link import Link

count = 0

def acao():
    global count
    count += 1
    ui.label.setText(str(count))
    print(Combo.getId())

# declarações da interface gráfica
app = QApplication(sys.argv)
window = QDialog()
ui = Ui_Form()
ui.setupUi(window)
ui.pushButton.clicked.connect(acao)

# inicializa a janela
window.show()

print("Teste")
Pessoa = ListaPessoa("pessoa")
Categoria = ListaCategoria("categoria")
ls = ["teste1", "teste2"]

Combo = Link(ui.comboBox, Pessoa)
Categoria.salva()
Pessoa.salva()

"""
árvore:
    importa QTreeWidgetItem
    
l1 = QTreeWidgetItem(["String A", "String B", "String C"])
l2 = QTreeWidgetItem(["String AA", "String BB", "String CC"])
for i in range(3):
    l1_child = QTreeWidgetItem(["Child A" + str(i), "Child B" + str(i), "Child C" + str(i)])
    l1.addChild(l1_child)

for j in range(2):
    l2_child = QTreeWidgetItem(["Child AA" + str(j), "Child BB" + str(j), "Child CC" + str(j)])
    l2.addChild(l2_child)

ui.treeWidget.addTopLevelItem(l1)
ui.treeWidget.addTopLevelItem(l2)
"""

sys.exit(app.exec_())

