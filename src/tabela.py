import os
import pandas as pd
import time
from PyQt5.QtCore import QDate, QDateTime


class Tabela:
    colunas = []

    def __init__(self, colunas, ano, mes, nome):

        self.colunas = colunas
        self.nome = nome

        self.endereco = 'data/' + str(ano)

        # cria uma pasta para o ano caso não exista
        if not os.path.exists(self.endereco):
            os.makedirs(self.endereco)
        # muda o mês de int M para str MM

        if type(mes) is int:
            if mes < 10:
                self.mes = '0' + str(mes)
            else:
                self.mes = str(mes)

        self.endereco += '/' + self.mes

        # cria uma pasta para o mes caso não exista
        if not os.path.exists(self.endereco):
            os.makedirs(self.endereco)

        self.endereco += '/' + self.nome + '.csv'

        # abre a tabela, ou cria caso não exista
        try:
            self.tabela = pd.read_csv(self.endereco, quotechar="'", index_col='id')
        except FileNotFoundError:
            self.tabela = pd.DataFrame(columns=self.colunas)
            self.tabela.to_csv(self.endereco, quotechar="'", index_label='id')

        if 'valor' in self.tabela.columns:
            self.tabela['valor'] = self.tabela['valor'].replace(',', '.')
            # self.tabela['valor'].astype('float64')

    def adicionar(self, linha):
        add = pd.DataFrame(
            [linha],
            columns=self.colunas
        )
        self.tabela = self.tabela.append(add, ignore_index=True, sort=False)
        self.tabela.to_csv(self.endereco, quotechar="'", index_label='id')  # todo revisar se está salvando direito

    def editar(self, id, linha, ):
        self.tabela.loc[id] = linha
        self.tabela.to_csv(self.endereco, quotechar="'", index_label='id')

    def excluir(self, id):
        self.tabela = self.tabela.drop(id)
        self.tabela.to_csv(self.endereco, quotechar="'", index_label='id')

    def adicionar_lista(self, lista, geral):
        for item in lista:
            linha = [
                geral["data"],
                geral["adicao"],
                item["nome"],
                geral["comentario"],
                item["valor"],
                geral["pagamento"],
                item["categoria"],
                item["sub"],
                geral["divida"],
                None
            ]
            add = pd.DataFrame(
                [linha],
                columns=self.colunas
            )
            self.tabela = self.tabela.append(add, ignore_index=True, sort=False)
        self.tabela.to_csv(self.endereco, quotechar="'", index_label='id')  # todo revisar se está salvando direito

    def soma(self):
        return self.tabela['valor'].sum()

    def soma_data(self, data):
        return self.tabela[self.tabela['data'] == data.toString("dd/MM/yyyy")]['valor'].sum()

    def soma_intervalo(self, data_inicio, data_fim):
        dia_inicial = data_inicio.day()
        dia_final = data_fim.day() + 1
        soma = 0
        data = QDate()
        for dia in range(dia_inicial, dia_final):  # todo e se o intervalo ocupar varios meses?
            data.setDate(data_inicio.year(), data_inicio.month(), dia)
            soma += self.soma_data(data)
        return soma

    def lista_nomes(self):
        return self.tabela['nome'].str.lower().unique()


class TabelaGeral:
    colunas = ["mes", "entrada", "saida"]

    def __init__(self, ano):

        self.endereco = 'data/' + str(ano)

        # cria uma pasta para o ano caso não exista
        if not os.path.exists(self.endereco):
            os.makedirs(self.endereco)

        self.endereco += '/geral.csv'

        # abre a tabela, ou cria caso não exista
        try:
            self.tabela = pd.read_csv(self.endereco, quotechar="'", index_col='id')
        except FileNotFoundError:
            self.tabela = pd.DataFrame(columns=self.colunas)
            self.tabela.to_csv(self.endereco, quotechar="'", index_label='id')

        self.tabela['entrada'] = self.tabela['entrada'].replace(',', '.')
        self.tabela['saida'] = self.tabela['saida'].replace(',', '.')

    def adicionar(self, linha):
        add = pd.DataFrame(
            [linha],
            columns=self.colunas
        )
        self.tabela = self.tabela.append(add, ignore_index=True, sort=False)
        self.tabela.to_csv(self.endereco, quotechar="'", index_label='id')  # todo revisar se está salvando direito


class TabelaInicia:

    colunas = []
    endereco = ""

    def __init__(self, colunas, nome):

        self.colunas = colunas
        self.nome = nome

        self.endereco = 'data/' + self.nome + '.csv'

        # abre a tabela, ou cria caso não exista
        try:
            self.tabela = pd.read_csv(self.endereco, quotechar="'", index_col='id')
        except FileNotFoundError:
            self.tabela = pd.DataFrame(columns=self.colunas)
            self.tabela.to_csv(self.endereco, quotechar="'", index_label='id')

        if 'valor' in self.tabela.columns:
            self.tabela['valor'] = self.tabela['valor'].replace(',', '.')

    def adicionar(self, linha):
        add = pd.DataFrame(
            [linha],
            columns=self.colunas
        )
        self.tabela = self.tabela.append(add, ignore_index=True, sort=False)
        self.tabela.to_csv(self.endereco, quotechar="'", index_label='id')  # todo revisar se está salvando direito

    def editar(self, id, linha, ):
        self.tabela.loc[id] = linha
        self.tabela.to_csv(self.endereco, quotechar="'", index_label='id')

    def excluir(self, id):
        self.tabela = self.tabela.drop(id)
        self.tabela.to_csv(self.endereco, quotechar="'", index_label='id')