from PyQt5.QtWidgets import QCompleter
from PyQt5.QtCore import Qt
import pandas as pd

class Completer:

    def __init__(self, campos, tabelas, tipo):

        self.Campo = campos
        self.Tabelas = tabelas
        self.Tipo = tipo

        self.atualizar()

    def atualizar(self):

        dados = pd.Series()

        for tabela in self.Tabelas:
            dados = dados.append(self.ler(tabela))

        if len(dados):
            for campo in self.Campo:
                print(dados.str.title().unique())
                completer = QCompleter(dados.str.title().unique())
                completer.setCaseSensitivity(Qt.CaseInsensitive)
                campo.setCompleter(completer)

    def ler(self, tabela):
        if self.Tipo == "saida":
            return tabela.Saida.tabela['nome']
        if self.Tipo == "entrada":
            return tabela.Entrada.tabela['nome']
        if self.Tipo == "reserva":
            return tabela.Reserva.tabela['nome']
        if self.Tipo == "Fixo":
            return tabela.FixoSaida.tabela['nome']


