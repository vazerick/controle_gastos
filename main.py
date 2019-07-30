import sys
import os
import configparser
import pandas
import time
from PyQt5.QtCore import QDate, QDateTime, QPoint
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialogButtonBox

# interface gráfica
from src.gui import gui

# classes
from src.lista import ListaPessoa, ListaCategoria, Pagamento
from src.link import Link, EditarLink, SubcategoriaLink
from src.arvore import *
from src.mensal import Mensal
from src.info import Info
from src.hoje import Hoje
from src.completer import Completer

# declaração das funções

selecionado = -1

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


def validador_gastos():
    botao = gui.uiGastosAdd.buttonBox.button(QDialogButtonBox.Ok)
    texto = gui.uiGastosAdd.inputGasto.text()
    valor = gui.uiGastosAdd.spinValor.text()
    if len(fila_gasto):
        if vazia(texto) != (valor == "0,00" or valor == "0"):
            botao.setEnabled(False)
            return 0
        botao.setEnabled(True)
        return 1
    if vazia(texto):
        botao.setEnabled(False)
        return 0
    if valor == "0,00" or valor == "0":
        botao.setEnabled(False)
        return 0
    botao.setEnabled(True)
    return 1

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


def seleciona_pagina():
    gui.ui.stackedWidget.setCurrentIndex(
        gui.ui.listMenu.currentRow()
    )



def subcategorias_lista_click(item):
    gui.subcategorias_remove()
    gui.uiSubCategoriasAdd.inputNome.setText(item.text())
    filaSubCategorias.remove(item.text())


# atualiza os combos após atualizar a lista Categorias

#todo atualizar também a árvore de categorias
#todo adicionar um combo_sub_atualiza
def combos_categoria_atualiza():
    colecao = [
        ComboSubAdd,
        ComboSubAddCat,
        ComboCategoriaAdd,
        ComboGastoCat,
        ComboGastoEditCat,
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
    valor = gui.uiReservaAdd.spinValor.value()

    Tabela.Reserva.adicionar(
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
        botao=[gui.uiReservaAdd.buttonBox.button(QDialogButtonBox.Ok)]
    )

    ArvoreSaida.atualiza(Tabela.Saida.tabela)
    Hoje.atualiza()


fila_gasto = []


def botao_gasto_add(): #todo Validação de dados: impedir datas do futuro

    data = gui.uiGastosAdd.calendarWidget.selectedDate()
    data = data.toString("dd/MM/yyyy")
    adicao = Info.data_hora()
    nome = gui.uiGastosAdd.inputGasto.text()
    comentario = gui.uiGastosAdd.textComentario.toPlainText()
    valor = gui.uiGastosAdd.spinValor.value()
    pagamento = ComboPagamento.getId()
    categoria = ComboGastoCat.getId()
    sub = ComboGastoSub.getId()
    divida = int(gui.uiGastosAdd.checkDivida.isChecked())
    if len(fila_gasto):
        if not vazia(nome) and not (valor == "0,00" or valor == "0"):
            fila_gasto.append({
                'nome': nome,
                'valor': valor,
                'categoria': categoria,
                'sub': sub
            })
        Tabela.Saida.adicionar_lista(
            fila_gasto,
            {
                "data": data,
                "adicao": adicao,
                "comentario": comentario,
                "pagamento": pagamento,
                "divida": divida
            }
        )
    else:
        Tabela.Saida.adicionar(
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
            gui.uiGastosAdd.checkDivida
        ],
        botao=[gui.uiGastosAdd.buttonBox.button(QDialogButtonBox.Ok)]
    )
    fila_gasto.clear()
    ArvoreFilaGastos.atualiza()
    gui.uiGastosAdd.labelSoma.setText("R$")
    ArvoreSaida.atualiza(Tabela.Saida.tabela)
    Hoje.atualiza()


def botao_gasto_cancela():
    fila_gasto.clear()
    ArvoreFilaGastos.atualiza()
    limpa_janela(
        janela=[gui.wGastosAdd],
        texto=[
            gui.uiGastosAdd.inputGasto,
            gui.uiGastosAdd.textComentario
        ],
        data=[gui.uiGastosAdd.calendarWidget],
        spin=[gui.uiGastosAdd.spinValor],
        check=[
            gui.uiGastosAdd.checkDivida
        ],
        botao=[gui.uiGastosAdd.buttonBox.button(QDialogButtonBox.Ok)]
    )


def botao_gasto_editar():
    global selecionado
    nome = gui.uiGastosEdit.inputGasto.text()
    valor = gui.uiGastosEdit.spinValor.value()
    comentario = gui.uiGastosEdit.textComentario.toPlainText()
    data = gui.uiGastosEdit.calendarWidget.selectedDate()
    data = data.toString("dd/MM/yyyy")
    categoria = ComboGastoEditCat.getId()
    sub = ComboGastoEditSub.getId()
    adicao = Info.data_hora()
    print("Antigo\n", Tabela.Saida.tabela.iloc[selecionado])
    print("Novo\n",nome, valor, comentario, data, Categoria.getNome(categoria), Categoria.getSubNome(categoria, sub))
    Tabela.Saida.editar(selecionado,
                        [
                            data,
                            adicao,
                            nome,
                            comentario,
                            valor,
                            0,
                            categoria,
                            sub,
                            None,  # divida
                            None,  # divisao
                        ])
    limpa_janela(
        janela=[gui.wGastosEdit],
        texto=[
            gui.uiGastosEdit.inputGasto,
            gui.uiGastosEdit.textComentario],
        spin=[gui.uiGastosEdit.spinValor],
        data=[gui.uiGastosEdit.calendarWidget]
    )
    ArvoreSaida.atualiza(Tabela.Saida.tabela)
    Hoje.atualiza()


def str_dinheiro(valor):
    return "R$"+str(valor).replace(".", ",")


def botao_gasto_fila():
    nome = gui.uiGastosAdd.inputGasto.text()
    valor = gui.uiGastosAdd.spinValor.value()
    pagamento = ComboPagamento.getId()
    categoria = ComboGastoCat.getId()
    sub = ComboGastoSub.getId()

    fila_gasto.append({
        'nome': nome,
        'valor': valor,
        'categoria': categoria,
        'sub': sub
    })
    soma = 0

    for item in fila_gasto:
        soma += item["valor"]
    gui.uiGastosAdd.labelSoma.setText(str_dinheiro(soma))

    limpa_janela(
        texto=[
            gui.uiGastosAdd.inputGasto
        ],
        spin=[gui.uiGastosAdd.spinValor],
        check=[
            gui.uiGastosAdd.checkDivida
        ],
        botao=[gui.uiGastosAdd.botaoAdd]
    )
    validador_gastos()
    ArvoreFilaGastos.atualiza()


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
    valor = gui.uiEntradaAdd.spinValor.value()

    Tabela.Entrada.adicionar(
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
        botao=[gui.uiEntradaAdd.buttonBox.button(QDialogButtonBox.Ok)]
    )

    ArvoreEntrada.atualiza(Tabela.Entrada.tabela)
    Hoje.atualiza()


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
    valor = gui.uiFixoAdd.spinValor.value()

    pagamento = 0
    categoria = ComboFixoCat.getId()
    subcategoria = ComboFixoSub.getId()

    Tabela.Fixo.adicionar( #todo rever  a adição para meses antigos...
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
        botao=[gui.uiFixoAdd.buttonBox.button(QDialogButtonBox.Ok)]
    )
    ArvoreFixo.atualiza(Tabela.Fixo.tabela)
    Hoje.atualiza()


def botao_troca_tela():
    if gui.ui.stackedWidget.currentIndex():
        gui.ui.stackedWidget.setCurrentIndex(0)
        gui.ui.botaoTela.setIcon(QIcon.fromTheme("go-next"))
    else:
        gui.ui.stackedWidget.setCurrentIndex(1)
        gui.ui.botaoTela.setIcon(QIcon.fromTheme("go-previous"))


def gasto_click(item):
    item = gui.ui.treeSaida.selectedItems()[0]
    data = item.text(0)
    nome = item.text(1)
    valor = float(item.text(4).replace("R$", ""))
    print(data, nome, valor)
    tabela = Tabela.Saida.tabela
    tabela = tabela[tabela["data"] == data]
    tabela = tabela[tabela["nome"] == nome]
    tabela = tabela[tabela["valor"] == valor]
    global selecionado
    if len(tabela) == 1:
        id = tabela.iloc[0].name
        selecionado = id
        item = Tabela.Saida.tabela.iloc[id]
        gui.uiGastosEdit.inputGasto.setText(item["nome"])
        gui.uiGastosEdit.spinValor.setValue(item["valor"])
        if pandas.notna(item["comentario"]):
            gui.uiGastosEdit.textComentario.setText(item["comentario"])
        gui.uiGastosEdit.calendarWidget.setSelectedDate(QDate().fromString(item["data"], "dd/MM/yyyy"))
        print(Categoria.getNome(item["categoria"]))
        gui.uiGastosEdit.comboCategoria.setCurrentText(Categoria.getNome(item["categoria"]))
        gui.uiGastosEdit.comboSub.setCurrentText(Categoria.getSubNome(item["categoria"], item["subcategoria"]))
        gui.wGastosEdit.setWindowTitle("Editar "+item["nome"])
        gui.wGastosEdit.show()
    else:
        selecionado = 0


def fila_click(item):
    item = gui.uiGastosAdd.treeWidget.selectedItems()[0]
    print(item)
    nome = item.text(0)
    categoria = item.text(1)
    sub = item.text(2)
    valor = float(item.text(3).replace("R$", ""))
    print("fila:\n", fila_gasto)
    print("Item:\n", nome, categoria, sub, valor)
    for i in fila_gasto:
        if i["nome"] == nome and i["valor"] == valor and Categoria.getNome(
                i["categoria"]) == categoria and Categoria.getSubNome(i["categoria"], i["sub"]) == sub:
            gui.uiGastosAdd.inputGasto.setText(i["nome"])
            gui.uiGastosAdd.spinValor.setValue(i["valor"])
            gui.uiGastosAdd.comboCategoria.setCurrentText(categoria)
            gui.uiGastosAdd.comboSub.setCurrentText(sub)
            fila_gasto.remove(i)
            validador_gastos()
            ArvoreFilaGastos.atualiza()
    # tabela = Tabela.Saida.tabela
    # tabela = tabela[tabela["data"] == data]
    # tabela = tabela[tabela["nome"] == nome]
    # tabela = tabela[tabela["valor"] == valor]
    # global selecionado
    # if len(tabela) == 1:
    #     id = tabela.iloc[0].name
    #     selecionado = id
    #     item = Tabela.Saida.tabela.iloc[id]
    #     gui.uiGastosEdit.inputGasto.setText(item["nome"])
    #     gui.uiGastosEdit.spinValor.setValue(item["valor"])
    #     if pandas.notna(item["comentario"]):
    #         gui.uiGastosEdit.textComentario.setText(item["comentario"])
    #     gui.uiGastosEdit.calendarWidget.setSelectedDate(QDate().fromString(item["data"], "dd/MM/yyyy"))
    #     print(Categoria.getNome(item["categoria"]))
    #     gui.uiGastosEdit.comboCategoria.setCurrentText(Categoria.getNome(item["categoria"]))
    #     gui.uiGastosEdit.comboSub.setCurrentText(Categoria.getSubNome(item["categoria"], item["subcategoria"]))
    #     gui.wGastosEdit.setWindowTitle("Editar "+item["nome"])
    #     gui.wGastosEdit.show()
    # else:
    #     selecionado = 0


# ações dos eventos de mudança


def troca_subcategoria(comboCat, comboSub):
    cat_id = comboCat.getId()
    comboSub.troca(cat_id)

#MAIN

# configuração


print("Inicia o aplicativo de Controle de Gastos")
print("Configurações")
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

gui.ui.stackedWidget.setCurrentIndex(0)
gui.ui.listMenu.setCurrentRow(0)
# objetos de listas
print("Carrega a lista de pessoas")
Pessoa = ListaPessoa("pessoa")
print("Carrega a lista de categorias")
Categoria = ListaCategoria("categoria")


# objetos de árvores

ArvorePessoa = Arvore(gui.ui.treePessoas, Pessoa)
ArvoreCategorias = Arvore(gui.ui.treeCategorias, Categoria)

ArvoreFilaGastos = ArvoreFilaGastos(gui.uiGastosAdd.treeWidget, fila_gasto, Categoria)

# objetos de link de combos

# links de pessoa
ComboPessoaAdd = Link(gui.uiPessoasAdd.comboBox, Pessoa, addFim=1)
ComboPessoaEdit = EditarLink(gui.uiPessoasEdit.comboBox, Pessoa)
# links de categoria
ComboGastoCat = Link(gui.uiGastosAdd.comboCategoria, Categoria)
ComboGastoSub = SubcategoriaLink(gui.uiGastosAdd.comboSub, Categoria)
ComboGastoEditCat = Link(gui.uiGastosEdit.comboCategoria, Categoria)
ComboGastoEditSub = SubcategoriaLink(gui.uiGastosEdit.comboSub, Categoria)
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

gui.ui.botaoGasto.clicked.connect(botao_adicionar_gasto)

gui.uiGastosAdd.botaoHoje.clicked.connect(
    lambda: gui.uiGastosAdd.calendarWidget.setSelectedDate(QDate.currentDate())
)
gui.uiGastosAdd.buttonBox.accepted.connect(botao_gasto_add)
gui.uiGastosAdd.buttonBox.rejected.connect(botao_gasto_cancela)
gui.uiGastosAdd.botaoAdd.clicked.connect(botao_gasto_fila)

gui.uiGastosEdit.buttonBox.accepted.connect(botao_gasto_editar)

gui.ui.botaoFixo.clicked.connect(botao_adicionar_fixo)

gui.uiFixoAdd.buttonBox.accepted.connect(botao_fixo_add)

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

gui.uiEntradaAdd.buttonBox.accepted.connect(botao_entrada_add)

gui.ui.botaoReserva.clicked.connect(botao_adicionar_reserva)

gui.uiReservaAdd.buttonBox.accepted.connect(botao_reserva_add)

gui.ui.botaoCategoriaAdicionar.clicked.connect(botao_adicionar_categoria)
gui.ui.botaoPessoaAdicionar.clicked.connect(botao_adicionar_pessoa)
gui.ui.botaoSubAdicionar.clicked.connect(botao_adicionar_sub)
gui.ui.botaoPessoaEditar.clicked.connect(botao_editar_pessoa)
gui.ui.botaoCategoriaEditar.clicked.connect(botao_editar_categoria)

gui.uiPessoasAdd.buttonBox.accepted.connect(botao_pessoa_add)
gui.uiPessoasAdd.buttonBox.rejected.connect(botao_pessoa_cancela)

gui.uiPessoasEdit.buttonBox.accepted.connect(botao_editar_pessoa_ok)
gui.uiPessoasEdit.buttonBox.rejected.connect(gui.wPessoasEdit.hide) #todo criar uma função para o botão "cancelar"

gui.uiCategoriasAdd.buttonBox.accepted.connect(botao_categorias_add)
gui.uiCategoriasAdd.buttonBox.rejected.connect(botao_categoria_cancela)

gui.uiSubCategoriasAdd.botaoMais.clicked.connect(botao_subcategorias_mais)
gui.uiSubCategoriasAdd.buttonBox.accepted.connect(botao_subcategorias_add)
gui.uiSubCategoriasAdd.buttonBox.rejected.connect(botao_subcategoria_cancela)

# desliga os botoes de Ok

colecao_validacao = [
    {
        "botao": gui.uiGastosAdd.buttonBox.button(QDialogButtonBox.Ok),
        "texto": [gui.uiGastosAdd.inputGasto],
        "valor": [gui.uiGastosAdd.spinValor]
    },
    {
        "botao": gui.uiGastosAdd.botaoAdd,
        "texto": [gui.uiGastosAdd.inputGasto],
        "valor": [gui.uiGastosAdd.spinValor]
    },
    {
        "botao": gui.uiReservaAdd.buttonBox.button(QDialogButtonBox.Ok),
        "texto": [gui.uiReservaAdd.inputReserva],
        "valor": [gui.uiReservaAdd.spinValor]
    },
    {
        "botao": gui.uiFixoAdd.buttonBox.button(QDialogButtonBox.Ok),
        "texto": [gui.uiFixoAdd.inputGasto],
        "valor": [gui.uiFixoAdd.spinValor]
    },
    {
        "botao": gui.uiEntradaAdd.buttonBox.button(QDialogButtonBox.Ok),
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


# conecta as ações das trocas em check box

gui.uiEntradaAdd.checkPago.stateChanged.connect(check_entrada)

gui.uiFixoAdd.checkPago.stateChanged.connect(check_fixo)

# conecta as ações dos clicks em lista

gui.uiSubCategoriasAdd.listWidget.itemDoubleClicked.connect(subcategorias_lista_click)
gui.ui.treeSaida.doubleClicked.connect(gasto_click)

gui.uiGastosAdd.treeWidget.doubleClicked.connect(fila_click)

gui.ui.listMenu.itemClicked.connect(
    lambda: gui.ui.stackedWidget.setCurrentIndex(
        gui.ui.listMenu.currentRow()
    )
)

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
        gui.uiGastosEdit.comboCategoria,
        lambda: troca_subcategoria(ComboGastoEditCat, ComboGastoEditSub)
    ],
    [
        gui.uiFixoAdd.comboCategoria,
        lambda: troca_subcategoria(ComboFixoCat, ComboFixoSub)
    ]
]
for item in combos_dinamicos:
    item[0].currentIndexChanged.connect(item[1])

# inicia as tabelas

print("Inicia as tabelas")

Historico = []

# cria uma pasta para o ano caso não exista
if not os.path.exists('data/'+Info.ano_str):
    print("Cria pasta do ano")
    os.makedirs('data/'+Info.ano_str)

# confere se já tem a tabela do mês atual
# Info.set_data(Info.ano_int, Info.mes_int+5, Info.dia_int)
if tabela_existe(Info.ano_str, Info.mes_str):
    print("Carrega as tabelas do mês atual")
else:
    print("Tabelas desatualizadas")
    while not tabela_existe(Info.ano_str, Info.mes_str):
        if Info.mes_int == 1:
            Info.set_data(Info.ano_int-1, 12, Info.dia_int)
        else:
            Info.set_data(Info.ano_int, Info.mes_int-1, Info.dia_int)
Tabela = Mensal(Info.ano_int, Info.mes_int)
#todo opção de iniciar o novo mês, ou de continuar no antigo

# gera as tabelas anteriores
#
# if Info.mes_int > 1:
#     ano = Info.ano_int
#     mes = Info.mes_int-1
# else:
#     ano = Info.ano_int-1
#     mes = 12
# while tabela_existe(str(ano), str_mes(mes)):
#     Tabela.append(Mensal(ano, mes))
#     if mes == 1:
#         ano -= 1
#         mes = 12
#     else:
#         mes -= 1

#todo rever caso fique um mês faltando no meio, tem que ter uma forma de criar uma tabela buraco?
print("Preenche as árvores e tabelas da interface")
# WidgetSaida = TabelaLink(gui.ui.tableSaida)
ArvoreSaida = ArvoreTabelaSaida(gui.ui.treeSaida, Tabela.Saida.tabela, Categoria)
ArvoreFixo = ArvoreTabelaFixo(gui.ui.treeFixo, Tabela.Fixo.tabela, Categoria)
ArvoreEntrada = ArvoreTabelaEntrada(gui.ui.treeEntrada, Tabela.Entrada.tabela)

for header in [
    gui.ui.treeSaida.header(),
    gui.ui.treeEntrada.header(),
    gui.ui.treeFixo.header()
]:
    header.setVisible(True)



# Calculadora de gastos diários:
print("Calcula os gastos")
Hoje = Hoje(
    Tabela=Tabela,
    Janela=gui.ui,
    Info=Info
)

GastoCompleter = Completer(
    campos=[
        gui.uiGastosAdd.inputGasto,
        gui.uiGastosEdit.inputGasto
    ],
    tabelas=Tabela,
    tipo="saida"
)

EntradaCompleter = Completer(
    campos=[
        gui.uiEntradaAdd.inputEntrada,
    ],
    tabelas=Tabela,
    tipo="entrada"
)

FixoCompleter = Completer(
    campos=[
        gui.uiFixoAdd.inputGasto,
    ],
    tabelas=Tabela,
    tipo="fixo"
)

ReservaCompleter = Completer(
    campos=[
        gui.uiReservaAdd.inputReserva,
    ],
    tabelas=Tabela,
    tipo="reserva"
)


sys.exit(gui.app.exec_())


# todo 29/07/2019: remover a "ordem" das categorias, é pura bobagem