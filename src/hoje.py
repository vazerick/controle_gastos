import calendar
import pandas as pd
from PyQt5.QtCore import Qt, QDate, QDateTime


class Hoje:
    soma_entrada = 0
    soma_saida = 0
    soma_fixo = 0
    soma_reserva = 0
    soma_hoje = 0
    soma_semana = 0
    mes_limite = 0
    mes_resta = 0
    hoje_limite = 0
    hoje_resta = 0
    media_dia = 0
    dia_limite = 0
    semana_limite = 0
    semana_resta = 0
    ajuste = 0

    def __init__(self, Tabela, Janela, Info):
        self.Tabela = Tabela
        self.Info = Info

        self.Dia = Janela.groupDia.setTitle
        self.Inicio = QDate()
        self.Inicio.setDate(self.Info.ano_int, self.Info.mes_int, 1)
        self.Referencia = QDate()
        self.Referencia.setDate(self.Info.ano_int, self.Info.mes_int, self.Info.referencia)

        self.Ontem = self.Referencia.addDays(-1)

        self.HojeGasto = Janela.labelHojeGastoV
        self.HojeLimite = Janela.labelHojeLimiteV
        self.HojeResto = Janela.labelHojeRestaV
        self.HojeBarra = Janela.progressBarHoje

        self.SemanaGasto = Janela.labelSemanaGastoV
        self.SemanaLimite = Janela.labelSemanaLimiteV
        self.SemanaResto = Janela.labelSemanaRestaV
        self.SemanaBarra = Janela.progressBarSemana

        self.MesGasto = Janela.labelMesGastoV
        self.MesLimite = Janela.labelMesLimiteV
        self.MesResto = Janela.labelMesRestaV
        self.MesBarra = Janela.progressBarMes

        self.Ajuste = Janela.labelAjuste
        self.BoxAjuste = Janela.boxAjuste
        self.LimiteDia = Janela.labelLimiteDia
        self.Media = Janela.labelMedia

        self.TotalEntrada = Janela.labelTotalEntradaV
        self.TotalFixo = Janela.labelTotalFixoV
        self.TotalReserva = Janela.labelTotalReservaV

        self.atualiza()

    def atualiza(self):  # todo o que fazer na virada da meia noite?? Quando muda o dia? Talvez costum no config?

        self.soma_saida = self.Tabela.Saida.soma()
        self.soma_entrada = self.Tabela.Entrada.soma()
        self.soma_fixo = self.Tabela.Fixo.soma()
        self.soma_reserva = self.Tabela.Reserva.soma()
        self.soma_hoje = self.Tabela.Saida.soma_data(self.Referencia)

        self.mes_limite = self.soma_entrada - self.soma_fixo - self.soma_reserva
        self.mes_resta = self.mes_limite - self.soma_saida

        dia_mes = self.Info.referencia
        dia_total = self.Info.tempo.daysInMonth()
        dia_percent = (dia_mes / dia_total) * 100
        self.Dia("Dia: " + str(dia_mes) + " de " + str(dia_total) + " (" + f'{dia_percent:.0f}' + "%)")
        if self.Referencia.day() > 1:
            self.media_dia = self.Tabela.Saida.soma_intervalo(self.Inicio, self.Ontem) / self.Ontem.day()
            dia_restante = dia_total - self.Ontem.day()
        else:
            self.media_dia = 0
            dia_restante = dia_total
        self.dia_limite = self.mes_limite / dia_total
        gasto_base = self.Tabela.Saida.soma_intervalo(self.Inicio, self.Ontem)
        self.hoje_limite = (self.mes_limite - gasto_base) / dia_restante
        self.hoje_resta = self.hoje_limite - self.soma_hoje

        self.ajuste = (self.dia_limite - self.media_dia) * self.Ontem.day()
        if self.ajuste >= 0:
            self.BoxAjuste.setTitle("Acumulado")
        else:
            self.BoxAjuste.setTitle("Excesso")

        print("Semana\n")
        calendario = calendar.monthcalendar(self.Info.ano_int, self.Info.mes_int)
        num_semanas = len(calendario)
        for i in range(0, num_semanas):
            if self.Info.dia_int in calendario[i]:
                semana_atual = calendario[i]
        ultima_semana = calendario[-1]
        print(semana_atual)
        semana_fim = QDate(self.Info.ano_int, self.Info.mes_int, max(semana_atual))
        if semana_atual[0]:
            semana_inicio = QDate(self.Info.ano_int, self.Info.mes_int, semana_atual[0])
            semana_anterior_fim = QDate(self.Info.ano_int, self.Info.mes_int, semana_atual[0]-1)
            soma_anterior = self.Tabela.Saida.soma_intervalo(self.Inicio, semana_anterior_fim)
            resta = (self.mes_limite - soma_anterior)/(dia_total-semana_anterior_fim.day())
            print(resta)
            count = 0
            while semana_atual[count] and count < 6:
                count += 1
            self.semana_limite = resta * (count+1)
        else:
            self.semana_limite = self.dia_limite * sum(1 for x in calendario[0] if x)
            semana_inicio = QDate(self.Info.ano_int, self.Info.mes_int, sorted(list(set(semana_atual)))[1])
        print(semana_inicio, semana_fim)
        self.soma_semana = self.Tabela.Saida.soma_intervalo(semana_inicio, semana_fim)
        self.semana_resta = self.semana_limite - self.soma_semana

        self.escreve_dinheiro([
            {
                'valor': self.soma_saida,
                'label': self.MesGasto
            },
            {
                'valor': self.soma_entrada,
                'label': self.TotalEntrada
            },
            {
                'valor': self.soma_fixo,
                'label': self.TotalFixo
            },
            {
                'valor': self.soma_reserva,
                'label': self.TotalReserva
            },
            {
                'valor': self.soma_hoje,
                'label': self.HojeGasto
            },
            {
                'valor': self.mes_limite,
                'label': self.MesLimite
            },
            {
                'valor': self.mes_resta,
                'label': self.MesResto
            },
            {
                'valor': self.dia_limite,
                'label': self.LimiteDia
            },
            {
                'valor': self.media_dia,
                'label': self.Media
            },
            {
                'valor': self.hoje_limite,
                'label': self.HojeLimite
            },
            {
                'valor': self.hoje_resta,
                'label': self.HojeResto
            },
            {
                'valor': self.ajuste,
                'label': self.Ajuste
            },
            {
                'valor': self.soma_semana,
                'label': self.SemanaGasto
            },
            {
                'valor': self.semana_limite,
                'label': self.SemanaLimite
            },
            {
                'valor': self.semana_resta,
                'label': self.SemanaResto
            }
        ])

        self.escreve_barra(self.MesBarra, self.soma_saida, self.mes_limite)
        self.escreve_barra(self.HojeBarra, self.soma_hoje, self.hoje_limite)
        self.escreve_barra(self.SemanaBarra, self.soma_semana, self.semana_limite)

    def escreve_dinheiro(self, itens):
        for item in itens:
            valor = "R$" + f"{item['valor']:.2f}"
            valor = valor.replace(".", ",")
            item['label'].setText(valor)

    def escreve_barra(self, barra, valor, total):
        if total == 0:
            barra.setValue(0)
        else:
            if valor > total:
                barra.setValue(100)
            else:
                barra.setValue((valor / total) * 100)
