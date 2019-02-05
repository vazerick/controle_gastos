import pandas as pd
from PyQt5.QtCore import Qt

class Hoje:

    soma_entrada = 0
    soma_saida = 0
    soma_fixo = 0
    soma_reserva = 0

    def __init__(self, Tabela, Janela, Info):
        self.Tabela = Tabela
        self.Info = Info

        self.Dia = Janela.labelDia

        self.HojeGasto = Janela.labelHojeGastoV
        self.HojeLimite = Janela.labelHojeLimiteV
        self.HojeResto = Janela.labelHojeRestaV

        self.MesGasto = Janela.labelMesGastoV
        self.MesLimite = Janela.labelMesLimiteV
        self.MesResto = Janela.labelMesRestaV

        self.Ajuste = Janela.labelAjuste
        self.LimiteDia = Janela.labelLimiteDia
        self.Media = Janela.labelMedia

        self.TotalEntrada = Janela.labelTotalEntradaV
        self.TotalFixo = Janela.labelTotalFixoV
        self.TotalReserva = Janela.labelTotalReservaV

        self.atualiza()
        

    def atualiza(self): #todo o que fazer na virada da meia noite??

        self.soma_saida = self.Tabela.Saida.soma()
        self.soma_entrada = self.Tabela.Entrada.soma()
        self.soma_fixo = self.Tabela.Fixo.soma()
        self.soma_reserva = self.Tabela.Reserva.soma()

        dia_mes = self.Info.dia_int
        dia_total = self.Info.tempo.daysInMonth()
        dia_percent = (dia_mes/dia_total)*100
        self.Dia.setText("Dia: "+str(dia_mes)+" de "+str(dia_total)+" ("+f'{dia_percent:.0f}'+"%)")



        self.escreve_dinheiro([
            {
                'valor': self.soma_saida,
                'label': self.MesGasto
            },
            {
                'valor': self.soma_entrada ,
                'label': self.TotalEntrada
            },
            {
                'valor': self.soma_fixo ,
                'label': self.TotalFixo
            },
            {
                'valor': self.soma_reserva ,
                'label': self.TotalReserva
            }
        ])

    def escreve_dinheiro(self, itens):
        for item in itens:
            valor = "R$"+f"{item['valor']:.2f}"
            valor = valor.replace(".", ",")
            item['label'].setText(valor)
