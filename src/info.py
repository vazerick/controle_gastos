import time
from PyQt5.QtCore import QDate, QDateTime


class Info:

    def __init__(self, config):

        self.interface = config['LAYOUT']['interface']

        self.atrasado = False

        self.tempo = QDate.currentDate()

        self.ano_int = self.tempo.year()
        self.mes_int = self.tempo.month()
        self.dia_int = self.tempo.day()

        self.inicio_dia = 4
        self.referencia = 0
        if QDateTime.currentDateTime().time().hour() > self.inicio_dia:
            self.referencia = self.dia_int
        else:
            self.referencia = self.dia_int-1

        self.ano_str = self.tempo.toString("yyyy")
        self.mes_str = self.tempo.toString("MM")
        self.dia_str = self.tempo.toString("dd")

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




