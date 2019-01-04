import pandas as pd
import os
import time
from PyQt5.QtCore import QDate, QDateTime



# classe das tabelas mensais

class Tabela:

    colunas = []

    # def __init__(self):
    #

    def adicionar( #todo repensar o adicionar, agora que Mensal é uma classe filha
            self,
            nome,
            valor,
            divida,
            dividir,
            pagamento,
            categoria,
            sub,
            comentario,
            data
    ):
        adicao = QDateTime.currentDateTime().toString("yyyy.MM.dd-HH:mm:ss")
        add = pd.DataFrame(
            [[
            data,
            adicao,
            nome,
            comentario,
            valor,
            pagamento,
            categoria,
            sub,
            dividir,
            divida,
        ]],
            columns=self.colunas
        )
        self.tabela = self.tabela.append(add, ignore_index=True, sort=False)
        print(self.tabela)
        self.tabela.to_csv(self.endereco, quotechar="'", index_label='id') #todo revisar se está salvando direito


class Mensal(Tabela):

    def __init__(self, ano, mes):
        super().__init__()
        self.colunas = [
            'data', 'adicao', 'nome', 'comentario', 'valor', 'pagamento', 'categoria', 'subcategoria', 'divida', 'divisao'
        ]
        self.ano = str(ano)
        self.endereco = 'data/' + str(ano)
        # muda o mês de int M para str MM
        if mes < 10:
            self.mes = '0' + str(mes)
        else:
            self.mes = str(mes)
        self.endereco += '/' + self.mes + '.csv'
        # abre a tabela, ou cria caso não exista
        try:
            self.tabela = pd.read_csv(self.endereco, quotechar="'", index_col='id')
        except FileNotFoundError:
            self.tabela = pd.DataFrame(columns=self.colunas)
            self.tabela.to_csv(self.endereco, quotechar="'", index_label='id')
        print(self.tabela)