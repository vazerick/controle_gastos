import pandas as pd
import os
from pathlib import Path


# classe das tabelas mensais

class Mensal:

    def __init__(self, ano, mes):
        self.ano = str(ano)
        self.endereco = 'data/'+str(ano)
        # cria uma pasta para o ano caso não exista
        if not os.path.exists(self.endereco):
            os.makedirs(self.endereco)
        # muda o mês de int M para str MM
        if mes < 10:
            self.mes = '0'+str(mes)
        else:
            self.mes = str(mes)
        self.endereco += '/'+self.mes+'.csv'
        # abre a tabela do mês, ou cria caso não exista
        try:
            self.tabela = pd.read_csv(self.endereco, quotechar="'", index_col='id')
        except FileNotFoundError:
            self.tabela = pd.DataFrame(columns=[
                'data', 'adicao', 'nome', 'comentario', 'valor', 'pagamento', 'categoria', 'subcategoria', 'divisao'
            ])
            self.tabela.to_csv(self.endereco, quotechar="'", index_label='id')
        print(self.tabela)
