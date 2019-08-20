print("Inicia o aplicativo")
print("Importa as bibliotecas necessárias")

print("\tSistema")
import configparser
import os
import sys
import time
import pyperclip

print("\tPandas")
import pandas as pd
import numpy as np

print("\tQt")
from PyQt5.QtCore import QDate, QDateTime, QPoint, Qt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QDialogButtonBox, QMenu, QAction, QToolButton, QCompleter

print("\tInterfaces Gráficas")
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


def janela_limpa(
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
        widget.setDate(Info.tempo)
    for widget in check:
        widget.setCheckState(0)
    for widget in botao:
        widget.setEnabled(False)


def validador_conecta(
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


def gasto_validador():
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


def nao_valida(input):
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


def pagina_seleciona():
    gui.ui.stackedWidget.setCurrentIndex(
        gui.ui.listMenu.currentRow()
    )


def gasto_atualiza():
    ArvoreSaida.atualiza(Tabela.Saida.tabela)
    Hoje.atualiza()
    hoje_grafico_escreve()


def sub_list_click(item):
    gui.subcategorias_remove()
    gui.uiSubCategoriasAdd.inputNome.setText(item.text())
    filaSubCategorias.remove(item.text())


# atualiza os combos após atualizar a lista Categorias

# todo atualizar também a árvore de categorias
# todo adicionar um combo_sub_atualiza
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


def conf_botao_pessoa_add():
    gui.wPessoasAdd.show()


def conf_botao_cat_add():
    gui.wCategoriasAdd.show()


def conf_botao_sub_add():
    index = gui.ui.treeCategorias.currentIndex().parent().row()
    if index == -1:
        index = gui.ui.treeCategorias.currentIndex().row()
    gui.uiSubCategoriasAdd.comboCat.setCurrentIndex(index)
    gui.wSubCategoriasAdd.show()


def conf_botao_pessoa_editar():
    index = gui.ui.treePessoas.currentIndex().row()
    if index >= 0:
        gui.uiPessoasEdit.labelTitulo.setText("Editar: " + Pessoa.id[index]['nome'])
        gui.uiPessoasEdit.inputNome.setText(Pessoa.id[index]['nome'])
        ComboPessoaEdit.atualizar()
        ComboPessoaEdit.select(index)
        gui.uiPessoasEdit.comboBox.setCurrentIndex(index)

        if Pessoa.id[index]['status']:
            gui.uiPessoasEdit.checkBox.setChecked(1)
        else:
            gui.uiPessoasEdit.checkBox.setChecked(0)

        gui.wPessoasEdit.show()


def pessoa_botao_editar():
    index = gui.ui.treePessoas.currentIndex().row()
    if nao_valida([gui.uiPessoasEdit.inputNome]):
        return 0
    nome = gui.uiPessoasEdit.inputNome.text()
    status = int(gui.uiPessoasEdit.checkBox.isChecked())
    combo_id = ComboPessoaEdit.getId()
    if combo_id == -1:
        ordem = len(Pessoa.id) - 1
    else:
        ordem = Pessoa.id[combo_id]['ordem']
    Pessoa.edita(index, nome, ordem, status)
    Pessoa.salva()
    gui.wPessoasEdit.hide()


# todo gerar e adicionar os combos de categorias e subcategorias
# todo adicionar o checkbox de "Ativo"
def conf_botao_cat_editar():
    index = gui.ui.treeCategorias.currentIndex().row()
    pai = gui.ui.treeCategorias.currentIndex().parent().row()
    if index >= 0:
        if pai == -1:
            gui.uiCategoriasEdit.labelTitulo.setText("Editar: " + Categoria.id[index]['nome'])
            gui.uiCategoriasEdit.inputNome.setText(Categoria.id[index]['nome'])
            gui.wCategoriasEdit.show()
        else:
            gui.uiSubCategoriasEdit.labelTitulo.setText(
                "Editar: " +
                Categoria.id[pai]['nome'] +
                " - " +
                Categoria.id[pai]['sub_lista'][index]['nome']
            )
            gui.uiSubCategoriasEdit.inputNome.setText(Categoria.id[pai]['sub_lista'][index]['nome'])
            gui.wSubCategoriasEdit.show()


def pessoa_botao_add():
    if nao_valida([gui.uiPessoasAdd.inputNome]):
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


def pessoa_botao_cancela():
    gui.uiPessoasAdd.inputNome.setText("")
    gui.uiPessoasAdd.comboBox.setCurrentIndex(0)
    gui.wPessoasAdd.hide()


def cat_botao_cancela():
    gui.uiCategoriasAdd.inputNome.setText("")
    gui.uiCategoriasAdd.checkBox.setChecked(0)
    gui.uiCategoriasAdd.comboBox.setCurrentIndex(0)
    gui.wCategoriasAdd.hide()


def cat_botao_add():
    if nao_valida([gui.uiCategoriasAdd.inputNome]):
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


def sub_botao_fila():
    if nao_valida([gui.uiSubCategoriasAdd.inputNome]):
        return 0
    nome = gui.uiSubCategoriasAdd.inputNome.text()
    filaSubCategorias.append(nome)
    gui.subcategorias_extra(nome)
    gui.uiSubCategoriasAdd.inputNome.clear()
    del nome


def sub_botao_add():
    cat = ComboSubAddCat.getId()
    combo_id = ComboSubAdd.getId()

    if combo_id == -1:
        ordem = len(Categoria.id[cat]['sub_lista'])
    else:
        ordem = Categoria.id[cat]['sub_lista'][combo_id]['ordem']

    if nao_valida([gui.uiSubCategoriasAdd.inputNome]):
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


def sub_botao_cancela():
    filaSubCategorias.clear()
    gui.uiSubCategoriasAdd.inputNome.clear()
    gui.subcategorias_reseta()
    gui.wSubCategoriasAdd.hide()


def hoje_botao_gasto_add():
    gui.wGastosAdd.show()


def hoje_botao_reserva_add():
    gui.wReservaAdd.show()


def reserva_botao_add():
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

    janela_limpa(
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


def reserva_botao_editar():
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

    janela_limpa(
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


def gasto_botao_add():  # todo Validação de dados: impedir datas do futuro

    data = gui.uiGastosAdd.dateEdit.date()
    data = data.toString("dd/MM/yyyy")
    adicao = Info.data_hora()
    nome = gui.uiGastosAdd.inputGasto.text()
    comentario = gui.uiGastosAdd.textComentario.toPlainText()
    valor = gui.uiGastosAdd.spinValor.value()
    pagamento = None
    categoria = ComboGastoCat.getId()
    sub = ComboGastoSub.getId()
    divida = None
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
                None,  # divida
                None,  # divisao
            ]
        )

    janela_limpa(
        janela=[gui.wGastosAdd],
        texto=[
            gui.uiGastosAdd.inputGasto,
            gui.uiGastosAdd.textComentario
        ],
        data=[gui.uiGastosAdd.dateEdit],
        spin=[gui.uiGastosAdd.spinValor],
        botao=[gui.uiGastosAdd.buttonBox.button(QDialogButtonBox.Ok)]
    )
    fila_gasto.clear()
    ArvoreFilaGastos.atualiza()
    gui.uiGastosAdd.labelSoma.setText("R$")
    gasto_atualiza()


def gasto_botao_cancela():
    fila_gasto.clear()
    ArvoreFilaGastos.atualiza()
    janela_limpa(
        janela=[gui.wGastosAdd],
        texto=[
            gui.uiGastosAdd.inputGasto,
            gui.uiGastosAdd.textComentario
        ],
        data=[gui.uiGastosAdd.dateEdit],
        spin=[gui.uiGastosAdd.spinValor],
        botao=[gui.uiGastosAdd.buttonBox.button(QDialogButtonBox.Ok)]
    )


def gasto_botao_editar():
    global selecionado
    nome = gui.uiGastosEdit.inputGasto.text()
    valor = gui.uiGastosEdit.spinValor.value()
    comentario = gui.uiGastosEdit.textComentario.toPlainText()
    data = gui.uiGastosEdit.dateEdit.date()
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
    janela_limpa(
        janela=[gui.wGastosEdit],
        texto=[
            gui.uiGastosEdit.inputGasto,
            gui.uiGastosEdit.textComentario],
        spin=[gui.uiGastosEdit.spinValor],
        data=[gui.uiGastosEdit.dateEdit]
    )
    gasto_atualiza()


def str_dinheiro(valor):
    return "R$" + str(valor).replace(".", ",")


def gasto_botao_fila():
    nome = gui.uiGastosAdd.inputGasto.text()
    valor = gui.uiGastosAdd.spinValor.value()
    pagamento = None
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

    janela_limpa(
        texto=[
            gui.uiGastosAdd.inputGasto
        ],
        spin=[gui.uiGastosAdd.spinValor],
        botao=[gui.uiGastosAdd.botaoAdd]
    )
    gasto_validador()
    ArvoreFilaGastos.atualiza()


def hoje_botao_entrada_add():
    gui.wEntradaAdd.show()


def entrada_calendario_habilita():
    gui.calendario_habilita(gui.uiEntradaAdd)


def fixo_calendario_habilita():
    gui.calendario_habilita(gui.uiFixoAdd)


def entrada_botao_add():
    previsao = gui.uiEntradaAdd.dateEdit.date()
    previsao = previsao.toString("dd/MM/yyyy")
    data = ""
    pago = int(gui.uiEntradaAdd.checkPago.checkState())
    if pago:
        data = gui.uiEntradaAdd.dateEdit_2.date()
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

    janela_limpa(
        janela=[gui.wEntradaAdd],
        texto=[
            gui.uiEntradaAdd.inputEntrada,
            gui.uiEntradaAdd.textComentario
        ],
        spin=[gui.uiEntradaAdd.spinValor],
        data=[
            gui.uiEntradaAdd.dateEdit,
            gui.uiEntradaAdd.dateEdit_2
        ],
        check=[gui.uiEntradaAdd.checkPago],
        botao=[gui.uiEntradaAdd.buttonBox.button(QDialogButtonBox.Ok)]
    )

    ArvoreEntrada.atualiza(Tabela.Entrada.tabela)
    Hoje.atualiza()


def entrada_botao_editar():
    previsao = gui.uiEntradaEdit.dateEdit.date()
    previsao = previsao.toString("dd/MM/yyyy")
    data = ""
    pago = int(gui.uiEntradaEdit.checkPago.checkState())
    if pago:
        data = gui.uiEntradaEdit.dateEdit_2.date()
        data = data.toString("dd/MM/yyyy")
    adicao = Info.data_hora()
    nome = gui.uiEntradaEdit.inputEntrada.text()
    comentario = gui.uiEntradaEdit.textComentario.toPlainText()
    valor = gui.uiEntradaEdit.spinValor.value()

    Tabela.Entrada.editar(selecionado,
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

    janela_limpa(
        janela=[gui.wEntradaEdit],
        texto=[
            gui.uiEntradaEdit.inputEntrada,
            gui.uiEntradaEdit.textComentario
        ],
        spin=[gui.uiEntradaEdit.spinValor],
        data=[
            gui.uiEntradaEdit.dateEdit,
            gui.uiEntradaEdit.dateEdit_2
        ],
        check=[gui.uiEntradaEdit.checkPago]
    )

    ArvoreEntrada.atualiza(Tabela.Entrada.tabela)
    Hoje.atualiza()


def hoje_botao_fixo_add():
    gui.wFixoAdd.show()


def fixo_botao_add():
    vencimento = gui.uiFixoAdd.dateEdit.date()
    vencimento = vencimento.toString("dd/MM/yyyy")
    data = ""
    pago = int(gui.uiFixoAdd.checkPago.checkState())
    if pago:
        data = gui.uiFixoAdd.dateEdit_2.date()
        data = data.toString("dd/MM/yyyy")
    adicao = Info.data_hora()
    nome = gui.uiFixoAdd.inputGasto.text()
    comentario = gui.uiFixoAdd.textComentario.toPlainText()
    valor = gui.uiFixoAdd.spinValor.value()

    pagamento = 0
    categoria = ComboFixoCat.getId()
    subcategoria = ComboFixoSub.getId()

    Tabela.Fixo.adicionar(  # todo rever  a adição para meses antigos...
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

    janela_limpa(
        janela=[gui.wFixoAdd],
        texto=[
            gui.uiFixoAdd.inputGasto,
            gui.uiFixoAdd.textComentario
        ],
        data=[
            gui.uiFixoAdd.dateEdit,
            gui.uiFixoAdd.dateEdit_2
        ],
        spin=[gui.uiFixoAdd.spinValor],
        check=[gui.uiFixoAdd.checkPago],
        botao=[gui.uiFixoAdd.buttonBox.button(QDialogButtonBox.Ok)]
    )
    ArvoreFixo.atualiza(Tabela.Fixo.tabela)
    Hoje.atualiza()
    hoje_grafico_escreve()


def fixo_botao_editar():
    vencimento = gui.uiFixoEdit.dateEdit.date()
    vencimento = vencimento.toString("dd/MM/yyyy")
    data = ""
    pago = int(gui.uiFixoEdit.checkPago.checkState())
    if pago:
        data = gui.uiFixoEdit.dateEdit_2.date()
        data = data.toString("dd/MM/yyyy")
    adicao = Info.data_hora()
    nome = gui.uiFixoEdit.inputGasto.text()
    comentario = gui.uiFixoEdit.textComentario.toPlainText()
    valor = gui.uiFixoEdit.spinValor.value()

    pagamento = 0
    categoria = ComboFixoEditCat.getId()
    subcategoria = ComboFixoEditSub.getId()

    Tabela.Fixo.editar(selecionado,
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

    janela_limpa(
        janela=[gui.wFixoEdit],
        texto=[
            gui.uiFixoEdit.inputGasto,
            gui.uiFixoEdit.textComentario
        ],
        data=[
            gui.uiFixoEdit.dateEdit,
            gui.uiFixoEdit.dateEdit_2
        ],
        spin=[gui.uiFixoEdit.spinValor],
        check=[gui.uiFixoEdit.checkPago]
    )
    ArvoreFixo.atualiza(Tabela.Fixo.tabela)
    Hoje.atualiza()


def hoje_gasto_click(item):
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
        item = Tabela.Saida.tabela.loc[id]
        gui.uiGastosEdit.inputGasto.setText(item["nome"])
        gui.uiGastosEdit.spinValor.setValue(item["valor"])
        if pd.notna(item["comentario"]):
            gui.uiGastosEdit.textComentario.setText(item["comentario"])
        gui.uiGastosEdit.dateEdit.setDate(QDate().fromString(item["data"], "dd/MM/yyyy"))
        gui.uiGastosEdit.comboCategoria.setCurrentText(Categoria.getNome(item["categoria"]))
        gui.uiGastosEdit.comboSub.setCurrentText(Categoria.getSubNome(item["categoria"], item["subcategoria"]))
        gui.wGastosEdit.setWindowTitle("Editar " + item["nome"])
        gui.wGastosEdit.show()
    else:
        selecionado = 0


def hoje_botao_excluir_gasto():
    if len(gui.ui.treeSaida.selectedItems()):
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
            item = Tabela.Saida.tabela.loc[id]
            mensagem(
                titulo="Excluir " + nome,
                mensagem="Deseja excluir " + nome + "?",
                aceita=lambda: mensagem_excluir_aceita(lambda: Tabela.Saida.excluir(id)),
                rejeita=mensagem_excluir_rejeita
            )
        else:
            selecionado = 0


def hoje_fixo_click(item):
    item = gui.ui.treeFixo.selectedItems()[0]
    nome = item.text(0)
    vencimento = item.text(1)
    valor = float(item.text(5).replace("R$", ""))
    tabela = Tabela.Fixo.tabela
    tabela = tabela[tabela["vencimento"] == vencimento]
    tabela = tabela[tabela["nome"] == nome]
    tabela = tabela[tabela["valor"] == valor]
    global selecionado
    if len(tabela) == 1:
        id = tabela.iloc[0].name
        selecionado = id
        item = Tabela.Fixo.tabela.loc[id]
        gui.uiFixoEdit.inputGasto.setText(item["nome"])
        gui.uiFixoEdit.spinValor.setValue(item["valor"])
        if pd.notna(item["comentario"]):
            gui.uiFixoEdit.textComentario.setText(item["comentario"])
        gui.uiFixoEdit.dateEdit.setDate(QDate().fromString(item["vencimento"], "dd/MM/yyyy"))
        if item["pago"]:
            gui.uiFixoEdit.checkPago.setCheckState(2)
            gui.uiFixoEdit.dateEdit_2.setDate(QDate().fromString(item["data"], "dd/MM/yyyy"))
        else:
            gui.uiFixoEdit.checkPago.setCheckState(0)
        gui.uiFixoEdit.comboCategoria.setCurrentText(Categoria.getNome(item["categoria"]))
        gui.uiFixoEdit.comboSub.setCurrentText(Categoria.getSubNome(item["categoria"], item["subcategoria"]))
        gui.wFixoEdit.setWindowTitle("Editar " + item["nome"])
        gui.wFixoEdit.show()
    else:
        selecionado = -1


def hoje_botao_excluir_fixo():
    if len(gui.ui.treeFixo.selectedItems()):
        item = gui.ui.treeFixo.selectedItems()[0]
        nome = item.text(0)
        vencimento = item.text(1)
        valor = float(item.text(5).replace("R$", ""))
        tabela = Tabela.Fixo.tabela
        tabela = tabela[tabela["vencimento"] == vencimento]
        tabela = tabela[tabela["nome"] == nome]
        tabela = tabela[tabela["valor"] == valor]
        global selecionado
        if len(tabela) == 1:
            id = tabela.iloc[0].name
            selecionado = id
            item = Tabela.Fixo.tabela.loc[id]
            mensagem(
                titulo="Excluir " + nome,
                mensagem="Deseja excluir " + nome + "?",
                aceita=lambda: mensagem_excluir_aceita(lambda: Tabela.Fixo.excluir(id)),
                rejeita=mensagem_excluir_rejeita
            )
        else:
            selecionado = -1


def hoje_botao_excluir_entrada():
    if len(gui.ui.treeEntrada.selectedItems()):
        item = gui.ui.treeEntrada.selectedItems()[0]
        nome = item.text(0)
        previsao = item.text(1)
        data = item.text(2)
        valor = float(item.text(3).replace("R$", ""))
        tabela = Tabela.Entrada.tabela
        tabela = tabela[tabela["nome"] == nome]
        tabela = tabela[tabela["previsao"] == previsao]
        tabela = tabela[tabela["data"] == data]
        tabela = tabela[tabela["valor"] == valor]
        global selecionado
        if len(tabela) == 1:
            id = tabela.iloc[0].name
            selecionado = id
            item = Tabela.Entrada.tabela.loc[id]
            mensagem(
                titulo="Excluir "+nome,
                mensagem="Deseja excluir "+nome+"?",
                aceita=lambda: mensagem_excluir_aceita(lambda: Tabela.Entrada.excluir(id)),
                rejeita=mensagem_excluir_rejeita
            )
        else:
            selecionado = -1


def hoje_entrada_click(item):
    item = gui.ui.treeEntrada.selectedItems()[0]
    nome = item.text(0)
    previsao = item.text(1)
    data = item.text(2)
    valor = float(item.text(3).replace("R$", ""))
    tabela = Tabela.Entrada.tabela
    tabela = tabela[tabela["nome"] == nome]
    tabela = tabela[tabela["previsao"] == previsao]
    tabela = tabela[tabela["data"] == data]
    tabela = tabela[tabela["valor"] == valor]
    global selecionado
    if len(tabela) == 1:
        id = tabela.iloc[0].name
        selecionado = id
        item = Tabela.Entrada.tabela.loc[id]
        gui.uiEntradaEdit.inputEntrada.setText(item["nome"])
        gui.uiEntradaEdit.spinValor.setValue(item["valor"])
        if pd.notna(item["comentario"]):
            gui.uiEntradaEdit.textComentario.setText(item["comentario"])
        gui.uiEntradaEdit.dateEdit.setDate(QDate().fromString(item["previsao"], "dd/MM/yyyy"))
        if item["data"]:
            gui.uiEntradaEdit.checkPago.setCheckState(2)
            gui.uiEntradaEdit.dateEdit_2.setDate(QDate().fromString(item["data"], "dd/MM/yyyy"))
        else:
            gui.uiEntradaEdit.checkPago.setCheckState(0)
        gui.wEntradaEdit.setWindowTitle("Editar " + item["nome"])
        gui.wEntradaEdit.show()
    else:
        selecionado = -1


def hoje_reserva_click(item):
    item = gui.ui.treeReserva.selectedItems()[0]
    nome = item.text(0)
    valor = float(item.text(1).replace("R$", ""))
    comentario = item.text(2)
    tabela = Tabela.Reserva.tabela
    tabela = tabela[tabela["nome"] == nome]
    tabela = tabela[tabela["valor"] == valor]
    global selecionado
    if len(tabela) == 1:
        id = tabela.iloc[0].name
        selecionado = id
        item = Tabela.Reserva.tabela.loc[id]
        gui.uiReservaEdit.inputReserva.setText(item["nome"])
        gui.uiReservaEdit.spinValor.setValue(item["valor"])
        if pd.notna(item["comentario"]):
            gui.uiReservaEdit.textComentario.setText(item["comentario"])
        gui.wReservaEdit.setWindowTitle("Editar " + item["nome"])
        gui.wReservaEdit.show()
    else:
        selecionado = -1


def hoje_botao_excluir_reserva():
    if len(gui.ui.treeReserva.selectedItems()):
        item = gui.ui.treeReserva.selectedItems()[0]
        nome = item.text(0)
        valor = float(item.text(1).replace("R$", ""))
        comentario = item.text(2)
        tabela = Tabela.Reserva.tabela
        tabela = tabela[tabela["nome"] == nome]
        tabela = tabela[tabela["valor"] == valor]
        global selecionado
        if len(tabela) == 1:
            id = tabela.iloc[0].name
            selecionado = id
            item = Tabela.Reserva.tabela.loc[id]
            mensagem(
                titulo="Excluir " + nome,
                mensagem="Deseja excluir " + nome + "?",
                aceita=lambda: mensagem_excluir_aceita(lambda: Tabela.Reserva.excluir(id)),
                rejeita=mensagem_excluir_rejeita
            )
        else:
            selecionado = -1


def hoje_botao_ajuste():
    total = Hoje.soma_reserva+Hoje.mes_resta
    for label, texto in [
        (gui.uiAjuste.labelReserva, Hoje.soma_reserva),
        (gui.uiAjuste.labelResto, Hoje.mes_resta),
        (gui.uiAjuste.labelSoma, total),
        (gui.uiAjuste.labelApp, total)
    ]:
        label.setText(escreve_dinheiro(texto))
    for label in [
        gui.uiAjuste.labelTenho,
        gui.uiAjuste.labelApp,
        gui.uiAjuste.labelAdd,
        gui.uiAjuste.labelAjuste,
    ]:
        label.clear()
    gui.uiAjuste.botaoAdd.setText("Ajuste")
    gui.uiAjuste.botaoAdd.setEnabled(False)
    gui.wAjuste.show()


def ajuste_carteira():
    soma = 0.00
    for spin, valor in [
        (gui.uiAjuste.spin001.value(), 0.01),
        (gui.uiAjuste.spin005.value(), 0.05),
        (gui.uiAjuste.spin01.value(), 0.1),
        (gui.uiAjuste.spin025.value(), 0.25),
        (gui.uiAjuste.spin05.value(), 0.5),
        (gui.uiAjuste.spin1.value(), 1),
        (gui.uiAjuste.spin2.value(), 2),
        (gui.uiAjuste.spin5.value(), 5),
        (gui.uiAjuste.spin10.value(), 10),
        (gui.uiAjuste.spin20.value(), 20),
        (gui.uiAjuste.spin50.value(), 50),
        (gui.uiAjuste.spin100.value(), 100),
    ]:
        soma += spin*valor
    gui.uiAjuste.spinCarteira.setValue(soma)


def ajuste_soma():
    soma = 0.0
    for spin, valor in [
        (gui.uiAjuste.spinAjusteN.value(), -1),
        (gui.uiAjuste.spinAjusteP.value(), 1),
        (gui.uiAjuste.spinCarteira.value(), 1),
        (gui.uiAjuste.spinConta1.value(), 1),
        (gui.uiAjuste.spinCredito1.value(), -1),
        (gui.uiAjuste.spinCredito2.value(), -1),
        (gui.uiAjuste.spinPoupanca.value(), 1),
        (gui.uiAjuste.spinPoupanca2.value(), 1),
        (gui.uiAjuste.spintConta2.value(), 1)
    ]:
        soma += spin*valor
    app = Hoje.soma_reserva+Hoje.mes_resta
    ajuste = soma-app
    for label, texto in [
        (gui.uiAjuste.labelTenho, soma),
        (gui.uiAjuste.labelAjuste, ajuste),
        (gui.uiAjuste.labelApp, app)
    ]:
        label.setText(escreve_dinheiro(texto))
    print(ajuste)
    if ajuste >= 0.01:
        texto = "Adicionar entrada de " + escreve_dinheiro(ajuste)
        botao = "Entrada"
        estado = True
        funcao = lambda: ajuste_botao_entrada(ajuste)
    elif ajuste <= -0.01:
        texto = "Adicionar saida de " + escreve_dinheiro(-ajuste)
        botao = "Saida"
        estado = True
        funcao = lambda: ajuste_botao_gasto(ajuste)
    else:
        texto = ""
        botao = "Ajustar"
        estado = False
        funcao = print
    gui.uiAjuste.labelAdd.setText(texto)
    gui.uiAjuste.botaoAdd.setEnabled(estado)
    gui.uiAjuste.botaoAdd.setText(botao)

    gui.uiAjuste.botaoAdd.disconnect()
    gui.uiAjuste.botaoAdd.clicked.connect(funcao)

    pyperclip.copy( str(f"{abs(ajuste):.2f}").replace(".", ",") )

def ajuste_botao_gasto(valor):
    gui.wAjuste.hide()
    gui.wFixoAdd.show()
    gui.uiFixoAdd.inputGasto.setText("Ajuste de erro")
    gui.uiFixoAdd.checkPago.setCheckState(2)
    gui.uiFixoAdd.spinValor.setValue(-valor)


def ajuste_botao_entrada(valor):
    gui.wAjuste.hide()
    gui.wEntradaAdd.show()
    gui.uiEntradaAdd.inputEntrada.setText("Ajuste de erro")
    gui.uiEntradaAdd.checkPago.setCheckState(2)
    gui.uiEntradaAdd.spinValor.setValue(valor)


def escreve_dinheiro(valor):
    texto = "R$" + f"{valor:.2f}"
    texto = texto.replace(".", ",")
    return texto


def gasto_fila_click(item):
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
            gasto_validador()
            ArvoreFilaGastos.atualiza()


# ações dos eventos de mudança


def combo_sub_troca(comboCat, comboSub):
    cat_id = comboCat.getId()
    comboSub.troca(cat_id)


def grafico_barra(grafico, dados, completo=False, destaque=True, fatia=False, titulo=""):
    print("Gera gráfico de barras")
    dias_destaque = []
    inicio = Info.mes_str + "/01/" + Info.ano_str
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
        dias_destaque = retornar_fds(dados)
    grafico.plot(rotulos, tabela["valor"],
                 destaque=dias_destaque, fatia=fatia, titulo=titulo, limite=Hoje.dia_limite, media=Hoje.media_dia)


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
    #     dias_destaque=retornar_fds(dados)
    grafico.plot(rotulos, tabela["valor"], destaque=dias_destaque, fatia=fatia, titulo=titulo)


def retornar_fds(dados):
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
    if gui.ui.comboGrafico.currentIndex() == 0:
        grafico_barra(gui.ui.graficoBarra, dados[dados["categoria"] == id_cat], destaque=True, fatia=True, titulo=cat)
    gui.ui.graficoPizza.fig.canvas.mpl_disconnect(cid)
    cid = gui.ui.graficoPizza.fig.canvas.mpl_connect('pick_event', grafico_click_reseta)


def grafico_click_zoom(event):
    wedge = event.artist
    label = wedge.get_label()
    label = label.replace("\n", " ")
    combo = gui.ui.comboGrafico.currentIndex()
    if combo == 0:
        grafico_fatia(gui.ui.graficoPizza, Tabela.Saida.tabela, label)
    elif combo == 1:
        grafico_fatia(gui.ui.graficoPizza, Tabela.Fixo.tabela, label)
    else:
        soma = Tabela.Saida.tabela.append(Tabela.Fixo.tabela)
        grafico_fatia(gui.ui.graficoPizza, soma, label)


def grafico_click_reseta(event):
    global cid
    hoje_grafico_escreve()
    gui.ui.graficoPizza.fig.canvas.mpl_disconnect(cid)
    cid = gui.ui.graficoPizza.fig.canvas.mpl_connect('pick_event', grafico_click_zoom)


def hoje_grafico_escreve():
    global cid2
    combo = gui.ui.comboGrafico.currentIndex()
    grafico_barra(gui.ui.graficoBarra, Tabela.Saida.tabela)
    if combo == 0:
        grafico_pizza(gui.ui.graficoPizza, Tabela.Saida.tabela)
    elif combo == 1:
        grafico_pizza(gui.ui.graficoPizza, Tabela.Fixo.tabela)
    else:
        soma = Tabela.Saida.tabela.append(Tabela.Fixo.tabela)
        grafico_pizza(gui.ui.graficoPizza, soma)


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


def mensagem_tabela_aceita():
    gui.wMensagem.hide()
    Info.atualiza()
    Geral.adicionar(
        [Meses[Info.mes_int],
         Hoje.soma_entrada,
         Hoje.soma_saida + Hoje.soma_fixo]
    )
    Tabela = Mensal(Info.ano_int, Info.mes_int)
    completer_atualiza()
    exit()


def mensagem_tabela_rejeita():
    gui.wMensagem.hide()


def mensagem_excluir_rejeita():
    gui.wMensagem.hide()
    global selecionado
    selecionado=-1


def mensagem_excluir_aceita(excluir):
    gui.wMensagem.hide()
    selecionado = -1
    excluir()
    ArvoreEntrada.atualiza(Tabela.Entrada.tabela)
    ArvoreFixo.atualiza(Tabela.Fixo.tabela)
    ArvoreReserva.atualiza(Tabela.Reserva.tabela)
    gasto_atualiza()


def completer_atualiza():
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


def botao_excluir():
    acao = [
        hoje_botao_excluir_gasto,
        hoje_botao_excluir_entrada,
        hoje_botao_excluir_fixo,
        hoje_botao_excluir_reserva
    ]
    arvore = gui.ui.stackedWidget.currentIndex()
    acao[arvore]()

def filtro():
    Saida = Tabela.Saida.tabela.copy()[["nome", "data", "categoria", "subcategoria", "valor"]]
    Saida["tipo"] = "gasto"
    Fixo = Tabela.Fixo.tabela.copy()[["nome", "vencimento", "categoria", "subcategoria", "valor"]]
    Fixo["tipo"] = "fixo"
    Fixo = Fixo.rename(columns={"vencimento": "data"})
    Entrada = Tabela.Entrada.tabela.copy()[["nome", "previsao", "valor"]]
    Entrada["tipo"] = "entrada"
    Entrada["categoria"] = None
    Entrada["subcategoria"] = None
    Entrada = Entrada.rename(columns={"previsao": "data"})
    Filtro = pd.DataFrame(Saida.append(
        Fixo.append(
            Entrada
        )
    ))

    completer = QCompleter(Filtro["nome"].str.title().unique())
    completer.setCaseSensitivity(Qt.CaseInsensitive)
    gui.ui.inputFiltro.setCompleter(completer)

    if gui.ui.checkRelTipo.checkState():
        Filtro = Filtro[Filtro["tipo"] == gui.ui.comboTipo.currentText()]
    if gui.ui.checkRelNome.checkState():
        nome = gui.ui.inputFiltro.text()
        while "  " in nome:
            nome = nome.replace("  ", " ")
        while nome[0] == " ":
            nome = nome[:0] + nome[(0 + 1):]
        while nome[-1] == " ":
            nome = nome[:-1]
        nome = nome.capitalize()
        gui.ui.inputFiltro.setText(nome)
        Filtro = Filtro[Filtro["nome"].str.contains(nome, case=False)]
    if gui.ui.checkRelCat.checkState():
        id = ComboFiltroCat.getId()
        Filtro = Filtro[Filtro["categoria"] == id]
        if not len(ComboFiltroSub.ativosSub):
            gui.ui.checkRelSub.setCheckState(0)
    if gui.ui.checkRelSub.checkState():
        id = ComboFiltroCat.getId()
        sub = ComboFiltroSub.getId()
        Filtro = Filtro[Filtro["subcategoria"] == sub]
    if gui.ui.checkRelFim.checkState() or gui.ui.checkRelInicio.checkState():
        if gui.ui.dateFim.date() < gui.ui.dateInicio.date():
            print("!!")
            gui.ui.dateFim.setDate(gui.ui.dateInicio.date())
        Filtro["data2"] = Filtro.apply(lambda row: QDate.fromString(row["data"], "dd/MM/yyyy"), axis=1)
        if gui.ui.checkRelInicio.checkState():
            Filtro = Filtro[Filtro["data2"] >= gui.ui.dateInicio.date()]
        if gui.ui.checkRelFim.checkState():
            Filtro = Filtro[Filtro["data2"] <= gui.ui.dateFim.date()]

    gui.ui.labelSomaFiltro.setText(escreve_dinheiro(Filtro['valor'].sum()))
    ArvoreFiltro = ArvoreTabelaFiltro(gui.ui.treeFiltro, Filtro, Categoria)


def filtro_check(check, widget):
    state = bool(check.checkState())
    widget.setEnabled(state)


def filtro_limpa():
    for check in [
        gui.ui.checkRelTipo,
        gui.ui.checkRelNome,
        gui.ui.checkRelCat,
        gui.ui.checkRelSub,
        gui.ui.checkRelInicio,
        gui.ui.checkRelFim,
    ]:
        check.setCheckState(0)

    for combo in[
        gui.ui.comboTipo,
        gui.ui.comboCategoria,
        gui.ui.comboSub,
    ]:
        combo.setCurrentIndex(0)

    gui.ui.inputFiltro.clear()
    gui.ui.dateInicio.setDate(QDate(Info.ano_int, Info.mes_int, 1))
    gui.ui.dateFim.setDate(QDate(Info.ano_int, Info.mes_int, QDate(Info.ano_int, Info.mes_int, 1).daysInMonth()))

# MAIN

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
ComboFiltroCat = Link(gui.ui.comboCategoria, Categoria)
ComboFiltroSub = SubcategoriaLink(gui.ui.comboSub, Categoria)
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
# ComboPagamento = Link(gui.uiGastosAdd.comboPagamento, Pagamentos)
# ComboFixoPag = Link(gui.uiFixoAdd.comboPagamento, Pagamentos)

# gui.ui.toolAdicionar.hide()
# gui.ui.botaoGasto.clicked.connect(hoje_botao_gasto_add)
acao_gasto = QAction("Gasto")
acao_gasto.triggered.connect(hoje_botao_gasto_add)
# gui.ui.botaoEntrada.clicked.connect(hoje_botao_entrada_add)
acao_entrada = QAction("Entrada")
acao_entrada.triggered.connect(hoje_botao_entrada_add)
# gui.ui.botaoFixo.clicked.connect(hoje_botao_fixo_add)
acao_fixo = QAction("Fixo")
acao_fixo.triggered.connect(hoje_botao_fixo_add)
# gui.ui.botaoReserva.clicked.connect(hoje_botao_reserva_add)
acao_reserva = QAction("Reserva")
acao_reserva.triggered.connect(hoje_botao_reserva_add)
menu = QMenu()
menu.addAction(acao_gasto)
menu.addAction(acao_entrada)
menu.addAction(acao_fixo)
menu.addAction(acao_reserva)
gui.ui.toolAdicionar.setPopupMode(QToolButton.InstantPopup)
gui.ui.toolAdicionar.setMenu(menu)

# ações

# conecta as ações dos botões

gui.uiAjuste.pushButton.clicked.connect(print)
gui.ui.botaoAjuste.clicked.connect(hoje_botao_ajuste)
gui.uiAjuste.pushButton.clicked.connect(lambda: gui.wAjuste.hide())

gui.uiGastosAdd.botaoHoje.clicked.connect(
    lambda: gui.uiGastosAdd.dateEdit.setDate(QDate.currentDate())
)
gui.uiGastosAdd.buttonBox.accepted.connect(gasto_botao_add)
gui.uiGastosAdd.buttonBox.rejected.connect(gasto_botao_cancela)
gui.uiGastosAdd.botaoAdd.clicked.connect(gasto_botao_fila)

gui.uiGastosEdit.buttonBox.accepted.connect(gasto_botao_editar)

gui.uiFixoAdd.buttonBox.accepted.connect(fixo_botao_add)
gui.uiFixoEdit.buttonBox.accepted.connect(fixo_botao_editar)

gui.uiFixoAdd.botaoHoje.clicked.connect(
    lambda: gui.uiFixoAdd.dateEdit.setDate(QDate.currentDate())
)
gui.uiFixoAdd.botaoHoje_2.clicked.connect(
    lambda: gui.uiFixoAdd.dateEdit_2.setDate(QDate.currentDate())
)

gui.uiFixoEdit.botaoHoje.clicked.connect(
    lambda: gui.uiFixoEdit.dateEdit.setDate(QDate.currentDate())
)
gui.uiFixoEdit.botaoHoje_2.clicked.connect(
    lambda: gui.uiFixoEdit.dateEdit_2.setDate(QDate.currentDate())
)

gui.uiEntradaEdit.botaoHoje.clicked.connect(
    lambda: gui.uiEntradaEdit.dateEdit.setDate(QDate.currentDate())
)

gui.uiEntradaEdit.botaoHoje_2.clicked.connect(
    lambda: gui.uiEntradaEdit.dateEdit_2.setDate(QDate.currentDate())
)

gui.uiEntradaAdd.botaoHoje.clicked.connect(
    lambda: gui.uiEntradaAdd.dateEdit.setDate(QDate.currentDate())
)
gui.uiEntradaAdd.botaoHoje_2.clicked.connect(
    lambda: gui.uiEntradaAdd.dateEdit_2.setDate(QDate.currentDate())
)

for widget in [
    gui.uiGastosAdd.dateEdit,
    gui.uiGastosEdit.dateEdit,
    gui.uiFixoAdd.dateEdit,
    gui.uiFixoAdd.dateEdit_2,
    gui.uiFixoEdit.dateEdit,
    gui.uiFixoEdit.dateEdit_2,
    gui.uiEntradaEdit.dateEdit,
    gui.uiEntradaEdit.dateEdit_2,
    gui.uiEntradaAdd.dateEdit,
    gui.uiEntradaAdd.dateEdit_2
]:
    widget.setDate(QDate.currentDate())

gui.ui.dateInicio.setDate(QDate(Info.ano_int, Info.mes_int, 1))
gui.ui.dateFim.setDate(QDate(Info.ano_int, Info.mes_int, QDate(Info.ano_int, Info.mes_int, 1).daysInMonth()))

gui.uiEntradaAdd.buttonBox.accepted.connect(entrada_botao_add)
gui.uiEntradaEdit.buttonBox.accepted.connect(entrada_botao_editar)

gui.uiReservaAdd.buttonBox.accepted.connect(reserva_botao_add)
gui.uiReservaEdit.buttonBox.accepted.connect(reserva_botao_editar)

gui.ui.botaoCategoriaAdicionar.clicked.connect(conf_botao_cat_add)
gui.ui.botaoPessoaAdicionar.clicked.connect(conf_botao_pessoa_add)
gui.ui.botaoSubAdicionar.clicked.connect(conf_botao_sub_add)
gui.ui.botaoPessoaEditar.clicked.connect(conf_botao_pessoa_editar)
gui.ui.botaoCategoriaEditar.clicked.connect(conf_botao_cat_editar)

gui.uiPessoasAdd.buttonBox.accepted.connect(pessoa_botao_add)
gui.uiPessoasAdd.buttonBox.rejected.connect(pessoa_botao_cancela)

gui.uiPessoasEdit.buttonBox.accepted.connect(pessoa_botao_editar)
gui.uiPessoasEdit.buttonBox.rejected.connect(gui.wPessoasEdit.hide)  # todo criar uma função para o botão "cancelar"

gui.uiCategoriasAdd.buttonBox.accepted.connect(cat_botao_add)
gui.uiCategoriasAdd.buttonBox.rejected.connect(cat_botao_cancela)

gui.uiSubCategoriasAdd.botaoMais.clicked.connect(sub_botao_fila)
gui.uiSubCategoriasAdd.buttonBox.accepted.connect(sub_botao_add)
gui.uiSubCategoriasAdd.buttonBox.rejected.connect(sub_botao_cancela)

gui.ui.botaoExcluir.clicked.connect(botao_excluir)

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
    validador_conecta(
        botao=item["botao"],
        texto=item["texto"],
        valor=item["valor"]
    )

# conecta as ações das trocas em check box

gui.uiEntradaAdd.checkPago.stateChanged.connect(entrada_calendario_habilita)

gui.uiFixoAdd.checkPago.stateChanged.connect(fixo_calendario_habilita)

gui.uiFixoEdit.checkPago.stateChanged.connect(lambda: gui.calendario_habilita(gui.uiFixoEdit))
gui.uiEntradaEdit.checkPago.stateChanged.connect(lambda: gui.calendario_habilita(gui.uiEntradaEdit))

# conecta as ações de atualização dinâmica de campos
for spin in [
    gui.uiAjuste.spin001,
    gui.uiAjuste.spin005,
    gui.uiAjuste.spin01,
    gui.uiAjuste.spin025,
    gui.uiAjuste.spin05,
    gui.uiAjuste.spin1,
    gui.uiAjuste.spin2,
    gui.uiAjuste.spin5,
    gui.uiAjuste.spin10,
    gui.uiAjuste.spin20,
    gui.uiAjuste.spin50,
    gui.uiAjuste.spin100
]:
    spin.valueChanged.connect(ajuste_carteira)

for spin in [
    gui.uiAjuste.spinAjusteN,
    gui.uiAjuste.spinAjusteP,
    gui.uiAjuste.spinCarteira,
    gui.uiAjuste.spinConta1,
    gui.uiAjuste.spinCredito1,
    gui.uiAjuste.spinCredito2,
    gui.uiAjuste.spinPoupanca,
    gui.uiAjuste.spinPoupanca2,
    gui.uiAjuste.spintConta2,
]:
    spin.valueChanged.connect(ajuste_soma)

# conecta as ações dos clicks em lista

gui.uiSubCategoriasAdd.listWidget.itemDoubleClicked.connect(sub_list_click)
gui.ui.treeSaida.doubleClicked.connect(hoje_gasto_click)
gui.ui.treeFixo.doubleClicked.connect(hoje_fixo_click)
gui.ui.treeEntrada.doubleClicked.connect(hoje_entrada_click)
gui.ui.treeReserva.doubleClicked.connect(hoje_reserva_click)

gui.uiGastosAdd.treeWidget.doubleClicked.connect(gasto_fila_click)

gui.ui.listMenu.itemClicked.connect(
    lambda: gui.ui.stackedWidget.setCurrentIndex(
        gui.ui.listMenu.currentRow()
    )
)

for check, widget in [
    (gui.ui.checkRelTipo, gui.ui.comboTipo),
    (gui.ui.checkRelNome, gui.ui.inputFiltro),
    (gui.ui.checkRelCat, gui.ui.comboCategoria),
    (gui.ui.checkRelSub, gui.ui.comboSub),
    (gui.ui.checkRelInicio, gui.ui.dateInicio),
    (gui.ui.checkRelFim, gui.ui.dateFim)
]:
    widget.setEnabled(False)

gui.ui.checkRelTipo.stateChanged.connect(lambda: filtro_check(gui.ui.checkRelTipo, gui.ui.comboTipo))
gui.ui.checkRelNome.stateChanged.connect(lambda: filtro_check(gui.ui.checkRelNome, gui.ui.inputFiltro))
gui.ui.checkRelCat.stateChanged.connect(lambda: filtro_check(gui.ui.checkRelCat, gui.ui.comboCategoria))
gui.ui.checkRelSub.stateChanged.connect(lambda: filtro_check(gui.ui.checkRelSub, gui.ui.comboSub))
gui.ui.checkRelInicio.stateChanged.connect(lambda: filtro_check(gui.ui.checkRelInicio, gui.ui.dateInicio))
gui.ui.checkRelFim.stateChanged.connect(lambda: filtro_check(gui.ui.checkRelFim, gui.ui.dateFim))

gui.ui.botaoFiltro.clicked.connect(filtro)
gui.ui.botaoLimpa.clicked.connect(filtro_limpa)

# conect as ações dos clicks nos gráficos

cid = gui.ui.graficoPizza.fig.canvas.mpl_connect('pick_event', grafico_click_zoom)
cid2 = gui.ui.graficoBarra.fig.canvas.mpl_connect('button_press_event', grafico_click_reseta)

gui.ui.comboGrafico.currentIndexChanged.connect(hoje_grafico_escreve)

# combos dinâmicos que mudam de valores conforme a seleção em combo pai

combos_dinamicos = [  # todo procurar mais combos dinamicos, como no add sub-categorias
    [
        gui.uiSubCategoriasAdd.comboCat,
        lambda: combo_sub_troca(ComboSubAddCat, ComboSubAdd)
    ],
    [
        gui.uiGastosAdd.comboCategoria,
        lambda: combo_sub_troca(ComboGastoCat, ComboGastoSub)
    ],
    [
        gui.uiGastosEdit.comboCategoria,
        lambda: combo_sub_troca(ComboGastoEditCat, ComboGastoEditSub)
    ],
    [
        gui.uiFixoAdd.comboCategoria,
        lambda: combo_sub_troca(ComboFixoCat, ComboFixoSub)
    ],
    [
        gui.uiFixoEdit.comboCategoria,
        lambda: combo_sub_troca(ComboFixoEditCat, ComboFixoEditSub)
    ],
    [
        gui.ui.comboCategoria,
        lambda: combo_sub_troca(ComboFiltroCat, ComboFiltroSub)
    ]
]
for item in combos_dinamicos:
    item[0].currentIndexChanged.connect(item[1])

# inicia as tabelas

print("Inicia as tabelas")

Historico = []

# cria uma pasta para o ano caso não exista
if not os.path.exists('data/' + Info.ano_str):
    print("Cria pasta do ano")
    os.makedirs('data/' + Info.ano_str)

# confere se já tem a tabela do mês atual
if tabela_existe(Info.ano_str, Info.mes_str):
    print("Carrega as tabelas do mês atual")
else:
    print("Tabelas desatualizadas")
    mensagem(
        titulo="Tabelas desatualizadas",
        mensagem="Tabelas desatualizadas\nDeseja iniciar as tabelas deste mês?\nSerá necessário reiniciar o app",
        aceita=mensagem_tabela_aceita,
        rejeita=mensagem_tabela_rejeita,
    )
    while not tabela_existe(Info.ano_str, Info.mes_str):
        if Info.mes_int == 1:
            Info.set_data(Info.ano_int - 1, 12, Info.dia_int)
        else:
            Info.set_data(Info.ano_int, Info.mes_int - 1, Info.dia_int)
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
    gui.ui.treeAno.header(),
    gui.ui.treeFiltro.header()
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

hoje_grafico_escreve()
gui.ui.graficoLinha.plot(Geral.tabela)
filtro()
sys.exit(gui.app.exec_())

# todo 29/07/2019: remover a "ordem" das categorias, é pura bobagem
