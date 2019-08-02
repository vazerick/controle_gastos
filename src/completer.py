from PyQt5.QtWidgets import QCompleter
from PyQt5.QtCore import Qt
import pandas as pd

class Completer:

    def __init__(self, campos, tabelas, tipo):

        self.Campo = campos
        self.Tabelas = tabelas
        self.Tipo = tipo

        self.arquivo = "data/completer_"+self.Tipo+".txt"
        try:
            f = open(self.arquivo, "r")
        except:
            f = open(self.arquivo, "w+")
        self.Anterior = pd.Series(f.read().split("\n"))
        f.close()

        self.atualizar()

    def atualizar(self):

        dados = pd.Series()
        historico = self.Anterior
        dados = dados.append(self.ler())
        dados = dados.append(historico)

        # todo completer que puxe os dados anteriores, sem sobrecarregar a memória
        # for tabela in self.Tabelas:
        #     dados = dados.append(self.ler(tabela))

        if len(dados):
            for campo in self.Campo:
                completer = QCompleter(dados.str.title().unique())
                completer.setCaseSensitivity(Qt.CaseInsensitive)
                campo.setCompleter(completer)
                print(completer.completionModel())

    def ler(self):
        tabela = self.Tabelas
        if self.Tipo == "saida":
            return tabela.Saida.tabela['nome']
        if self.Tipo == "entrada":
            return tabela.Entrada.tabela['nome']
        if self.Tipo == "reserva":
            return tabela.Reserva.tabela['nome']
        if self.Tipo == "fixo":
            return tabela.Fixo.tabela['nome']


