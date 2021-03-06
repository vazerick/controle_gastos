import time
import xml.dom.minidom
from xml.dom import minidom


# classe geral das listas geradas pelos arquivos .xml

class Lista:

    def __init__(self, nome):
        self.endereco = "data/" + nome + ".xml"
        try:
            arquivo = xml.dom.minidom.parse(self.endereco)
        except FileNotFoundError:
            arvore = xml.dom.minidom.Document()
            arvore.appendChild(arvore.createComment("Criacao: %s" % time.asctime(time.localtime(time.time()))))
            lista = arvore.createElement('lista')
            arvore.appendChild(lista)

            arquivo = open(self.endereco, "w", encoding='utf-8')
            arquivo.write(arvore.toprettyxml(indent='   '))

            arquivo = []

        try:
            lista = arquivo.documentElement  # lê o nó <lista> do arquivo
            self.itens = lista.getElementsByTagName(nome)  # gera a lista de nós de cada item
        except AttributeError:
            lista = []
            self.itens = []
        self.id = []  # lista vazia para abrigar os itens

    def adiciona(self, add):
        add['id'] = len(self.id)
        add['status'] = 1
        self.id.append(add)

    def edita(self, index, nome, status):
        self.id[index]['nome'] = nome
        self.id[index]['status'] = status


class ListaCategoria(Lista):

    def __init__(self, nome):
        super().__init__(nome)

        for item in self.itens:  # para cada item da lista, cria um dicionário com os atributos definidos
            nome = item.getElementsByTagName("nome")[0]
            status = item.getElementsByTagName("status")[0]
            sub_status = item.getElementsByTagName("sub_status")[0]

            sub_lista = item.getElementsByTagName("sub_lista")[0]
            sub_cats = sub_lista.getElementsByTagName("sub")

            sub = []  # cria a lista para abrigar as subcategorias

            for sub_cat in sub_cats:  # para cada sub_categorias da lsta, cria um dicionário com os atributos
                snome = sub_cat.getElementsByTagName("nome")[0]
                sstatus = sub_cat.getElementsByTagName("status")[0]

                sub.append(
                    {
                        'id': int(sub_cat.getAttribute("id")),
                        'nome': snome.childNodes[0].data,
                        'status': int(sstatus.childNodes[0].data),
                    }
                )
            print(nome.childNodes[0].data)
            self.id.append(
                {
                    'id': int(item.getAttribute("id")),
                    'nome': nome.childNodes[0].data,
                    'status': int(status.childNodes[0].data),
                    'sub_status': int(sub_status.childNodes[0].data),
                    'sub_lista': sub
                }
            )

    def edita(self, index, nome, status):
        super(ListaCategoria, self).edita(index, nome, status)
        self.salva()

    def editaSub(self, id_cat, id_sub, nome, status):
        self.id[id_cat]['sub_lista'][id_sub]['nome'] = nome
        self.id[id_cat]['sub_lista'][id_sub]['status'] = status
        self.salva()

    def getNome(self, id):
        return self.id[id]['nome']

    def getSubNome(self, id_cat, id_sub):
        if self.id[id_cat]['sub_status']:
            return self.id[id_cat]['sub_lista'][id_sub]['nome']
        else:
            return ""

    def getAtivos(self):
        ativos = []  # lista vazia para abrigar os itens ativos
        for item in range(len(self.id)):
            if self.id[item]["status"]:
                ativos.append(
                    {
                        'id': self.id[item]["id"],
                        'nome': self.id[item]["nome"],
                        'sub_status': self.id[item]["sub_status"],
                        'sub_lista': self.id[item]["sub_lista"]
                    }
                )
        return ativos

    def salva(self):
        doc = minidom.Document()  # cria um objeto xml
        # adiciona um comentário com o horário de criação
        doc.appendChild(doc.createComment("Criacao: %s" % time.asctime(time.localtime(time.time()))))
        lista = doc.createElement('lista')  # cria uma lista xml de doc
        for indice in self.id:  # adiciona cada nó na lista de doc
            item = doc.createElement('categoria')
            item.setAttribute('id', str(indice['id']))
            lista.appendChild(item)

            nome = doc.createElement('nome')
            item.appendChild(nome)
            nome.appendChild(doc.createTextNode(indice['nome']))

            status = doc.createElement('status')
            item.appendChild(status)
            status.appendChild(doc.createTextNode(str(indice['status'])))

            sub_status = doc.createElement('sub_status')
            item.appendChild(sub_status)
            sub_status.appendChild(doc.createTextNode(str(indice['sub_status'])))

            sub_lista = doc.createElement('sub_lista')
            item.appendChild(sub_lista)

            if indice['sub_status']:
                for sub_cat in indice['sub_lista']:
                    sitem = doc.createElement('sub')
                    sitem.setAttribute('id', str(sub_cat['id']))
                    sub_lista.appendChild(sitem)

                    nome = doc.createElement('nome')
                    sitem.appendChild(nome)
                    nome.appendChild(doc.createTextNode(sub_cat['nome']))

                    status = doc.createElement('status')
                    sitem.appendChild(status)
                    status.appendChild(doc.createTextNode(str(sub_cat['status'])))

        doc.appendChild(lista)

        arquivo = open(self.endereco, "w", encoding='utf-8')
        arquivo.write(doc.toprettyxml(indent='   '))

    def adicionaSubcategoria(self, categoria_id, add):
        add['id'] = len(self.id[categoria_id]['sub_lista'])
        add['status'] = 1
        self.id[categoria_id]['sub_status'] = 1
        self.id[categoria_id]['sub_lista'].append(add)

    def subGetAtivos(self, cat):
        ativos = []
        for item in range(len(self.id[cat]['sub_lista'])):
            if self.id[cat]['sub_lista'][item]['status']:
                ativos.append(
                    {
                        'id': self.id[cat]['sub_lista'][item]["id"],
                        'nome': self.id[cat]['sub_lista'][item]["nome"],
                    }
                )
        return ativos

    def getId(self, nome):
        for item in self.id:
            if item["nome"] == nome:
                return item["id"]

    def getSubId(self, cat, nome):
        for item in self.id[cat]['sub_lista']:
            if item["nome"] == nome:
                return item["id"]

class Pagamento:

    def __init__(self, config):
        self.id = [
            {
                'id': 0,
                'nome': 'Dinheiro',
                'status': 1,
                'ordem': 0
            },
            {
                'id': 1,
                'nome': 'Débito',
                'status': 0,
                'ordem': 1
            },
            {
                'id': 2,
                'nome': 'Crédito',
                'status': 0,
                'ordem': 2
            },
            {
                'id': 3,
                'nome': 'Vale',
                'status': 0,
                'ordem': 3
            }
        ]

        if config['banco'] == 'sim':
            self.id[1]['status'] = 1

        if config['credito'] == 'sim':
            self.id[2]['status'] = 1

        if config['vale'] == 'sim':
            self.id[3]['status'] = 1


    def getAtivos(self):
        ativos = []  # lista vazia para abrigar os itens ativos
        for item in range(len(self.id)):
            if self.id[item]["status"]:
                ativos.append(
                    {
                        'id': self.id[item]["id"],
                        'nome': self.id[item]["nome"],
                        'ordem': self.id[item]["ordem"]
                    }
                )
        return ativos