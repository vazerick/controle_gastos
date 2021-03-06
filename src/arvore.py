import pandas
from operator import itemgetter
from PyQt5.QtWidgets import QTreeWidget, QTreeWidgetItem, QApplication, QWidget
from PyQt5.QtCore import Qt

ligacao = [
    " De ",
    " Do ",
    " Da ",
    " Em ",
    " Com ",
    " Da "
]

class Arvore:

    def __init__(self, Widget, Lista):
        self.Widget = Widget
        self.Lista = Lista
        self.atualiza()

    def atualiza(self):
        self.Widget.clear()

        lista = sorted(self.Lista.id, key=itemgetter('nome'))

        for item in lista:
            linha = [item['nome']]
            if item['status']:
                linha.append("Ativo")
            else:
                linha.append("Não ativo")
            WidgetItem = QTreeWidgetItem(linha)

            if 'sub_status' in item:
                if item['sub_status']:
                    lista_sub = sorted(item['sub_lista'], key=itemgetter('nome'))
                    for sub in lista_sub:
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

    def formatar(self, texto):
        global ligacao

        limite = 20

        limite -= 2

        if len(texto) > limite and " " in texto:
            for palavra in ligacao:
                texto = texto.replace(palavra, "@&"+palavra.replace(" ","")+"%#")

            corte = round(len(texto)/2)
            corte = max([limite,corte])

            while " " not in texto[corte:]:
                corte -= 1
                if corte < 1:
                    break

            inicio = texto[:corte]
            fim = texto[corte:]

            fim = fim.replace(" ", "%#",1)

            texto = inicio+fim
            texto = texto.replace("%#","\n")
            texto = texto.replace("@&", " ")

        return texto

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
            linha.append(self.formatar(str(Tabela.iloc[x]['nome'])))
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

    def __init__(self, Widget, Tabela):
        super().__init__(Widget, Tabela)

    def atualiza(self, Tabela):
        self.Widget.clear()

        pessoas = Tabela["pessoa"]
        pessoas = list(set(pessoas))
        pessoas.sort()

        for pessoa in pessoas:

            Itens = Tabela[Tabela["pessoa"] == pessoa].copy()
            linha = []
            linha.append(str(pessoa))
            linha.append("R$"+str(Itens["valor"].sum()))
            ItemPai = QTreeWidgetItem(linha)

            for x in range(0, len(Itens)):
                linha = []
                linha.append(str(Itens.iloc[x]['data']))
                linha.append(Itens.iloc[x]['item'])
                comentario = Itens.iloc[x]['comentario']
                if pandas.isna(comentario):
                    comentario = ""
                linha.append(comentario)
                linha.append("R$"+str(Itens.iloc[x]['valor']))

                WidgetItem = QTreeWidgetItem(linha)

                ItemPai.addChild(WidgetItem)

            self.Widget.addTopLevelItem(ItemPai)
        self.Widget.expandAll()
        self.Widget.sortByColumn(0, Qt.AscendingOrder)
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
