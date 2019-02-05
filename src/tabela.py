import pandas as pd
import os
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
            print(self.nome)
            print("$$$$$$:", self.tabela['valor'])
            # self.tabela['valor'].astype('float64')



    def adicionar(self, linha):
        add = pd.DataFrame(
            [linha],
            columns=self.colunas
        )
        self.tabela = self.tabela.append(add, ignore_index=True, sort=False)
        print(self.tabela)
        self.tabela.to_csv(self.endereco, quotechar="'", index_label='id') #todo revisar se está salvando direito

    def soma(self):
        return self.tabela['valor'].sum()