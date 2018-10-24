from PyQt5.QtWidgets import QApplication, QDialog

class Link:

    def __init__(self, Combo, Lista):
        self.Combo = Combo
        self.ativos = Lista.getAtivos()
        for item in range(len(self.ativos)):
            Combo.addItem(self.ativos[item]['nome'])

    def getId(self):
        return self.ativos[self.Combo.currentIndex()]['id']