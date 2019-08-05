print("Inicia o aplicativo")
print("Importa as bibliotecas necessárias")

print("\tSistema")
import sys
import os
import configparser
import time
print("\tPandas")
import pandas as pd
import numpy as np
print("\tQt")
from PyQt5.QtCore import QDate, QDateTime, QPoint
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialogButtonBox, QMenu, QAction, QToolButton

print("\tInterfaces Gráficas")
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
from src.tabela import TabelaGeral

print("Declaração das funções")
# declaração das funções

selecionado = -1
cid = 0

Meses = [
    "",
    "Janeiro",
    "Fevereiro",
    "Março",
    "Abril",
    "Maio",
    "Junho",
    "Julho",
    "Agosto",
    "Setembro",
    "Outubro",
    "Novembro",
    "Dezembro"
]

def limpa_janela(
        janela=[],
        botao=[],
        texto=[],
        spin=[],
        data=[],
        check=[],
):
    global selecionado
    selecionado = -1
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


def gasto_atualiza():
    ArvoreSaida.atualiza(Tabela.Saida.tabela)
    Hoje.atualiza()
    grafico_mes()

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
    ArvoreReserva.atualiza(Tabela.Reserva.tabela)
    gasto_atualiza()


def botao_reserva_editar():
    adicao = Info.data_hora()
    nome = gui.uiReservaEdit.inputReserva.text()
    comentario = gui.uiReservaEdit.textComentario.toPlainText()
    valor = gui.uiReservaEdit.spinValor.value()

    Tabela.Reserva.editar(selecionado,
                             [
                                adicao,
                                nome,
                                comentario,
                                valor
                            ]
    )

    limpa_janela(
        janela=[gui.wReservaEdit],
        texto=[
            gui.uiReservaEdit.inputReserva,
            gui.uiReservaEdit.textComentario
        ],
        spin=[gui.uiReservaEdit.spinValor]
    )
    ArvoreReserva.atualiza(Tabela.Reserva.tabela)
    gasto_atualiza()


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
    gasto_atualiza()


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
    gasto_atualiza()

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
    

def botao_fixo_editar():

    vencimento = gui.uiFixoEdit.calendarWidget.selectedDate()
    vencimento = vencimento.toString("dd/MM/yyyy")
    data = ""
    pago = int(gui.uiFixoEdit.checkPago.checkState())
    if pago:
        data = gui.uiFixoEdit.calendarWidget_2.selectedDate()
        data = data.toString("dd/MM/yyyy")
    adicao = Info.data_hora()
    nome = gui.uiFixoEdit.inputGasto.text()
    comentario = gui.uiFixoEdit.textComentario.toPlainText()
    valor = gui.uiFixoEdit.spinValor.value()

    pagamento = 0
    categoria = ComboFixoEditCat.getId()
    subcategoria = ComboFixoEditSub.getId()

    Tabela.Fixo.editar( selecionado,
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
        janela=[gui.wFixoEdit],
        texto=[
            gui.uiFixoEdit.inputGasto,
            gui.uiFixoEdit.textComentario
        ],
        data=[
            gui.uiFixoEdit.calendarWidget,
            gui.uiFixoEdit.calendarWidget_2
        ],
        spin=[gui.uiFixoEdit.spinValor],
        check=[gui.uiFixoEdit.checkPago]
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
        if pd.notna(item["comentario"]):
            gui.uiGastosEdit.textComentario.setText(item["comentario"])
        gui.uiGastosEdit.calendarWidget.setSelectedDate(QDate().fromString(item["data"], "dd/MM/yyyy"))
        gui.uiGastosEdit.comboCategoria.setCurrentText(Categoria.getNome(item["categoria"]))
        gui.uiGastosEdit.comboSub.setCurrentText(Categoria.getSubNome(item["categoria"], item["subcategoria"]))
        gui.wGastosEdit.setWindowTitle("Editar "+item["nome"])
        gui.wGastosEdit.show()
    else:
        selecionado = 0


def fixo_click(item):
    item = gui.ui.treeFixo.selectedItems()[0]
    nome = item.text(0)
    vencimento = item.text(1)
    valor = float(item.text(5).replace("R$", ""))
    tabela = Tabela.Fixo.tabela
    tabela = tabela[tabela["vencimento"] == vencimento]
    tabela = tabela[tabela["nome"] == nome]
    tabela = tabela[tabela["valor"] == valor]
    global selecionado
    print(tabela["nome"])
    if len(tabela) == 1:
        id = tabela.iloc[0].name
        selecionado = id
        item = Tabela.Fixo.tabela.iloc[id]
        print(item)
        gui.uiFixoEdit.inputGasto.setText(item["nome"])
        gui.uiFixoEdit.spinValor.setValue(item["valor"])
        if pd.notna(item["comentario"]):
            gui.uiFixoEdit.textComentario.setText(item["comentario"])
        gui.uiFixoEdit.calendarWidget.setSelectedDate(QDate().fromString(item["vencimento"], "dd/MM/yyyy"))
        if item["pago"]:
            gui.uiFixoEdit.calendarWidget_2.setSelectedDate(QDate().fromString(item["data"], "dd/MM/yyyy"))
            gui.uiFixoEdit.checkPago.setCheckState(2)
        else:
            gui.uiFixoEdit.checkPago.setCheckState(0)
        gui.uiFixoEdit.comboCategoria.setCurrentText(Categoria.getNome(item["categoria"]))
        gui.uiFixoEdit.comboSub.setCurrentText(Categoria.getSubNome(item["categoria"], item["subcategoria"]))
        gui.wFixoEdit.setWindowTitle("Editar "+item["nome"])
        gui.wFixoEdit.show()
    else:
        selecionado = -1


def entrada_click(item):
    item = gui.ui.treeEntrada.selectedItems()[0]
    nome = item.text(0)
    previsao = item.text(1)
    data = item.text(2)
    valor = float(item.text(3).replace("R$", ""))
    print(nome, previsao, data, valor)
    # tabela = Tabela.Fixo.tabela
    # tabela = tabela[tabela["vencimento"] == vencimento]
    # tabela = tabela[tabela["nome"] == nome]
    # tabela = tabela[tabela["valor"] == valor]
    # global selecionado
    # print(tabela["nome"])
    # if len(tabela) == 1:
    #     id = tabela.iloc[0].name
    #     selecionado = id
    #     item = Tabela.Fixo.tabela.iloc[id]
    #     print(item)
    #     gui.uiFixoEdit.inputGasto.setText(item["nome"])
    #     gui.uiFixoEdit.spinValor.setValue(item["valor"])
    #     if pd.notna(item["comentario"]):
    #         gui.uiFixoEdit.textComentario.setText(item["comentario"])
    #     gui.uiFixoEdit.calendarWidget.setSelectedDate(QDate().fromString(item["vencimento"], "dd/MM/yyyy"))
    #     if item["pago"]:
    #         gui.uiFixoEdit.calendarWidget_2.setSelectedDate(QDate().fromString(item["data"], "dd/MM/yyyy"))
    #         gui.uiFixoEdit.checkPago.setCheckState(2)
    #     else:
    #         gui.uiFixoEdit.checkPago.setCheckState(0)
    #     gui.uiFixoEdit.comboCategoria.setCurrentText(Categoria.getNome(item["categoria"]))
    #     gui.uiFixoEdit.comboSub.setCurrentText(Categoria.getSubNome(item["categoria"], item["subcategoria"]))
    #     gui.wFixoEdit.setWindowTitle("Editar "+item["nome"])
    #     gui.wFixoEdit.show()
    # else:
    #     selecionado = -1


def reserva_click(item):
    item = gui.ui.treeReserva.selectedItems()[0]
    nome = item.text(0)
    valor = float(item.text(1).replace("R$", ""))
    comentario = item.text(2)
    tabela = Tabela.Reserva.tabela
    tabela = tabela[tabela["nome"] == nome]
    tabela = tabela[tabela["valor"] == valor]
    global selecionado
    print(tabela["nome"])
    if len(tabela) == 1:
        id = tabela.iloc[0].name
        selecionado = id
        item = Tabela.Reserva.tabela.iloc[id]
        print(item)
        gui.uiReservaEdit.inputReserva.setText(item["nome"])
        gui.uiReservaEdit.spinValor.setValue(item["valor"])
        if pd.notna(item["comentario"]):
            gui.uiReservaEdit.textComentario.setText(item["comentario"])
        gui.wReservaEdit.setWindowTitle("Editar "+item["nome"])
        gui.wReservaEdit.show()
    else:
        selecionado = -1


def fila_click(item):
    item = gui.uiGastosAdd.treeWidget.selectedItems()[0]
    nome = item.text(0)
    categoria = item.text(1)
    sub = item.text(2)
    valor = float(item.text(3).replace("R$", ""))
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


# ações dos eventos de mudança


def troca_subcategoria(comboCat, comboSub):
    cat_id = comboCat.getId()
    comboSub.troca(cat_id)


def grafico_barra(grafico, dados, completo=False, destaque=True, fatia=False, titulo=""):
    print("Gera gráfico de barras")
    dias_destaque=[]
    inicio = Info.mes_str+"/01/"+Info.ano_str
    if completo:
        periodo = Info.tempo.daysInMonth()
        datelist = pd.date_range(start=inicio, periods=periodo).strftime('%d/%m/%Y').tolist()
    else:
        fim = Info.mes_str + "/" + Info.dia_str + "/" + Info.ano_str
        datelist = pd.date_range(start=inicio, end=fim).strftime('%d/%m/%Y').tolist()
    tabela = pd.DataFrame(datelist, columns=["data"])
    tabela["valor"] = 0
    # tabela["data"] = dados["data"]
    tabela = tabela.append(dados, sort=True)
    tabela = tabela.groupby("data").agg(np.sum)
    rotulos = tabela.index.values
    i = 0
    for i in range(0, len(rotulos)):
        rotulos[i] = rotulos[i][0:2]
    if destaque:
        dias_destaque=fim_de_semana(dados)
    grafico.plot(rotulos, tabela["valor"], destaque=dias_destaque, fatia=fatia, titulo=titulo)


def grafico_linha(grafico, dados):
    print("Gera gráfico de linhas")
    # tabela = pd.DataFrame(datelist, columns=["data"])
    # tabela["valor"] = 0
    # # tabela["data"] = dados["data"]
    # tabela = tabela.append(dados, sort=True)
    # tabela = tabela.groupby("data").agg(np.sum)
    # rotulos = tabela.index.values
    # i = 0
    # for i in range(0, len(rotulos)):
    #     rotulos[i] = rotulos[i][0:2]
    # if destaque:
    #     dias_destaque=fim_de_semana(dados)
    grafico.plot(rotulos, tabela["valor"], destaque=dias_destaque, fatia=fatia, titulo=titulo)


def fim_de_semana(dados):
    dias = pd.DataFrame()
    if len(dados):
        dias["data"] = dados["data"].copy()
        dias["time"] = dias.apply(lambda row: time.strptime(row["data"], "%d/%m/%Y"), axis=1)
        dias["semana"] = dias.apply(lambda row: time.strftime("%w", row["time"]), axis=1)
        dias["data"] = dias.apply(lambda row: row["data"][0:2], axis=1)
        destaque = []
        destaque = list((dias[dias["semana"] == "5"]["data"])) + \
                   list((dias[dias["semana"] == "6"]["data"])) + \
                   list((dias[dias["semana"] == "0"]["data"]))
        return destaque
    else:
        return []

def grafico_pizza(grafico, dados):
    print("Gera gráfico de pizza")
    tabela = pd.DataFrame()
    tabela["categoria"] = dados["categoria"]
    tabela["valor"] = dados["valor"]
    tabela = tabela.groupby("categoria").agg(np.sum)
    tabela = tabela.sort_values(["valor"], ascending=False)
    rotulos = []
    for rotulo in tabela.index.values:
        nome = Categoria.getNome(rotulo)
        nome = nome.replace(" e ", "%e%")
        nome = nome.replace(" ", "\n")
        nome = nome.replace("%e%", " e\n")
        rotulos.append(nome)

    grafico.plot(tabela["valor"], rotulos)


def grafico_fatia(grafico, dados, cat):
    global cid
    id_cat = -1
    for i in Categoria.getAtivos():
        if i["nome"] == cat:
            id_cat = i["id"]
            break
    if len(Categoria.subGetAtivos(id_cat)):
        tabela = pd.DataFrame()
        tabela["categoria"] = dados["categoria"]
        tabela["subcategoria"] = dados["subcategoria"]
        tabela["valor"] = dados["valor"]
        tabela = tabela[tabela["categoria"] == id_cat]
        tabela = tabela.groupby("subcategoria").agg(np.sum)
        tabela = tabela.sort_values(["valor"], ascending=False)
        rotulos = []
        for rotulo in tabela.index.values:
            nome = Categoria.getSubNome(id_cat, rotulo)
            nome = nome.replace(" e ", "%e%")
            nome = nome.replace(" ", "\n")
            nome = nome.replace("%e%", " e\n")
            rotulos.append(nome)
        grafico.plot(tabela["valor"], rotulos, fatia=True, titulo=cat)
    grafico_barra(gui.ui.graficoBarra, dados[dados["categoria"] == id_cat], destaque=True, fatia=True, titulo=cat)
    gui.ui.graficoPizza.fig.canvas.mpl_disconnect(cid)
    cid = gui.ui.graficoPizza.fig.canvas.mpl_connect('pick_event', reseta_grafico)


def click_pizza(event):
    wedge = event.artist
    label = wedge.get_label()
    label = label.replace("\n", " ")
    grafico_fatia(gui.ui.graficoPizza, Tabela.Saida.tabela, label)


def reseta_grafico(event):
    global cid
    grafico_mes()
    gui.ui.graficoPizza.fig.canvas.mpl_disconnect(cid)
    cid = gui.ui.graficoPizza.fig.canvas.mpl_connect('pick_event', click_pizza)


def grafico_mes():
    grafico_barra(gui.ui.graficoBarra, Tabela.Saida.tabela)
    grafico_pizza(gui.ui.graficoPizza, Tabela.Saida.tabela)


def mensagem(titulo, mensagem, aceita, rejeita):
    gui.wMensagem.setWindowTitle(titulo)
    gui.uiMensagem.label.setText(mensagem)
    gui.wMensagem.show()
    gui.uiMensagem.buttonBox.accepted.disconnect()
    gui.uiMensagem.buttonBox.rejected.disconnect()
    gui.wMensagem.rejected.disconnect()
    gui.uiMensagem.buttonBox.accepted.connect(aceita)
    gui.uiMensagem.buttonBox.rejected.connect(rejeita)
    gui.wMensagem.rejected.connect(rejeita)


def m_atualiza_tabela():
    gui.wMensagem.hide()
    print(Info.tempo)
    Info.atualiza()
    print(Info.tempo)
    Geral.adicionar(
        [Meses[Info.mes_int],
        Hoje.soma_entrada,
        Hoje.soma_saida+Hoje.soma_fixo]
    )
    Tabela = Mensal(Info.ano_int, Info.mes_int)
    atualiza_completer()
    exit()

def m_rejeita_tabela():
    gui.wMensagem.hide()


def atualiza_completer():
    for completer in [
        GastoCompleter,
        EntradaCompleter,
        FixoCompleter,
        ReservaCompleter
    ]:
        completer.atualizar()
        historico = completer.Anterior
        atual = completer.ler()
        if len(historico[0]):
            novo = list(historico.append(atual).sort_values().str.title().unique())
        else:
            if atual is not None:
                novo = list(atual.sort_values())
            else:
                novo = []
        arquivo = open(completer.arquivo, "w")
        arquivo.write("\n".join(novo))
        arquivo.close()


#MAIN

# configuração


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

if Info.dia_int == 1:
    gui.ui.boxMedia.setVisible(False)
    gui.ui.boxLimiteDia.setVisible(False)
    gui.ui.boxAjuste.setVisible(False)

gui.ui.stackedWidget.setCurrentIndex(0)
gui.ui.tabWidget.setCurrentIndex(0)
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
ComboFixoEditCat = Link(gui.uiFixoEdit.comboCategoria, Categoria)
ComboFixoEditSub = SubcategoriaLink(gui.uiFixoEdit.comboSub, Categoria)

# link de pagamento
ComboPagamento = Link(gui.uiGastosAdd.comboPagamento, Pagamentos)
ComboFixoPag = Link(gui.uiFixoAdd.comboPagamento, Pagamentos)

# gui.ui.toolAdicionar.hide()
# gui.ui.botaoGasto.clicked.connect(botao_adicionar_gasto)
acao_gasto = QAction("Gasto")
acao_gasto.triggered.connect(botao_adicionar_gasto)
# gui.ui.botaoEntrada.clicked.connect(botao_adicionar_entrada)
acao_entrada = QAction("Entrada")
acao_entrada.triggered.connect(botao_adicionar_entrada)
# gui.ui.botaoFixo.clicked.connect(botao_adicionar_fixo)
acao_fixo = QAction("Fixo")
acao_fixo.triggered.connect(botao_adicionar_fixo)
# gui.ui.botaoReserva.clicked.connect(botao_adicionar_reserva)
acao_reserva = QAction("Reserva")
acao_reserva.triggered.connect(botao_adicionar_reserva)
menu = QMenu()
menu.addAction(acao_gasto)
menu.addAction(acao_entrada)
menu.addAction(acao_fixo)
menu.addAction(acao_reserva)
gui.ui.toolAdicionar.setPopupMode(QToolButton.InstantPopup)
gui.ui.toolAdicionar.setMenu(menu)

# ações

# conecta as ações dos botões



gui.uiGastosAdd.botaoHoje.clicked.connect(
    lambda: gui.uiGastosAdd.calendarWidget.setSelectedDate(QDate.currentDate())
)
gui.uiGastosAdd.buttonBox.accepted.connect(botao_gasto_add)
gui.uiGastosAdd.buttonBox.rejected.connect(botao_gasto_cancela)
gui.uiGastosAdd.botaoAdd.clicked.connect(botao_gasto_fila)

gui.uiGastosEdit.buttonBox.accepted.connect(botao_gasto_editar)

gui.uiFixoAdd.buttonBox.accepted.connect(botao_fixo_add)
gui.uiFixoEdit.buttonBox.accepted.connect(botao_fixo_editar)

gui.uiFixoAdd.botaoHoje.clicked.connect(
    lambda: gui.uiFixoAdd.calendarWidget.setSelectedDate(QDate.currentDate())
)
gui.uiFixoAdd.botaoHoje_2.clicked.connect(
    lambda: gui.uiFixoAdd.calendarWidget_2.setSelectedDate(QDate.currentDate())
)


gui.uiEntradaAdd.botaoHoje.clicked.connect(
    lambda: gui.uiEntradaAdd.calendarWidget.setSelectedDate(QDate.currentDate())
)
gui.uiEntradaAdd.botaoHoje_2.clicked.connect(
    lambda: gui.uiEntradaAdd.calendarWidget_2.setSelectedDate(QDate.currentDate())
)

gui.uiEntradaAdd.buttonBox.accepted.connect(botao_entrada_add)


gui.uiReservaAdd.buttonBox.accepted.connect(botao_reserva_add)
gui.uiReservaEdit.buttonBox.accepted.connect(botao_reserva_editar)

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

gui.uiMensagem.buttonBox.accepted.connect(print)
gui.uiMensagem.buttonBox.rejected.connect(print)
gui.wMensagem.rejected.connect(print)

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

gui.uiFixoEdit.checkPago.stateChanged.connect(lambda: gui.check_calendario(gui.uiFixoEdit))

# conecta as ações dos clicks em lista

gui.uiSubCategoriasAdd.listWidget.itemDoubleClicked.connect(subcategorias_lista_click)
gui.ui.treeSaida.doubleClicked.connect(gasto_click)
gui.ui.treeFixo.doubleClicked.connect(fixo_click)
gui.ui.treeEntrada.doubleClicked.connect(entrada_click)
gui.ui.treeReserva.doubleClicked.connect(reserva_click)

gui.uiGastosAdd.treeWidget.doubleClicked.connect(fila_click)

gui.ui.listMenu.itemClicked.connect(
    lambda: gui.ui.stackedWidget.setCurrentIndex(
        gui.ui.listMenu.currentRow()
    )
)

# conect as ações dos clicks nos gráficos

cid = gui.ui.graficoPizza.fig.canvas.mpl_connect('pick_event', click_pizza)
cid2 = gui.ui.graficoBarra.fig.canvas.mpl_connect('button_press_event', reseta_grafico)


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
    ],
    [
        gui.uiFixoEdit.comboCategoria,
        lambda: troca_subcategoria(ComboFixoEditCat, ComboFixoEditSub)
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
if tabela_existe(Info.ano_str, Info.mes_str):
    print("Carrega as tabelas do mês atual")
else:
    print("Tabelas desatualizadas")
    mensagem(
        titulo="Tabelas desatualizadas",
        mensagem="Tabelas desatualizadas\nDeseja iniciar as tabelas deste mês?\nSerá necessário reiniciar o app",
        aceita=m_atualiza_tabela,
        rejeita=m_rejeita_tabela,
    )
    while not tabela_existe(Info.ano_str, Info.mes_str):
        if Info.mes_int == 1:
            Info.set_data(Info.ano_int-1, 12, Info.dia_int)
        else:
            Info.set_data(Info.ano_int, Info.mes_int-1, Info.dia_int)
Tabela = Mensal(Info.ano_int, Info.mes_int)
Geral = TabelaGeral(Info.ano_int)

print("Preenche as árvores e tabelas da interface")
# WidgetSaida = TabelaLink(gui.ui.tableSaida)
ArvoreSaida = ArvoreTabelaSaida(gui.ui.treeSaida, Tabela.Saida.tabela, Categoria)
ArvoreFixo = ArvoreTabelaFixo(gui.ui.treeFixo, Tabela.Fixo.tabela, Categoria)
ArvoreEntrada = ArvoreTabelaEntrada(gui.ui.treeEntrada, Tabela.Entrada.tabela)
ArvoreReserva = ArvoreTabelaReserva(gui.ui.treeReserva, Tabela.Reserva.tabela)
ArvoreGeral = ArvoreTabelaGeral(gui.ui.treeAno, Geral.tabela)

for header in [
    gui.ui.treeSaida.header(),
    gui.ui.treeEntrada.header(),
    gui.ui.treeFixo.header(),
    gui.ui.treeReserva.header(),
    gui.ui.treeAno.header()
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
        gui.uiEntradaEdit.inputEntrada
    ],
    tabelas=Tabela,
    tipo="entrada"
)

FixoCompleter = Completer(
    campos=[
        gui.uiFixoAdd.inputGasto,
        gui.uiFixoEdit.inputGasto
    ],
    tabelas=Tabela,
    tipo="fixo"
)

ReservaCompleter = Completer(
    campos=[
        gui.uiReservaAdd.inputReserva,
        gui.uiReservaEdit.inputReserva
    ],
    tabelas=Tabela,
    tipo="reserva"
)

grafico_mes()
gui.ui.graficoLinha.plot(Geral.tabela)

sys.exit(gui.app.exec_())


# todo 29/07/2019: remover a "ordem" das categorias, é pura bobagem