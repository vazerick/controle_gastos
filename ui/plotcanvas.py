from PyQt5.QtWidgets import QSizePolicy

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np


class PlotBarra(FigureCanvas):

    def __init__(self, parent=None, width=1, height=1, dpi=75):
        self.fig = Figure(figsize=(width, height), dpi=dpi, facecolor="#C2D5E8")
        self.axes = self.fig.add_subplot(111)

        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

        self.titulo = "Título"
        self.nome_valores = "Valores"
        self.nome_rotulos = "Rotulos"

    def plot(self, x, y, destaque=[]):
        cor = "#01665E"
        cor_destaque = '#80CDC1'
        cores = []
        if len(destaque):
            i = 0
            for i in range(0, len(x)):
                if x[i] in destaque:
                    print("Destaque")
                    cores.append(cor_destaque)
                else:
                    cores.append(cor)
        else:
            cores=cor
        ax = self.fig.add_subplot(111)
        ax.clear()
        tick = 10 * round(y.max()/10)
        tick = round(tick/4)
        ax.set_yticks([tick, tick*2, tick*3, tick*4], minor=False)
        ax.yaxis.grid(True, which='major', linewidth=1)
        ax.xaxis.grid(True, linestyle="--", linewidth=0.5)
        ax.bar(x, y, color=cores)
        ax.set_facecolor("#E1EBF5")
        for tick in ax.get_xticklabels():
            tick.set_rotation(45)
        self.draw()

class PlotPizza(FigureCanvas):

    def __init__(self, parent=None, width=1, height=1, dpi=75):
        self.fig = Figure(figsize=(width, height), dpi=dpi, facecolor="#C2D5E8")
        self.axes = self.fig.add_subplot(111)

        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                QSizePolicy.Expanding,
                QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

        self.titulo = "Título"
        self.nome_valores = "Valores"
        self.nome_rotulos = "Rotulos"

        self.cores = [
            '#003C30',
            '#01665E',
            '#35978F',
            '#80CDC1',
            '#C7EAE5',
            '#F5F5F5',
            '#F6E8C3',
            '#DFC27D',
            '#BF812D',
            '#8C510A',
            '#543005'
        ]

    def func(self, pct, allvals):
        if pct >= 10:
            absolute = int(pct / 100. * np.sum(allvals))
            return "{:.1f}%\n(R${:d})".format(pct, absolute)
        else:
            return ""

    def plot(self, dados, rotulo):
        ax = self.fig.add_subplot(111)
        ax.clear()

        wedges, texts, autotexts = ax.pie(dados, autopct=lambda pct: self.func(pct, dados), pctdistance=0.7,
                                          textprops=dict(color="w"), colors=self.cores)

        ax.legend(wedges, rotulo,
                  loc="center left",
                  bbox_to_anchor=(0.8, 0, 1, 1))

        ax.axis('equal')
        self.draw()
