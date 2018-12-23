from PyQt5.QtWidgets import QApplication, QDialog
from operator import itemgetter


class Link:

    def __init__(self, Combo, Lista, addFim=0):
        self.addFim = addFim
        self.Combo = Combo
        self.Lista = Lista
        self.ativos = sorted(self.Lista.getAtivos(), key=itemgetter('ordem'))
        for item in range(len(self.ativos)):
            self.Combo.addItem(self.ativos[item]['nome'])
        if self.addFim:
            self.Combo.addItem("Fim da lista")

    def getId(self):
        if self.Combo.currentText() == "Fim da lista":
            return -1
        else:
            return self.ativos[self.Combo.currentIndex()]['id']

    def atualiza(self):
        self.ativos = []
        self.Combo.clear()
        self.ativos = sorted(self.Lista.getAtivos(), key=itemgetter('ordem'))
        for item in range(len(self.ativos)):
            self.Combo.addItem(self.ativos[item]['nome'])
        if self.addFim:
            self.Combo.addItem("Fim da lista")


class SubcategoriaLink:

    def __init__(self, Combo, Lista, addFim=0):
        self.Combo = Combo
        self.Lista = Lista
        self.addFim = addFim
        self.ativosCat = sorted(self.Lista.getAtivos(), key=itemgetter('ordem'))
        self.ativosSub = sorted(self.Lista.subGetAtivos(self.ativosCat[0]['sub_lista'][0]['id']),
                                key=itemgetter('ordem'))
        for item in range(len(self.ativosSub)):
            self.Combo.addItem(self.ativosSub[item]['nome'])
        if self.addFim:
            self.Combo.addItem("Fim da lista")

    def getId(self):
        if self.Combo.currentText() == "Fim da lista":
            return -1
        else:
            return self.ativosSub[self.Combo.currentIndex()]['id']

    # troca a lista de subcategorias para corresponder a categoria correta
    def troca(self, cat):
        self.ativosSub = []
        self.Combo.clear()
        print(self.Lista.id[cat]['sub_lista'])
        print("Link Ativos:", self.Lista.subGetAtivos(cat))
        self.ativosSub = sorted(self.Lista.subGetAtivos(cat), key=itemgetter('ordem'))
        print(cat, self.ativosSub)
        for item in range(len(self.ativosSub)):
            self.Combo.addItem(self.ativosSub[item]['nome'])
        if self.addFim:
            self.Combo.addItem("Fim da lista")

    def reseta(self):
        self.troca(self.ativosCat[0]['id'])

    def atualiza(self):
        self.ativosCat = []
        self.ativosSub = []
        self.Combo.clear()
        self.ativosCat = sorted(self.Lista.getAtivos(), key=itemgetter('ordem'))
        self.ativosSub = sorted(self.Lista.subGetAtivos(self.ativosCat[0]['sub_lista'][0]['id']),
                                key=itemgetter('ordem'))
        for item in range(len(self.ativosSub)):
            self.Combo.addItem(self.ativosSub[item]['nome'])
        if self.addFim:
            self.Combo.addItem("Fim da lista")