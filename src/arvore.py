import pandas
from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem, QApplication, QWidget
from PyQt5.QtCore import Qt


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


class ArvoreFilaGastos():

    def __init__(self, Widget, Lista, Categoria):
        self.Categoria = Categoria
        self.Widget = Widget
        self.Lista = Lista
        self.atualiza()

    def atualiza(self):
        self.Widget.clear()
        for item in self.Lista:
            linha = [
                item['nome'],
                self.Categoria.getNome(item['categoria']),
                self.Categoria.getSubNome(item['categoria'], item['sub']),
                "R$" + str(item['valor'])
            ]
            WidgetItem = QTreeWidgetItem(linha)
            self.Widget.addTopLevelItem(WidgetItem)
        for i in range(0, self.Widget.columnCount()):
            self.Widget.resizeColumnToContents(i)


class ArvoreTabela:

    def __init__(self, Widget, Tabela):
        self.Widget = Widget
        self.atualiza(Tabela)

    def colunas(self):
        for i in range(0, self.Widget.columnCount()):
            self.Widget.resizeColumnToContents(i)


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
            if Tabela.iloc[x]['categoria'] is not None:
                linha.append(self.Categoria.id[
                                 Tabela.iloc[x]['categoria']
                             ]['nome'])
                if self.Categoria.id[
                    Tabela.iloc[x]['categoria']
                ]['sub_status']:
                    linha.append(self.Categoria.id[
                                     Tabela.iloc[x]['categoria']
                                 ]['sub_lista'][
                                     Tabela.iloc[x]['subcategoria']
                                 ]['nome'])
                else:
                    linha.append("")
            else:
                linha.append("")
                linha.append("")
            linha.append('R$' + str(Tabela.iloc[x]['valor']))
            WidgetItem = QTreeWidgetItem(linha)
            self.Widget.addTopLevelItem(WidgetItem)
        self.colunas()


class ArvoreTabelaDividir(ArvoreTabela):

    def __init__(self, Widget, Tabela):
        super().__init__(Widget, Tabela)

    def atualiza(self, Tabela):
        self.Widget.clear()
        for x in range(0, len(Tabela)):
            linha = []
            linha.append(str(Tabela.iloc[x]['data']))
            linha.append(str(Tabela.iloc[x]['nome']))
            linha.append('R$' + str(Tabela.iloc[x]['valor']))
            WidgetItem = QTreeWidgetItem(linha)
            WidgetItem.setFlags(WidgetItem.flags() | Qt.ItemIsTristate | Qt.ItemIsUserCheckable)
            WidgetItem.setCheckState(0, Qt.Unchecked)
            self.Widget.addTopLevelItem(WidgetItem)
        self.colunas()


class ArvoreTabelaDivida(ArvoreTabela):

    def __init__(self, Widget, Tabela, Pessoas):
        Tabela["pessoa"] = Tabela.apply(lambda row: Pessoas.id[row["pessoa"]]["nome"], axis=1)
        super().__init__(Widget, Tabela)

    def atualiza(self, Tabela):
        self.Widget.clear()

        pessoas = Tabela["pessoa"]
        pessoas = list(set(pessoas))

        for pessoa in pessoas:
            Itens = Tabela[Tabela["pessoa"] == pessoa].copy()
            linha = []
            linha.append(str(pessoa))
            linha.append(str(Itens["valor"].sum()))
            ItemPai = QTreeWidgetItem(linha)

            for x in range(0, len(Itens)):
                linha = []
                linha.append(str(Itens.iloc[x]['data']))
                linha.append(str(Itens.iloc[x]['item']))
                linha.append(str(Itens.iloc[x]['comentario']))
                linha.append(str(Itens.iloc[x]['valor']))
                # data, item, comentario, valor

                # linha.append(str(Tabela.iloc[x]['nome']))
                # linha.append('R$' + str(Tabela.iloc[x]['valor']))
                WidgetItem = QTreeWidgetItem(linha)
                # WidgetItem.setFlags(WidgetItem.flags() | Qt.ItemIsTristate | Qt.ItemIsUserCheckable)
                # WidgetItem.setCheckState(0, Qt.Unchecked)
                ItemPai.addChild(WidgetItem)

            self.Widget.addTopLevelItem(ItemPai)
        self.Widget.expandAll()
        self.colunas()


class ArvoreTabelaFiltro(ArvoreTabela):

    def __init__(self, Widget, Tabela, Categoria):
        self.Categoria = Categoria
        super().__init__(Widget, Tabela)

    def atualiza(self, Tabela):
        self.Widget.clear()
        for x in range(0, len(Tabela)):
            linha = []
            linha.append(str(Tabela.iloc[x]['tipo']))
            linha.append(str(Tabela.iloc[x]['nome']))
            linha.append(str(Tabela.iloc[x]['data']))
            if Tabela.iloc[x]['categoria'] is not None:
                linha.append(self.Categoria.id[
                                 Tabela.iloc[x]['categoria']
                             ]['nome'])
                if self.Categoria.id[
                    Tabela.iloc[x]['categoria']
                ]['sub_status']:
                    linha.append(self.Categoria.id[
                                     Tabela.iloc[x]['categoria']
                                 ]['sub_lista'][
                                     Tabela.iloc[x]['subcategoria']
                                 ]['nome'])
                else:
                    linha.append("")
            else:
                linha.append("")
                linha.append("")
            linha.append('R$' + str(Tabela.iloc[x]['valor']))
            WidgetItem = QTreeWidgetItem(linha)
            self.Widget.addTopLevelItem(WidgetItem)
        self.colunas()


class ArvoreTabelaFixo(ArvoreTabelaSaida):

    def __init__(self, Widget, Tabela, Categoria):
        super().__init__(Widget, Tabela, Categoria)

    def atualiza(self, Tabela):
        self.Widget.clear()
        for x in range(0, len(Tabela)):
            linha = []
            linha.append(str(Tabela.iloc[x]['nome']))
            linha.append(str(Tabela.iloc[x]['vencimento']))
            if pandas.isna(Tabela.iloc[x]['data']):
                linha.append("")
            else:
                linha.append(str(Tabela.iloc[x]['data']))
            linha.append(self.Categoria.id[
                             Tabela.iloc[x]['categoria']
                         ]['nome'])
            if self.Categoria.id[
                Tabela.iloc[x]['categoria']
            ]['sub_status']:
                linha.append(self.Categoria.id[
                                 Tabela.iloc[x]['categoria']
                             ]['sub_lista'][
                                 Tabela.iloc[x]['subcategoria']
                             ]['nome'])
            else:
                linha.append("")
            linha.append('R$' + str(Tabela.iloc[x]['valor']))
            WidgetItem = QTreeWidgetItem(linha)
            self.Widget.addTopLevelItem(WidgetItem)
        self.colunas()


class ArvoreTabelaRecorrente(ArvoreTabelaSaida):

    def __init__(self, Widget, Tabela, Categoria):
        super().__init__(Widget, Tabela, Categoria)

    def atualiza(self, Tabela):
        self.Widget.clear()
        for x in range(0, len(Tabela)):
            linha = []
            linha.append(str(Tabela.iloc[x]['nome']))
            linha.append(str(Tabela.iloc[x]['tipo']))
            valor = Tabela.iloc[x]['valor']
            if pandas.notna(valor):
                valor = ('R$' + str(valor))
            else:
                valor = ""
            linha.append(valor)
            vencimento = Tabela.iloc[x]['vencimento']
            if pandas.notna(vencimento):
                vencimento = '{:d}'.format(int(vencimento))
            else:
                vencimento = ""
            linha.append(vencimento)
            parcelas = Tabela.iloc[x]['parcelas']
            if pandas.notna(parcelas):
                parcelas = '{:d}'.format(int(parcelas))
            else:
                parcelas = ""
            linha.append(parcelas)
            # if pandas.isna(Tabela.iloc[x]['data']):
            #     linha.append("")
            # else:
            #     linha.append(str(Tabela.iloc[x]['data']))
            linha.append(self.Categoria.id[
                             Tabela.iloc[x]['categoria']
                         ]['nome'])
            if self.Categoria.id[
                Tabela.iloc[x]['categoria']
            ]['sub_status']:
                linha.append(self.Categoria.id[
                                 Tabela.iloc[x]['categoria']
                             ]['sub_lista'][
                                 Tabela.iloc[x]['subcategoria']
                             ]['nome'])
            else:
                linha.append("")
            WidgetItem = QTreeWidgetItem(linha)
            self.Widget.addTopLevelItem(WidgetItem)
        self.colunas()

    def colunas(self):
        for i in [0,1,2,5,6]:
            self.Widget.resizeColumnToContents(i)
        for i in [3,4]:
            self.Widget.setColumnWidth(i, 75)


class ArvoreTabelaGerador(ArvoreTabelaSaida):

    def __init__(self, Widget, Tabela, Categoria):
        super().__init__(Widget, Tabela, Categoria)

    def atualiza(self, Tabela):
        self.Widget.clear()
        for x in range(0, len(Tabela)):
            linha = []
            linha.append(str(Tabela.iloc[x]['nome']))
            valor = Tabela.iloc[x]['valor']
            if pandas.notna(valor):
                valor = ('R$' + str(valor))
            else:
                valor = ""
            linha.append(valor)
            vencimento = Tabela.iloc[x]['vencimento']
            if pandas.notna(vencimento):
                vencimento = '{:d}'.format(int(vencimento))
            else:
                vencimento = ""
            linha.append(vencimento)
            parcelas = Tabela.iloc[x]['parcelas']
            if pandas.notna(parcelas):
                parcelas = '{:d}'.format(int(parcelas))
            else:
                parcelas = ""
            linha.append(parcelas)
            # if pandas.isna(Tabela.iloc[x]['data']):
            #     linha.append("")
            # else:
            #     linha.append(str(Tabela.iloc[x]['data']))
            linha.append(self.Categoria.id[
                             Tabela.iloc[x]['categoria']
                         ]['nome'])
            if self.Categoria.id[
                Tabela.iloc[x]['categoria']
            ]['sub_status']:
                linha.append(self.Categoria.id[
                                 Tabela.iloc[x]['categoria']
                             ]['sub_lista'][
                                 Tabela.iloc[x]['subcategoria']
                             ]['nome'])
            else:
                linha.append("")
            WidgetItem = QTreeWidgetItem(linha)
            self.Widget.addTopLevelItem(WidgetItem)
        self.colunas()

    def colunas(self):
        for i in [0,1,4,5]:
            self.Widget.resizeColumnToContents(i)
        for i in [1]:
            self.Widget.setColumnWidth(i, 45)
        for i in [2, 3]:
            self.Widget.setColumnWidth(i, 75)



class ArvoreTabelaEntrada(ArvoreTabela):

    def __init__(self, Widget, Tabela):
        super().__init__(Widget, Tabela)

    def atualiza(self, Tabela):
        self.Widget.clear()
        for x in range(0, len(Tabela)):
            linha = []
            linha.append(str(Tabela.iloc[x]['nome']))
            linha.append(str(Tabela.iloc[x]['previsao']))
            if pandas.isna(Tabela.iloc[x]['data']):
                linha.append("")
            else:
                linha.append(str(Tabela.iloc[x]['data']))
            linha.append('R$' + str(Tabela.iloc[x]['valor']))
            WidgetItem = QTreeWidgetItem(linha)
            self.Widget.addTopLevelItem(WidgetItem)
        self.colunas()


class ArvoreTabelaReserva(ArvoreTabela):

    def __init__(self, Widget, Tabela):
        super().__init__(Widget, Tabela)

    def atualiza(self, Tabela):
        self.Widget.clear()
        for x in range(0, len(Tabela)):
            linha = []
            linha.append(str(Tabela.iloc[x]['nome']))
            linha.append('R$' + str(Tabela.iloc[x]['valor']))
            comentario = Tabela.iloc[x]['comentario']
            if pandas.isna(comentario):
                comentario = ""
            linha.append(str(comentario))
            WidgetItem = QTreeWidgetItem(linha)
            self.Widget.addTopLevelItem(WidgetItem)
        self.colunas()


class ArvoreTabelaGeral(ArvoreTabela):

    def __init__(self, Widget, Tabela):
        self.Tabela = Tabela
        super().__init__(Widget, Tabela)

    def atualiza(self, Tabela):
        self.Widget.clear()
        for x in range(0, len(Tabela)):
            linha = []
            linha.append(str(Tabela.iloc[x]['mes']))
            linha.append('R$' + str(Tabela.iloc[x]['entrada']))
            linha.append('R$' + str(Tabela.iloc[x]['saida']))
            WidgetItem = QTreeWidgetItem(linha)
            self.Widget.addTopLevelItem(WidgetItem)
        self.colunas()
