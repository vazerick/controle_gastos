import sass
import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtCore import Qt, QDate
from PyQt5.QtWidgets import QApplication, QDialog, QMainWindow, QSplashScreen, QDesktopWidget
from ui.categorias_add import Ui_Form as CategoriasAdd
from ui.categorias_edit import Ui_Form as CategoriasEdit
from ui.dialog import Ui_Dialog as Mensagem
from ui.entrada_add import Ui_Form as EntradaAdd
from ui.fixo_add import Ui_Form as FixoAdd
from ui.gastos_add import Ui_Form as GastosAdd
from ui.gastos_edit import Ui_Form as GastosEdit
from ui.janela import Ui_Form as Main
from ui.pessoas_add import Ui_Form as PessoasAdd
from ui.pessoas_edit import Ui_Form as PessoasEdit
from ui.reserva_add import Ui_Form as ReservaAdd
from ui.reserva_edit import Ui_Form as ReservaEdit
from ui.subcategorias_add import Ui_Form as SubCategoriasAdd
from ui.subcategorias_edit import Ui_Form as SubCategoriasEdit
from ui.ajuste import Ui_Form as Ajuste
from ui.investimento import Ui_Form as Investimento
from ui.recorrentes import Ui_Form as Recorrente
from ui.gerador import Ui_Form as Gerador
from ui.relatorio import Ui_Form as Relatorio
from ui.dividir import Ui_Form as Dividir
from ui.ajustar import Ui_Form as Ajustar

class gui:

    def __init__(self):
        # declarações da interface gráfica
        print("Inicia a interface gráfica")
        self.app = QApplication(sys.argv)

        # janela principal
        print("Janela principal")
        self.wMain = QDialog()
        self.ui = Main()
        self.ui.setupUi(self.wMain)

        self.wMain.setWindowIcon(QtGui.QIcon("resources/dinheiro.png"))

        self.ui.treePessoas.setColumnWidth(0, 250)
        self.ui.treeCategorias.setColumnWidth(0, 250)

        self.ui.treeFixo.setColumnWidth(0, 250)

        print("Janelas secundárias")
        # janela para adicionar novas entradas
        self.wEntradaAdd = QDialog()
        self.uiEntradaAdd = EntradaAdd()
        self.uiEntradaAdd.setupUi(self.wEntradaAdd)

        self.wInvestimento = QDialog()
        self.uiInvestimento = Investimento()
        self.uiInvestimento.setupUi(self.wInvestimento)

        self.wInvestimentoEdit = QDialog()
        self.uiInvestimentoEdit = Investimento()
        self.uiInvestimentoEdit.setupUi(self.wInvestimentoEdit)

        self.wRecorrente = QDialog()
        self.uiRecorrente = Recorrente()
        self.uiRecorrente.setupUi(self.wRecorrente)

        self.wRecorrenteEdit = QDialog()
        self.uiRecorrenteEdit = Recorrente()
        self.uiRecorrenteEdit.setupUi(self.wRecorrenteEdit)

        # janela para relatório
        self.wRelatorio = QDialog()
        self.uiRelatorio = Relatorio()
        self.uiRelatorio.setupUi(self.wRelatorio)

        # janela para ajustes
        self.wAjuste = QDialog()
        self.uiAjuste = Ajuste()
        self.uiAjuste.setupUi(self.wAjuste)

        # janela para editar entradas
        self.wEntradaEdit = QDialog()
        self.uiEntradaEdit = EntradaAdd()
        self.uiEntradaEdit.setupUi(self.wEntradaEdit)

        # janela para adicionar novos gastos
        self.wGastosAdd = QDialog()
        self.uiGastosAdd = GastosAdd()
        self.uiGastosAdd.setupUi(self.wGastosAdd)

        # janela para editar gastos
        self.wGastosEdit = QDialog()
        self.uiGastosEdit = GastosEdit()
        self.uiGastosEdit.setupUi(self.wGastosEdit)

        # janela para converter para gastos
        self.wGastosConverte = QDialog()
        self.uiGastosConverte = GastosEdit()
        self.uiGastosConverte.setupUi(self.wGastosConverte)

        # janela para adicionar novos fixos
        self.wFixoAdd = QDialog()
        self.uiFixoAdd = FixoAdd()
        self.uiFixoAdd.setupUi(self.wFixoAdd)

        # janela para converter para fixo
        self.wFixoConverte = QDialog()
        self.uiFixoConverte = FixoAdd()
        self.uiFixoConverte.setupUi(self.wFixoConverte)

        # janela para editar fixos
        self.wFixoEdit = QDialog()
        self.uiFixoEdit = FixoAdd()
        self.uiFixoEdit.setupUi(self.wFixoEdit)

        # janela para adicionar novas reservas
        self.wReservaAdd = QDialog()
        self.uiReservaAdd = ReservaAdd()
        self.uiReservaAdd.setupUi(self.wReservaAdd)

        # janela para editar reservas
        self.wReservaEdit = QDialog()
        self.uiReservaEdit = ReservaEdit()
        self.uiReservaEdit.setupUi(self.wReservaEdit)

        # janela para adicionar novas pessoas
        self.wPessoasAdd = QDialog()
        self.uiPessoasAdd = PessoasAdd()
        self.uiPessoasAdd.setupUi(self.wPessoasAdd)

        # janela para editar pessoas
        self.wPessoasEdit = QDialog()
        self.uiPessoasEdit = PessoasEdit()
        self.uiPessoasEdit.setupUi(self.wPessoasEdit)

        # janela para adicionar novas categorias
        self.wCategoriasAdd = QDialog()
        self.uiCategoriasAdd = CategoriasAdd()
        self.uiCategoriasAdd.setupUi(self.wCategoriasAdd)

        # janela para editar categorias
        self.wCategoriasEdit = QDialog()
        self.uiCategoriasEdit = CategoriasEdit()
        self.uiCategoriasEdit.setupUi(self.wCategoriasEdit)

        # janela para adicionar novas sub-categorias
        self.altura = 250
        self.extra = 0
        self.fator = 10
        self.lista = ''

        self.wSubCategoriasAdd = QDialog()
        self.uiSubCategoriasAdd = SubCategoriasAdd()
        self.uiSubCategoriasAdd.setupUi(self.wSubCategoriasAdd)

        # janela para editar sub-categorias
        self.wSubCategoriasEdit = QDialog()
        self.uiSubCategoriasEdit = SubCategoriasEdit()
        self.uiSubCategoriasEdit.setupUi(self.wSubCategoriasEdit)

        # janela para Dividir
        self.wDividir = QDialog()
        self.uiDividir = Dividir()
        self.uiDividir.setupUi(self.wDividir)

        # janela para Ajustar
        self.wAjustar = QDialog()
        self.uiAjustar = Ajustar()
        self.uiAjustar.setupUi(self.wAjustar)

        # janela das mensagens
        self.wMensagem = QDialog()
        self.uiMensagem = Mensagem()
        self.uiMensagem.setupUi(self.wMensagem)

        # janela do gerador de novo mês
        self.wGerador = QDialog()
        self.uiGerador = Gerador()
        self.uiGerador.setupUi(self.wGerador)

        # seta a mesma configuração para todas as janelas
        print("Configura a folha de estilos")
        arquivo = open("ui/style.scss")

        self.style = arquivo.read()

        self.style = sass.compile(filename="ui/style.scss")

        arquivo.close()
        for janela in [
            self.wMain,
            self.wPessoasAdd,
            self.wPessoasEdit,
            self.wCategoriasAdd,
            self.wCategoriasEdit,
            self.wSubCategoriasAdd,
            self.wSubCategoriasEdit,
            self.wGastosAdd,
            self.wGastosEdit,
            self.wGastosConverte,
            self.wEntradaAdd,
            self.wReservaAdd,
            self.wFixoAdd,
            self.wFixoEdit,
            self.wFixoConverte,
            self.wEntradaEdit,
            self.wReservaEdit,
            self.wMensagem,
            self.wAjuste,
            self.wRecorrente,
            self.wInvestimento,
            self.wRecorrenteEdit,
            self.wInvestimentoEdit,
            self.wGerador,
            self.wRelatorio,
            self.wDividir,
            self.wAjustar
        ]:
            janela.setStyleSheet(self.style)
            janela.setWindowModality(Qt.ApplicationModal)

        # inicializa a janela
        print("Inicia a janela")
        self.wMain.show()

    def calendario_habilita(self, janela):
        pago = [
            janela.labelPago,
            janela.dateEdit_2,
            janela.botaoHoje_2
        ]
        if janela.checkPago.checkState():
            for widget in pago:
                widget.setEnabled(True)
            janela.dateEdit_2.setDate(
                janela.dateEdit.date()
            )
        else:
            for widget in pago:
                widget.setEnabled(False)
            janela.dateEdit_2.setDate(QDate.currentDate())
