import time
import xml.dom.minidom
from xml.dom import minidom


# classe geral das listas geradas pelos arquivos .xml

class Lista:

    def __init__(self, nome):
        self.endereco = "data/" + nome + ".xml"
        arquivo = xml.dom.minidom.parse(self.endereco)
        lista = arquivo.documentElement  # lê o nó <lista> do arquivo
        self.itens = lista.getElementsByTagName(nome)  # gera a lista de nós de cada item
        self.id = []  # lista vazia para abrigar os itens

    def adiciona(self, add):
        add['id'] = len(self.id)
        add['status'] = 1
        self.id.append(add)

    def reordena(self, posicao):
        for item in self.id:
            if item['ordem'] >= posicao:
                item['ordem'] += 1

    def edita(self, index, nome, ordem_nova, status):
        ordem_velha = self.id[index]['ordem']
        self.id[index]['nome'] = nome
        self.id[index]['status'] = status
        if ordem_nova > ordem_velha:
            for item in self.id:
                if ( item['ordem'] > ordem_velha) and (item['ordem'] <= ordem_nova):
                    item['ordem'] -= 1
        else:
            for item in self.id:
                if ( item['ordem'] >= ordem_nova) and (item['ordem'] < ordem_velha):
                    item['ordem'] += 1
        self.id[index]['ordem'] = ordem_nova

class ListaPessoa(Lista):

    def __init__(self, nome):
        super().__init__(nome)

        for item in self.itens:  # para cada item da lista, cria um dicionário com os atributos definidos
            nome = item.getElementsByTagName("nome")[0]
            status = item.getElementsByTagName("status")[0]
            ordem = item.getElementsByTagName("ordem")[0]
            self.id.append(
                {
                    'id': int(item.getAttribute("id")),
                    'nome': nome.childNodes[0].data,
                    'status': int(status.childNodes[0].data),
                    'ordem': int(ordem.childNodes[0].data)
                }
            )

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

    def salva(self):
        doc = minidom.Document()  # cria um objeto xml
        # adiciona um comentário com o horário de criação
        doc.appendChild(doc.createComment("Criacao: %s" % time.asctime(time.localtime(time.time()))))
        lista = doc.createElement('lista')  # cria uma lista xml de doc
        for indice in self.id:  # adiciona cada nó na lista de doc
            item = doc.createElement('pessoa')
            item.setAttribute('id', str(indice['id']))
            lista.appendChild(item)

            nome = doc.createElement('nome')
            item.appendChild(nome)
            nome.appendChild(doc.createTextNode(indice['nome']))

            status = doc.createElement('status')
            item.appendChild(status)
            status.appendChild(doc.createTextNode(str(indice['status'])))

            ordem = doc.createElement('ordem')
            item.appendChild(ordem)
            ordem.appendChild(doc.createTextNode(str(indice['ordem'])))

        doc.appendChild(lista)

        arquivo = open(self.endereco, "w", encoding='utf-8')
        arquivo.write(doc.toprettyxml(indent='   '))


class ListaCategoria(Lista):

    def __init__(self, nome):
        super().__init__(nome)

        for item in self.itens:  # para cada item da lista, cria um dicionário com os atributos definidos
            nome = item.getElementsByTagName("nome")[0]
            status = item.getElementsByTagName("status")[0]
            ordem = item.getElementsByTagName("ordem")[0]
            sub_status = item.getElementsByTagName("sub_status")[0]

            sub_lista = item.getElementsByTagName("sub_lista")[0]
            sub_cats = sub_lista.getElementsByTagName("sub")

            sub = []  # cria a lista para abrigar as subcategorias

            for sub_cat in sub_cats:  # para cada sub_categorias da lsta, cria um dicionário com os atributos
                snome = sub_cat.getElementsByTagName("nome")[0]
                sstatus = sub_cat.getElementsByTagName("status")[0]
                sordem = sub_cat.getElementsByTagName("ordem")[0]

                sub.append(
                    {
                        'id': int(sub_cat.getAttribute("id")),
                        'nome': snome.childNodes[0].data,
                        'status': int(sstatus.childNodes[0].data),
                        'ordem': int(sordem.childNodes[0].data),
                    }
                )

            self.id.append(
                {
                    'id': int(item.getAttribute("id")),
                    'nome': nome.childNodes[0].data,
                    'status': int(status.childNodes[0].data),
                    'ordem': int(ordem.childNodes[0].data),
                    'sub_status': int(sub_status.childNodes[0].data),
                    'sub_lista': sub
                }
            )

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
                        'ordem': self.id[item]["ordem"],
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

            ordem = doc.createElement('ordem')
            item.appendChild(ordem)
            ordem.appendChild(doc.createTextNode(str(indice['ordem'])))

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

                    ordem = doc.createElement('ordem')
                    sitem.appendChild(ordem)
                    ordem.appendChild(doc.createTextNode(str(sub_cat['ordem'])))

        doc.appendChild(lista)

        arquivo = open(self.endereco, "w", encoding='utf-8')
        arquivo.write(doc.toprettyxml(indent='   '))

    def adicionaSubcategoria(self, categoria_id, add):
        add['id'] = len(self.id[categoria_id]['sub_lista'])
        add['status'] = 1
        self.id[categoria_id]['sub_status'] = 1
        self.id[categoria_id]['sub_lista'].append(add)

    def reordenaSubcategoria(self, categoria_id, posicao):
        for item in self.id[categoria_id]['sub_lista']:
            if item['ordem'] >= posicao:
                item['ordem'] += 1

    def subGetAtivos(self, cat):
        ativos = []
        for item in range(len(self.id[cat]['sub_lista'])):
            ativos.append(
                {
                    'id': self.id[cat]['sub_lista'][item]["id"],
                    'nome': self.id[cat]['sub_lista'][item]["nome"],
                    'ordem': self.id[cat]['sub_lista'][item]["ordem"],
                }
            )
        return ativos


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