import pandas as pd
import os
import time
from PyQt5.QtCore import QDate, QDateTime

from src.tabela import Tabela


# classe das tabelas mensais

class Mensal:

    def __init__(self, ano, mes):

        self.ano = ano
        self.mes = mes

        saida_colunas = [
            'data',
            'adicao',
            'nome',
            'comentario',
            'valor',
            'pagamento',
            'categoria',
            'subcategoria',
            'divida',
            'divisao'
        ]

        fixo_colunas = [
            'data',
            'vencimento',
            'adicao',
            'nome',
            'comentario',
            'valor',
            'pagamento',
            'categoria',
            'subcategoria',
            'pago'
        ]

        entrada_colunas = [
            'data',
            'previsao',
            'adicao',
            'nome',
            'comentario',
            'valor',
            'pago'
        ]

        reserva_colunas = [
            'adicao',
            'nome',
            'comentario',
            'valor'
        ]

        self.Saida = Tabela(
            colunas=saida_colunas,
            ano=self.ano,
            mes=self.mes,
            nome='saida'
        )

        self.Entrada = Tabela(
            colunas=entrada_colunas,
            ano=self.ano,
            mes=self.mes,
            nome='entrada'
        )

        self.Fixo = Tabela(
            colunas=fixo_colunas,
            ano=self.ano,
            mes=self.mes,
            nome='fixo'
        )

        self.Reserva = Tabela(
            colunas=reserva_colunas,
            ano=self.ano,
            mes=self.mes,
            nome='reserva'
        )
