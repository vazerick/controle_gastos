import time
from PyQt5.QtCore import QDate, QDateTime


class Info:

    def __init__(self, config):

        self.interface = config['LAYOUT']['interface']
        self.atualiza()

    def atualiza(self):
        self.atrasado = False

        self.tempo = QDate.currentDate()
        print(QDate.currentDate())
        print(self.tempo)
        self.ano_int = self.tempo.year()
        self.mes_int = self.tempo.month()
        self.dia_int = self.tempo.day()

        self.inicio_dia = 0
        self.referencia = 0
        if QDateTime.currentDateTime().time().hour() >= self.inicio_dia:
            self.referencia = self.dia_int
        else:
            self.referencia = self.dia_int - 1

        self.ano_str = self.tempo.toString("yyyy")
        self.mes_str = self.tempo.toString("MM")
        self.dia_str = self.tempo.toString("dd")

        try:
            arquivo = open('data/info.txt', "r", encoding='utf-8')
            erro = arquivo.readline().split('\n')[0]
            erro = erro.split('erro:')[1]
            erro = erro.strip()
            erro = erro.replace(',', '.')
            self.erro = float(erro)
            reserva = arquivo.readline()
            reserva = reserva.split('reserva:')[1]
            reserva = reserva.strip()
            reserva = reserva.replace(',', '.')
            self.reserva = float(reserva)
            arquivo.close()
        except FileNotFoundError:
            arquivo = open('data/info.txt', "w", encoding='utf-8')
            arquivo.close()
            self.erro = 0
            self.reserva = 0
            self.salvar()

    def salvar(self):
        arquivo = open('data/info.txt', "w", encoding='utf-8')
        arquivo.write("erro: " + str(self.erro) + "\nreserva: " + str(self.reserva))


    def set_data(self, ano, mes, dia):

        self.atrasado = True

        self.tempo.setDate(ano, mes, dia)

        self.ano_int = self.tempo.year()
        self.mes_int = self.tempo.month()
        self.dia_int = self.tempo.day()

        self.ano_str = self.tempo.toString("yyyy")
        self.mes_str = self.tempo.toString("MM")
        self.dia_str = self.tempo.toString("dd")

    def data_hora(self):

        return QDateTime.currentDateTime().toString("yyyy.MM.dd-HH:mm:ss")
