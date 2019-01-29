import sys
import os
import configparser
import pandas
import time
from PyQt5.QtCore import QDate, QDateTime
from PyQt5.QtGui import QIcon
# interface gráfica
from src.gui import gui

# classes
from src.lista import ListaPessoa, ListaCategoria, Pagamento
from src.link import Link, EditarLink, SubcategoriaLink
from src.arvore import *
from src.mensal import Mensal
from src.info import Info

# funções de teste


def panda():
    print("TTTT")
    if gui.ui.stackedWidget.currentIndex():
        gui.ui.stackedWidget.setCurrentIndex(0)
    else:
        gui.ui.stackedWidget.setCurrentIndex(1)

# declaração das funções

def limpa_janela(
        janela=[],
        botao=[],
        texto=[],
        spin=[],
        data=[],
        check=[],
):
    for widget in janela:
        widget.hide()
    for widget in texto:
        widget.clear()
    for widget in spin:
        widget.setValue(0)
    for widget in data:
        widget.setSelectedDate(Info.tempo)
    for widget in check:
        widget.setCheckState(0)
    for widget in botao:
        widget.setEnabled(False)


def conecta_validador(
        botao,
        texto=[],
        valor=[]
):
    observar = []
    for widget in texto:
        observar.append(widget.textChanged)
    for widget in valor:
        observar.append(widget.valueChanged)
    for item in observar:
        item.connect(
            lambda: validador(
                botao=botao,
                texto=texto,
                valor=valor
            )
        )


def validador(
        botao,
        texto=[],
        valor=[]
):
    for widget in texto:
        if vazia(widget.text()):
            botao.setEnabled(False)
            return 0
    for widget in valor:
        if widget.text() == "0,00" or widget.text() == "0":
            botao.setEnabled(False)
            return 0
    botao.setEnabled(True)

def vazia(texto):
    return not bool(texto and texto.strip())


def not_valida(input):
    for item in input:
        if vazia(item.text()):
            return 1


def tabela_existe(ano, mes):
    endereco = 'data/' + ano + '/' + mes
    if os.path.exists(endereco):
        return True
    else:
        return False

def str_mes(mes):
    if mes < 10:
        return '0' + str(mes)
    else:
        return str(mes)

# editar uma subcategoia na edição


def subcategorias_lista_click(item):
    gui.subcategorias_remove()
    gui.uiSubCategoriasAdd.inputNome.setText(item.text())
    filaSubCategorias.remove(item.text())
    print(item.text())


# atualiza os combos após atualizar a lista Categorias

#todo atualizar também a árvore de categorias
#todo adicionar um combo_sub_atualiza
def combos_categoria_atualiza():
    colecao = [
        ComboSubAdd,
        ComboSubAddCat,
        ComboCategoriaAdd,
        ComboGastoCat,
        ComboFixoCat
    ]

    for item in combos_dinamicos:
        item[0].disconnect()

    for item in colecao:
        item.atualiza()

    for item in combos_dinamicos:
        item[0].currentIndexChanged.connect(item[1])


# ações de botões


def botao_adicionar_pessoa():
    gui.wPessoasAdd.show()


def botao_adicionar_categoria():
    gui.wCategoriasAdd.show()


def botao_adicionar_sub():
    index = gui.ui.treeCategorias.currentIndex().parent().row()
    if index == -1:
        index = gui.ui.treeCategorias.currentIndex().row()
    gui.uiSubCategoriasAdd.comboCat.setCurrentIndex(index)
    gui.wSubCategoriasAdd.show()

def botao_editar_pessoa():
    index = gui.ui.treePessoas.currentIndex().row()
    if index >= 0:
        gui.uiPessoasEdit.labelTitulo.setText("Editar: "+Pessoa.id[index]['nome'])
        gui.uiPessoasEdit.inputNome.setText(Pessoa.id[index]['nome'])
        ComboPessoaEdit.atualizar()
        ComboPessoaEdit.select(index)
        gui.uiPessoasEdit.comboBox.setCurrentIndex(index)

        if Pessoa.id[index]['status']:
            gui.uiPessoasEdit.checkBox.setChecked(1)
        else:
            gui.uiPessoasEdit.checkBox.setChecked(0)

        gui.wPessoasEdit.show()


def botao_editar_pessoa_ok():
    index = gui.ui.treePessoas.currentIndex().row()
    if not_valida([gui.uiPessoasEdit.inputNome]):
        return 0
    nome = gui.uiPessoasEdit.inputNome.text()
    status = int(gui.uiPessoasEdit.checkBox.isChecked())
    combo_id = ComboPessoaEdit.getId()
    if combo_id == -1:
        ordem = len(Pessoa.id)-1
    else:
        ordem = Pessoa.id[combo_id]['ordem']
    print(status)
    Pessoa.edita(index, nome, ordem, status)
    Pessoa.salva()
    gui.wPessoasEdit.hide()

#todo gerar e adicionar os combos de categorias e subcategorias
#todo adicionar o checkbox de "Ativo"
def botao_editar_categoria():
    index = gui.ui.treeCategorias.currentIndex().row()
    pai = gui.ui.treeCategorias.currentIndex().parent().row()
    if index >= 0:
        if pai == -1:
            gui.uiCategoriasEdit.labelTitulo.setText("Editar: "+Categoria.id[index]['nome'])
            gui.uiCategoriasEdit.inputNome.setText(Categoria.id[index]['nome'])
            gui.wCategoriasEdit.show()
        else:
            gui.uiSubCategoriasEdit.labelTitulo.setText(
                "Editar: "+
                Categoria.id[pai]['nome']+
                " - "+
                Categoria.id[pai]['sub_lista'][index]['nome']
            )
            gui.uiSubCategoriasEdit.inputNome.setText(Categoria.id[pai]['sub_lista'][index]['nome'])
            gui.wSubCategoriasEdit.show()


def botao_pessoa_add():
    if not_valida([gui.uiPessoasAdd.inputNome]):
        return 0
    nome = gui.uiPessoasAdd.inputNome.text()
    combo_id = ComboPessoaAdd.getId()
    if combo_id == -1:
        ordem = len(Pessoa.id)
    else:
        ordem = Pessoa.id[combo_id]['ordem']
    Pessoa.reordena(ordem)
    Pessoa.adiciona({
        'nome': nome,
        'ordem': ordem
    })
    Pessoa.salva()
    ComboPessoaAdd.atualiza()
    ArvorePessoa.atualiza()
    gui.wPessoasAdd.hide()
    gui.uiPessoasAdd.inputNome.clear()


def botao_pessoa_cancela():
    gui.uiPessoasAdd.inputNome.setText("")
    gui.uiPessoasAdd.comboBox.setCurrentIndex(0)
    gui.wPessoasAdd.hide()


def botao_categoria_cancela():
    gui.uiCategoriasAdd.inputNome.setText("")
    gui.uiCategoriasAdd.checkBox.setChecked(0)
    gui.uiCategoriasAdd.comboBox.setCurrentIndex(0)
    gui.wCategoriasAdd.hide()


def botao_categorias_add():
    if not_valida([gui.uiCategoriasAdd.inputNome]):
        return 0
    nome = gui.uiCategoriasAdd.inputNome.text()
    combo_id = ComboCategoriaAdd.getId()
    if combo_id == -1:
        ordem = len(Categoria.id)
    else:
        ordem = Categoria.id[combo_id]['ordem']
    Categoria.reordena(ordem)
    Categoria.adiciona({
        'nome': nome,
        'ordem': ordem,
        'sub_status': 0,
        'sub_lista': ''
    })
    Categoria.salva()
    ComboCategoriaAdd.atualiza()
    ArvoreCategorias.atualiza()
    gui.wCategoriasAdd.hide()
    gui.uiCategoriasAdd.inputNome.clear()
    combos_categoria_atualiza()


filaSubCategorias = []


def botao_subcategorias_mais():
    if not_valida([gui.uiSubCategoriasAdd.inputNome]):
        return 0
    nome = gui.uiSubCategoriasAdd.inputNome.text()
    filaSubCategorias.append(nome)
    gui.subcategorias_extra(nome)
    gui.uiSubCategoriasAdd.inputNome.clear()
    del nome


def botao_subcategorias_add():
    cat = ComboSubAddCat.getId()
    combo_id = ComboSubAdd.getId()

    if combo_id == -1:
        ordem = len(Categoria.id[cat]['sub_lista'])
    else:
        ordem = Categoria.id[cat]['sub_lista'][combo_id]['ordem']

    if not_valida([gui.uiSubCategoriasAdd.inputNome]):
        if len(filaSubCategorias) == 0:
            return 0
    else:
        filaSubCategorias.append(gui.uiSubCategoriasAdd.inputNome.text())
    for nome in filaSubCategorias[::-1]:
        Categoria.reordenaSubcategoria(cat, ordem)
        Categoria.adicionaSubcategoria(cat, {
            'nome': nome,
            'ordem': ordem
        })
    filaSubCategorias.clear()
    gui.uiSubCategoriasAdd.inputNome.clear()
    gui.subcategorias_reseta()
    gui.wSubCategoriasAdd.hide()
    Categoria.salva()
    combos_categoria_atualiza()


def botao_subcategoria_cancela():
    filaSubCategorias.clear()
    gui.uiSubCategoriasAdd.inputNome.clear()
    gui.subcategorias_reseta()
    gui.wSubCategoriasAdd.hide()


def botao_adicionar_gasto():
    gui.wGastosAdd.show()


def botao_adicionar_reserva():
    gui.wReservaAdd.show()


def botao_reserva_add():
    adicao = Info.data_hora()
    nome = gui.uiReservaAdd.inputReserva.text()
    comentario = gui.uiReservaAdd.textComentario.toPlainText()
    valor = gui.uiReservaAdd.spinValor.text()

    Tabela[0].Reserva.adicionar(
        [
            adicao,
            nome,
            comentario,
            valor
        ]
    )

    limpa_janela(
        janela=[gui.wReservaAdd],
        texto=[
            gui.uiReservaAdd.inputReserva,
            gui.uiReservaAdd.textComentario
        ],
        spin=[gui.uiReservaAdd.spinValor],
        botao=[gui.uiReservaAdd.botaoOk]
    )

    # ArvoreSaida.atualiza(Tabela[0].Saida.tabela)


def botao_gasto_add(): #todo Validação de dados: impedir (alguns) campos em branco, datas do futuro e letras no valor

    data = gui.uiGastosAdd.calendarWidget.selectedDate()
    data = data.toString("dd/MM/yyyy")
    adicao = Info.data_hora()
    nome = gui.uiGastosAdd.inputGasto.text()
    comentario = gui.uiGastosAdd.textComentario.toPlainText()
    valor = gui.uiGastosAdd.spinValor.text()
    pagamento = ComboPagamento.getId()
    categoria = ComboGastoCat.getId()
    sub = ComboGastoSub.getId()
    divida = int(gui.uiGastosAdd.checkDivida.isChecked())
    dividir = int(gui.uiGastosAdd.checkDividir.isChecked())

    Tabela[0].Saida.adicionar(
        [
            data,
            adicao,
            nome,
            comentario,
            valor,
            pagamento,
            categoria,
            sub,
            None, #divida
            None, #divisao
        ]
    )

    limpa_janela(
        janela=[gui.wGastosAdd],
        texto=[
            gui.uiGastosAdd.inputGasto,
            gui.uiGastosAdd.textComentario
        ],
        data=[gui.uiGastosAdd.calendarWidget],
        spin=[gui.uiGastosAdd.spinValor],
        check=[
            gui.uiGastosAdd.checkDivida,
            gui.uiGastosAdd.checkDividir
        ],
        botao=[gui.uiGastosAdd.botaoOk]
    )

    ArvoreSaida.atualiza(Tabela[0].Saida.tabela)


def botao_adicionar_entrada():
    gui.wEntradaAdd.show()


def check_entrada():
    gui.check_calendario(gui.uiEntradaAdd)


def check_fixo():
    gui.check_calendario(gui.uiFixoAdd)


def botao_entrada_add():

    previsao = gui.uiEntradaAdd.calendarWidget.selectedDate()
    previsao = previsao.toString("dd/MM/yyyy")
    data = ""
    pago = int(gui.uiEntradaAdd.checkPago.checkState())
    if pago:
        data = gui.uiEntradaAdd.calendarWidget_2.selectedDate()
        data = data.toString("dd/MM/yyyy")
    adicao = Info.data_hora()
    nome = gui.uiEntradaAdd.inputEntrada.text()
    comentario = gui.uiEntradaAdd.textComentario.toPlainText()
    valor = gui.uiEntradaAdd.spinValor.text()

    Tabela[0].Entrada.adicionar(
        [
            data,
            previsao,
            adicao,
            nome,
            comentario,
            valor,
            pago
        ]
    )

    limpa_janela(
        janela=[gui.wEntradaAdd],
        texto=[
            gui.uiEntradaAdd.inputEntrada,
            gui.uiEntradaAdd.textComentario
        ],
        spin=[gui.uiEntradaAdd.spinValor],
        data=[
            gui.uiEntradaAdd.calendarWidget,
            gui.uiEntradaAdd.calendarWidget_2
        ],
        check=[gui.uiEntradaAdd.checkPago],
        botao=[gui.uiEntradaAdd.botaoOk]
    )


    # ArvoreSaida.atualiza(Tabela[0].Saida.tabela)


def botao_adicionar_fixo():
    gui.wFixoAdd.show()


def botao_fixo_add():

    vencimento = gui.uiFixoAdd.calendarWidget.selectedDate()
    vencimento = vencimento.toString("dd/MM/yyyy")
    data = ""
    pago = int(gui.uiFixoAdd.checkPago.checkState())
    if pago:
        data = gui.uiFixoAdd.calendarWidget_2.selectedDate()
        data = data.toString("dd/MM/yyyy")
    adicao = Info.data_hora()
    nome = gui.uiFixoAdd.inputGasto.text()
    comentario = gui.uiFixoAdd.textComentario.toPlainText()
    valor = gui.uiFixoAdd.spinValor.text()

    pagamento = 0
    categoria = 0
    subcategoria = 0

    Tabela[0].Fixo.adicionar( #todo rever  a adição para meses antigos...
        [
            data,
            vencimento,
            adicao,
            nome,
            comentario,
            valor,
            pagamento,
            categoria,
            subcategoria,
            pago
        ]
    )

    limpa_janela(
        janela=[gui.wFixoAdd],
        texto=[
            gui.uiFixoAdd.inputGasto,
            gui.uiFixoAdd.textComentario
        ],
        data=[
            gui.uiFixoAdd.calendarWidget,
            gui.uiFixoAdd.calendarWidget_2
        ],
        spin=[gui.uiFixoAdd.spinValor],
        check=[gui.uiFixoAdd.checkPago],
        botao=[gui.uiFixoAdd.botaoOk]
    )



    # ArvoreSaida.atualiza(Tabela[0].Saida.tabela)


def botao_troca_tela():
    if gui.ui.stackedWidget.currentIndex():
        gui.ui.stackedWidget.setCurrentIndex(0)
        gui.ui.botaoTela.setIcon(QIcon.fromTheme("go-next"))
    else:
        gui.ui.stackedWidget.setCurrentIndex(1)
        gui.ui.botaoTela.setIcon(QIcon.fromTheme("go-previous"))


# ações dos eventos de mudança


def troca_subcategoria(comboCat, comboSub):
    cat_id = comboCat.getId()
    comboSub.troca(cat_id)

#MAIN

# configuração


config = configparser.ConfigParser()

if os.path.exists("config.ini"):
    config.read("config.ini")
else:
    config['PAGAMENTO'] = {
        'banco': 'sim',
        'credito': 'sim',
        'vale': 'nao'
    }
    config['LAYOUT'] = {
        'interface': 'escura'
    }
    config.write(open('config.ini', 'w'))

Info = Info(config)

Pagamentos = Pagamento(config['PAGAMENTO'])

# inicia a interface gráfica
gui = gui()

# objetos de listas
Pessoa = ListaPessoa("pessoa")
Categoria = ListaCategoria("categoria")


# objetos de árvores

ArvorePessoa = Arvore(gui.ui.treePessoas, Pessoa)
ArvoreCategorias = Arvore(gui.ui.treeCategorias, Categoria)

# objetos de link de combos

# links de pessoa
ComboPessoaAdd = Link(gui.uiPessoasAdd.comboBox, Pessoa, addFim=1)
ComboPessoaEdit = EditarLink(gui.uiPessoasEdit.comboBox, Pessoa)
# links de categoria
ComboGastoCat = Link(gui.uiGastosAdd.comboCategoria, Categoria)
ComboGastoSub = SubcategoriaLink(gui.uiGastosAdd.comboSub, Categoria)
ComboCategoriaAdd = Link(gui.uiCategoriasAdd.comboBox, Categoria, addFim=1)
ComboCategoriaEdit = EditarLink(gui.uiCategoriasEdit.comboBox, Categoria)
ComboSubAddCat = Link(gui.uiSubCategoriasAdd.comboCat, Categoria)
ComboSubAdd = SubcategoriaLink(gui.uiSubCategoriasAdd.comboSub, Categoria, addFim=1)
ComboFixoCat = Link(gui.uiFixoAdd.comboCategoria, Categoria)
ComboFixoSub = SubcategoriaLink(gui.uiFixoAdd.comboSub, Categoria)

# link de pagamento
ComboPagamento = Link(gui.uiGastosAdd.comboPagamento, Pagamentos)
ComboFixoPag = Link(gui.uiFixoAdd.comboPagamento, Pagamentos)
# ações

# conecta as ações dos botões

gui.ui.botaoTela.clicked.connect(botao_troca_tela)

gui.ui.botaoGasto.clicked.connect(botao_adicionar_gasto)

gui.uiGastosAdd.botaoOk.setEnabled(False)

gui.uiGastosAdd.botaoHoje.clicked.connect(
    lambda: gui.uiGastosAdd.calendarWidget.setSelectedDate(QDate.currentDate())
)
gui.uiGastosAdd.botaoOk.clicked.connect(botao_gasto_add)

gui.ui.botaoFixo.clicked.connect(botao_adicionar_fixo)

gui.uiFixoAdd.botaoOk.clicked.connect(botao_fixo_add)

gui.uiFixoAdd.botaoHoje.clicked.connect(
    lambda: gui.uiFixoAdd.calendarWidget.setSelectedDate(QDate.currentDate())
)
gui.uiFixoAdd.botaoHoje_2.clicked.connect(
    lambda: gui.uiFixoAdd.calendarWidget_2.setSelectedDate(QDate.currentDate())
)

gui.ui.botaoEntrada.clicked.connect(botao_adicionar_entrada)

gui.uiEntradaAdd.botaoHoje.clicked.connect(
    lambda: gui.uiEntradaAdd.calendarWidget.setSelectedDate(QDate.currentDate())
)
gui.uiEntradaAdd.botaoHoje_2.clicked.connect(
    lambda: gui.uiEntradaAdd.calendarWidget_2.setSelectedDate(QDate.currentDate())
)

gui.uiEntradaAdd.botaoOk.clicked.connect(botao_entrada_add)

gui.ui.botaoReserva.clicked.connect(botao_adicionar_reserva)

gui.uiReservaAdd.botaoOk.clicked.connect(botao_reserva_add)

gui.ui.botaoCategoriaAdicionar.clicked.connect(botao_adicionar_categoria)
gui.ui.botaoPessoaAdicionar.clicked.connect(botao_adicionar_pessoa)
gui.ui.botaoSubAdicionar.clicked.connect(botao_adicionar_sub)
gui.ui.botaoPessoaEditar.clicked.connect(botao_editar_pessoa)
gui.ui.botaoCategoriaEditar.clicked.connect(botao_editar_categoria)

gui.uiPessoasAdd.botaoOk.clicked.connect(botao_pessoa_add)
gui.uiPessoasAdd.botaoCancela.clicked.connect(botao_pessoa_cancela)

gui.uiPessoasEdit.botaoOk.clicked.connect(botao_editar_pessoa_ok)
gui.uiPessoasEdit.botaoCancela.clicked.connect(gui.wPessoasEdit.hide) #todo criar uma função para o botão "cancelar"

gui.uiCategoriasAdd.botaoOk.clicked.connect(botao_categorias_add)
gui.uiCategoriasAdd.botaoCancela.clicked.connect(botao_categoria_cancela)

gui.uiSubCategoriasAdd.botaoMais.clicked.connect(botao_subcategorias_mais)
gui.uiSubCategoriasAdd.botaoOk.clicked.connect(botao_subcategorias_add)
gui.uiSubCategoriasAdd.botaoCancela.clicked.connect(botao_subcategoria_cancela)

# desliga os botoes de Ok

colecao_validacao = [
    {
        "botao": gui.uiGastosAdd.botaoOk,
        "texto": [gui.uiGastosAdd.inputGasto],
        "valor": [gui.uiGastosAdd.spinValor]
    },
    {
        "botao": gui.uiReservaAdd.botaoOk,
        "texto": [gui.uiReservaAdd.inputReserva],
        "valor": [gui.uiReservaAdd.spinValor]
    },
    {
        "botao": gui.uiFixoAdd.botaoOk,
        "texto": [gui.uiFixoAdd.inputGasto],
        "valor": [gui.uiFixoAdd.spinValor]
    },
    {
        "botao": gui.uiEntradaAdd.botaoOk,
        "texto": [gui.uiEntradaAdd.inputEntrada],
        "valor": [gui.uiEntradaAdd.spinValor]
    }
]

for item in colecao_validacao:
    item["botao"].setEnabled(False)
    conecta_validador(
        botao=item["botao"],
        texto=item["texto"],
        valor=item["valor"]
    )


# teste panda
gui.ui.pushButton.clicked.connect(panda)

# conecta as ações das trocas em check box

gui.uiEntradaAdd.checkPago.stateChanged.connect(check_entrada)

gui.uiFixoAdd.checkPago.stateChanged.connect(check_fixo)

# conecta as ações dos clicks em lista

gui.uiSubCategoriasAdd.listWidget.itemDoubleClicked.connect(subcategorias_lista_click)

# combos dinâmicos que mudam de valores conforme a seleção em combo pai

combos_dinamicos = [ #todo procurar mais combos dinamicos, como no add sub-categorias
    [
        gui.uiSubCategoriasAdd.comboCat,
        lambda: troca_subcategoria(ComboSubAddCat, ComboSubAdd)
    ],
    [
        gui.uiGastosAdd.comboCategoria,
        lambda: troca_subcategoria(ComboGastoCat, ComboGastoSub)
    ],
    [
        gui.uiFixoAdd.comboCategoria,
        lambda: troca_subcategoria(ComboFixoCat, ComboFixoSub)
    ]
]
for item in combos_dinamicos:
    item[0].currentIndexChanged.connect(item[1])

# inicia as tabelas

Tabela = []


# cria uma pasta para o ano caso não exista
if not os.path.exists('data/'+Info.ano_str):
    os.makedirs('data/'+Info.ano_str)

# confere se já tem a tabela do mês atual
if tabela_existe(Info.ano_str, Info.mes_str):
    Tabela.append(Mensal(Info.ano_int, Info.mes_int))
else:
    print("Tabelas desatualizadas")
#todo opção de iniciar o novo mês, ou de continuar no antigo

# gera as tabelas anteriores

if Info.mes_int > 1:
    ano = Info.ano_int
    mes = Info.mes_int-1
else:
    ano = Info.ano_int-1
    mes = 12
while tabela_existe(str(ano), str_mes(mes)):
    Tabela.append(Mensal(ano, mes))
    if mes == 1:
        ano -= 1
        mes = 12
    else:
        mes -= 1

for i in Tabela:
    print(i.ano)
    print(i.mes)
    print(i.Saida.endereco)
    print(i.Fixo.endereco)


# WidgetSaida = TabelaLink(gui.ui.tableSaida)
ArvoreSaida = ArvoreTabelaSaida(gui.ui.treeSaida, Tabela[0].Saida.tabela, Categoria)
ArvoreFixo = ArvoreTabelaSaida(gui.ui.treeFixo, Tabela[0].Fixo.tabela, Categoria)
ArvoreEntrada = ArvoreTabelaEntrada(gui.ui.treeEntrada, Tabela[0].Entrada.tabela)
gui.ui.botaoTela.setIcon(QIcon.fromTheme("go-next"))

for header in [
    gui.ui.treeSaida.header(),
    gui.ui.treeEntrada.header(),
    gui.ui.treeFixo.header()
]:
    header.setVisible(True)

sys.exit(gui.app.exec_())
