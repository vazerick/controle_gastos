import matplotlib.ticker as ticker
import numpy as np
from PyQt5.QtWidgets import QSizePolicy
from PyQt5.QtCore import QDate, QDateTime
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class PlotBarra(FigureCanvas):

    def __init__(self, parent=None, width=1, height=1, dpi=75):
        self.fig = Figure(figsize=(width, height), dpi=dpi, facecolor="#C2D5E8")

        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

        self.titulo = "Título"
        self.nome_valores = "Valores"
        self.nome_rotulos = "Rotulos"

    def plot(self, x, y, destaque=[], fatia=False, titulo="", limite=0, media=0):
        if fatia:
            cor = "#543005"
            cor_destaque = '#BF812D'
        else:
            cor = "#01665E"
            cor_destaque = '#80CDC1'
        cores = []
        if len(destaque):
            i = 0
            for i in range(0, len(x)):
                if x[i] in destaque:
                    cores.append(cor_destaque)
                else:
                    cores.append(cor)
        else:
            cores = cor
        ax = self.fig.add_subplot(111)
        ax.clear()
        tick = 10 * round(y.max() / 10)
        tick = round(tick / 4)
        ax.set_yticks([tick, tick * 2, tick * 3, tick * 4], minor=False)
        ax.yaxis.grid(True, which='major', linewidth=1)
        ax.xaxis.grid(True, linestyle="--", linewidth=0.5)
        ax.bar(x, y, color=cores)
        ax.set_facecolor("#E1EBF5")
        ax.axhline(y=limite, zorder=0, color="#c06761", linewidth=2.5)
        ax.axhline(y=media, zorder=0, color="#4067e0", linewidth=2.5)

        if len(titulo):
            ax.set_title(titulo)

        for tick in ax.get_xticklabels():
            tick.set_rotation(75)

        self.draw()


class PlotPizza(FigureCanvas):

    def __init__(self, parent=None, width=1, height=1, dpi=75):
        self.fig = Figure(figsize=(width, height), dpi=dpi, facecolor="#C2D5E8")

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
        if pct >= 5:
            absolute = int(pct / 100. * np.sum(allvals))
            return "{:.1f}%\n(R${:d})".format(pct, absolute)
        else:
            return ""

    def plot(self, dados, rotulo, fatia=False, titulo=""):
        ax = self.fig.add_subplot(111)
        ax.clear()

        if fatia:
            cores = self.cores[::-1]
        else:
            cores = self.cores

        wedges, texts, autotexts = ax.pie(dados, autopct=lambda pct: self.func(pct, dados), pctdistance=0.8,
                                          textprops=dict(color="w"), colors=cores)

        ax.legend(wedges, rotulo,
                  loc="center left",
                  bbox_to_anchor=(0.8, 0, 1, 1))

        i = 0

        for i in range(0, len(wedges)):
            wedges[i].set_picker(True)
            wedges[i].set_label(rotulo[i])

        if len(titulo):
            ax.set_title(titulo)

        ax.axis('equal')
        self.draw()


class PlotLinha(FigureCanvas):

    def __init__(self, parent=None, width=1, height=1, dpi=75):
        self.fig = Figure(figsize=(width, height), dpi=dpi, facecolor="#C2D5E8")

        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def plot(self, tabela):
        meses = tabela["mes"].copy()
        if len(meses) > 6:
            for i in range(0, len(meses)):
                meses[i] = meses[i][:3]

        entrada = tabela["entrada"]
        saida = tabela["saida"]

        ax = self.fig.add_subplot(111)

        linha_entrada = ax.plot(meses, entrada, 'bD-')
        linha_entrada[0].set_lw(2)
        linha_saida = ax.plot(meses, saida, 'rD-')
        linha_saida[0].set_lw(2)

        ax.set_facecolor('#C2D5E8')

        formatter = ticker.FormatStrFormatter('R$%1.0f')
        ax.yaxis.set_major_formatter(formatter)

        ax.yaxis.grid(True, which='major', linewidth=1)
        ax.xaxis.grid(True, linestyle="--", linewidth=0.5)

        for label in ax.xaxis.get_ticklabels():
            label.set_rotation(10)

        self.draw()


class PlotRelatorio(FigureCanvas):

    def __init__(self, parent=None, width=1, height=1, dpi=75):
        self.fig = Figure(figsize=(width, height), dpi=dpi, facecolor="#C2D5E8")

        FigureCanvas.__init__(self, self.fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

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

    def plot(self, tabela, categorias):

        self.fig.clear()

        meses = tabela.index.copy()
        meses = meses.strftime('%m/%y')

        entrada = tabela["entrada"]
        saida = tabela["saida"]

        ax_linha = self.fig.add_subplot(313)
        ax_linha.clear()

        ax_linha.yaxis.grid(True, which='major', linewidth=1)
        ax_linha.xaxis.grid(True, linestyle="--", linewidth=0.5)

        linha_entrada = ax_linha.plot(meses, entrada, 'bD-')
        linha_entrada[0].set_lw(2)
        linha_saida = ax_linha.plot(meses, saida, 'rD-')
        linha_saida[0].set_lw(2)

        for label in ax_linha.xaxis.get_ticklabels():
            label.set_rotation(10)

        lista_categorias = list(categorias.index)
        colunas = list(tabela.columns)

        outros = list(set(colunas) - set(lista_categorias+["entrada", "saida"]))

        lista_categorias.append("outros")

        tabela["outros"] = tabela[outros].sum(axis=1)

        print("OUTROS:\n", tabela)

        tabela = tabela[lista_categorias]

        labels = []
        stack_total = []
        stack_percet = []

        for categoria in lista_categorias:
            labels.append(categoria)
            valores = list(tabela[categoria])
            stack_total.append(list(tabela[categoria]))
            for i in range(0, len(list(tabela[categoria]))):
                print(valores[i])

        y = np.vstack(stack_total)

        ax_total = self.fig.add_subplot(311)
        ax_total.clear()

        ax_total.yaxis.grid(True, which='major', linewidth=0.2)
        ax_total.xaxis.grid(True, linestyle="--", linewidth=0.1)

        ax_total.stackplot(meses, y, labels=labels, colors=self.cores)
        # ax_total.legend(loc='upper left')

        formatter = ticker.FormatStrFormatter('R$%1.0f')
        ax_linha.yaxis.set_major_formatter(formatter)
        ax_total.yaxis.set_major_formatter(formatter)

        tabela = tabela.divide(tabela.sum(axis=1), axis=0)
        print("ABV\n", tabela)
        for categoria in lista_categorias:
            stack_percet.append(list(tabela[categoria]))

        y = np.vstack(stack_percet)

        ax_perc = self.fig.add_subplot(312)
        ax_perc.clear()

        ax_perc.yaxis.grid(True, which='major', linewidth=0.2)
        ax_perc.xaxis.grid(True, linestyle="--", linewidth=0.1)

        ax_perc.stackplot(meses, y, labels=labels, colors=self.cores)

        handles, labels = ax_perc.get_legend_handles_labels()
        self.fig.legend(handles, labels, loc='upper center', ncol=4)

        # self.fig.legend(loc='upper left')

        ax_perc.yaxis.set_major_formatter(formatter)

        for grafico in [
            ax_linha,
            ax_total,
            ax_perc
        ]:
            grafico.set_facecolor('#C2D5E8')

        self.draw()
