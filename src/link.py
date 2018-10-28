from PyQt5.QtWidgets import QApplication, QDialog
from operator import itemgetter

class Link:

    def __init__(self, Combo, Lista):
        self.Combo = Combo
        self.Lista = Lista
        self.ativos = sorted(self.Lista.getAtivos(), key=itemgetter('ordem'))
        for item in range(len(self.ativos)):
            self.Combo.addItem(self.ativos[item]['nome'])

    def getId(self):
        return self.ativos[self.Combo.currentIndex()]['id']

    def atualiza(self):
        self.ativos = []
        self.Combo.clear()
        self.ativos = sorted(self.Lista.getAtivos(), key=itemgetter('ordem'))
        for item in range(len(self.ativos)):
            self.Combo.addItem(self.ativos[item]['nome'])