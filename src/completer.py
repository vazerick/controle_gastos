from PyQt5.QtWidgets import QCompleter
from PyQt5.QtCore import Qt
import pandas as pd

class Completer:

    def __init__(self, campo_gasto, campo_entrada, tabelas):

        self.CampoGasto = campo_gasto
        self.CampoEntrada = campo_entrada
        self.Tabelas = tabelas

        self.atualizar()

    def atualizar(self):

        dados_gasto = pd.Series()
        dados_entrada = pd.Series()

        for tabela in self.Tabelas:
            dados_gasto = dados_gasto.append(tabela.Saida.tabela['nome'])
            dados_gasto = dados_gasto.append(tabela.Fixo.tabela['nome'])
            dados_gasto = dados_gasto.append(tabela.Reserva.tabela['nome'])
            dados_entrada = dados_entrada.append(tabela.Entrada.tabela['nome'])

        for campo in self.CampoGasto:
            completer = QCompleter(dados_gasto.str.title().unique())
            completer.setCaseSensitivity(Qt.CaseInsensitive)
            campo.setCompleter(completer)

        for campo in self.CampoEntrada:
            completer = QCompleter(dados_entrada.str.title().unique())
            completer.setCaseSensitivity(Qt.CaseInsensitive)
            campo.setCompleter(completer)
