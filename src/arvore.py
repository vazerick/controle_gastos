from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem, QApplication, QWidget

class Arvore:

    def __init__(self, Widget, Lista):
        self.Widget = Widget
        self.Lista = Lista
        self.atualiza()

    def atualiza(self):
        self.Widget.clear()
        for item in self.Lista.id:
            linha = [item['nome']]
            if item['status']:
                linha.append("Ativo")
            else:
                linha.append("Não ativo")
            WidgetItem = QTreeWidgetItem(linha)

            if 'sub_status' in item:
                if item['sub_status']:
                    for sub in item['sub_lista']:
                        child = [sub['nome']]
                        if sub['status']:
                            child.append("Ativo")
                        else:
                            child.append("Não Ativo")
                        WidgetChild = QTreeWidgetItem(child)
                        WidgetItem.addChild(WidgetChild)

            self.Widget.addTopLevelItem(WidgetItem)

