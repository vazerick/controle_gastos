import sys
import os
import configparser
import pandas

# interface gráfica
from src.gui import gui

# classes
from src.lista import ListaPessoa, ListaCategoria
from src.link import Link, SubcategoriaLink

# funções de teste

count = 0


def panda():
    dt = pandas.read_csv("data/tabela.csv", quotechar="'", index_col='id')
    dt.to_csv("data/tabela.csv", quotechar="'", index_label='id')
    print(dt['valor'])


def acao():
    global count
    count += 1
    gui.ui.label.setText(str(count))
    print(Combo.getId())

    # gui.wPessoasAdd.show()
    # gui.wCategoriasAdd.show()
    gui.wSubCategoriasAdd.show()


# declaração das funções


def vazia(texto):
    return not bool(texto and texto.strip())


def not_valida(input):
    for item in input:
        if vazia(item.text()):
            return 1


# editar uma subcategoia na edição


def subcategorias_lista_click(item):
    gui.subcategorias_remove()
    gui.uiSubCategoriasAdd.inputNome.setText(item.text())
    filaSubCategorias.remove(item.text())
    print(item.text())


# atualiza os combos após atualizar a lista Categorias


def combos_categoria_atualiza():
    colecao = [
        ComboSubAdd,
        ComboSubAddCat,
        ComboCategoriaAdd
    ]

    for item in combos_dinamicos:
        item['link'].disconnect()

    for item in colecao:
        item.atualiza()

    for item in combos_dinamicos:
        item['link'].currentIndexChanged.connect(item['acao'])


# ações de botões


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
    gui.wPessoasAdd.hide()
    gui.uiPessoasAdd.inputNome.clear()


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
    gui.wCategoriasAdd.hide()
    gui.uiCategoriasAdd.inputNome.clear()
    print(gui.uiCategoriasAdd.checkBox.isChecked())


filaSubCategorias = []


def subcategorias_ui(categoria):
    gui.wSubCategoriasAdd.show()


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


# ações dos eventos de mudança


def troca_subcategoria():
    cat_id = ComboSubAddCat.getId()
    ComboSubAdd.troca(cat_id)


# configuração

config = configparser.ConfigParser()
if os.path.exists("config.ini"):
    config.read("config.ini")
else:
    config['PAGAMENTO'] = {
        'banco': 'sim',
        'vale': 'nao'
    }
    config['LAYOUT'] = {
        'interface': 'escura'
    }
    config['DADOS'] = {
        'inicio': '',
        'fim': ''
    }
    config.write(open('config.ini', 'w'))
print(config['LAYOUT']['Interface'])

# inicia a interface gráfica
gui = gui()

# objetos de listas
Pessoa = ListaPessoa("pessoa")
Categoria = ListaCategoria("categoria")

# objetos de link de combos
Combo = Link(gui.ui.comboBox, Pessoa)
# links de pessoa
ComboPessoaAdd = Link(gui.uiPessoasAdd.comboBox, Pessoa, addFim=1)
# links de categoria
ComboCategoriaAdd = Link(gui.uiCategoriasAdd.comboBox, Categoria, addFim=1)
ComboSubAddCat = Link(gui.uiSubCategoriasAdd.comboCat, Categoria)
ComboSubAdd = SubcategoriaLink(gui.uiSubCategoriasAdd.comboSub, Categoria, addFim=1)

# ações

# conecta as ações dos botões
gui.ui.pushButton.clicked.connect(acao)

gui.uiPessoasAdd.botaoOk.clicked.connect(botao_pessoa_add)
gui.uiPessoasAdd.botaoCancela.clicked.connect(gui.wPessoasAdd.hide)

gui.uiCategoriasAdd.botaoOk.clicked.connect(botao_categorias_add)
gui.uiCategoriasAdd.botaoCancela.clicked.connect(gui.wCategoriasAdd.hide)

gui.uiSubCategoriasAdd.botaoMais.clicked.connect(botao_subcategorias_mais)
gui.uiSubCategoriasAdd.botaoOk.clicked.connect(botao_subcategorias_add)
gui.uiSubCategoriasAdd.botaoCancela.clicked.connect(botao_subcategoria_cancela)


# conecta as ações dos clicks em lista
gui.uiSubCategoriasAdd.listWidget.itemDoubleClicked.connect(subcategorias_lista_click)


combos_dinamicos = [
    {
        'link': gui.uiSubCategoriasAdd.comboCat,
        'acao': troca_subcategoria
    }
]
for item in combos_dinamicos:
    item['link'].currentIndexChanged.connect(item['acao'])
# gui.uiSubCategoriasAdd.comboCat.currentIndexChanged.connect(troca_subcategoria)

# testes


# configura o fim do programa
sys.exit(gui.app.exec_())

# A fazer:
# Limpar o combo e o checkbox escolhidos ao dar Ok
# Organizar as adições das listas
# Atualizar todos os combos relevantes quando houver atualização

"""
árvore:
    importa QTreeWidgetItem
    
l1 = QTreeWidgetItem(["String A", "String B", "String C"])
l2 = QTreeWidgetItem(["String AA", "String BB", "String CC"])
for i in range(3):
    l1_child = QTreeWidgetItem(["Child A" + str(i), "Child B" + str(i), "Child C" + str(i)])
    l1.addChild(l1_child)

for j in range(2):
    l2_child = QTreeWidgetItem(["Child AA" + str(j), "Child BB" + str(j), "Child CC" + str(j)])
    l2.addChild(l2_child)

ui.treeWidget.addTopLevelItem(l1)
ui.treeWidget.addTopLevelItem(l2)
"""
