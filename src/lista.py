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

class ListaPessoa (Lista):

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
        print(doc.toprettyxml(indent='   '))

        arquivo = open(self.endereco, "w", encoding='utf-8')
        arquivo.write(doc.toprettyxml(indent='   '))

    def getAtivos(self):
        ativos = []  # lista vazia para abrigar os itens ativos
        for item in range(len(self.id)):
            if self.id[item]["status"]:
                ativos.append(
                    {
                        'nome': self.id[item]["nome"],
                        'id': self.id[item]["id"]
                    }
                )
        return ativos

class ListaCategoria (Lista):

    def __init__(self, nome):
        super().__init__(nome)

        for item in self.itens:  # para cada item da lista, cria um dicionário com os atributos definidos
            nome = item.getElementsByTagName("nome")[0]
            status = item.getElementsByTagName("status")[0]
            ordem = item.getElementsByTagName("ordem")[0]
            sub_status = item.getElementsByTagName("sub_status")[0]
            sub_lista = item.getElementsByTagName("sub_lista")[0]
            self.id.append(
                {
                    'id': int(item.getAttribute("id")),
                    'nome': nome.childNodes[0].data,
                    'status': int(status.childNodes[0].data),
                    'ordem': int(ordem.childNodes[0].data),
                    'sub_status': int(sub_status.childNodes[0].data),
                    'sub_lista': sub_lista.childNodes[0].data
                }
            )
            print(self.id)

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
            sub_lista.appendChild(doc.createTextNode(str(indice['sub_lista'])))

        doc.appendChild(lista)
        print(doc.toprettyxml(indent='   '))

        arquivo = open(self.endereco, "w", encoding='utf-8')
        arquivo.write(doc.toprettyxml(indent='   '))

    def getAtivos(self):
        ativos = []  # lista vazia para abrigar os itens ativos
        for item in range(len(self.id)):
            if self.id[item]["status"]:
                ativos.append(
                    {
                        'nome': self.id[item]["nome"],
                        'id': self.id[item]["id"]
                    }
                )
        return ativos

# indice = int(pessoa.getAttribute("id"))


# criar:
#    metodos:
#        retornar uma lista em ordem das pessoas, para gerar os combos
#        adicionar pessoas
#        deletar pessoas (desligar o status)
#        ligar pessoas (ligar o status)
#
# ver como fazer com as categorias (deixar as sub-categorias para um próximo passo)
