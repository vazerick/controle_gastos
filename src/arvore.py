from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem, QApplication, QWidget
import pandas


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


class ArvoreTabela:

    def __init__(self, Widget, Tabela):
        self.Widget = Widget
        self.atualiza(Tabela)


class ArvoreTabelaSaida(ArvoreTabela):

    def __init__(self, Widget, Tabela, Categoria):
        self.Categoria = Categoria
        super().__init__(Widget, Tabela)


    def atualiza(self, Tabela):
        self.Widget.clear()
        for x in range(0, len(Tabela)):
            linha = []
            linha.append(str(Tabela.iloc[x]['data']))
            linha.append(str(Tabela.iloc[x]['nome']))
            linha.append(self.Categoria.id[
                             Tabela.iloc[x]['categoria']
                         ]['nome'])
            linha.append(self.Categoria.id[
                             Tabela.iloc[x]['categoria']
                         ]['sub_lista'][
                             Tabela.iloc[x]['subcategoria']
                         ]['nome'])
            linha.append('R$'+str(Tabela.iloc[x]['valor']))
            WidgetItem = QTreeWidgetItem(linha)
            self.Widget.addTopLevelItem(WidgetItem)
        print("ADD:")
        print(Tabela)
