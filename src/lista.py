from xml.dom.minidom import parse
import xml.dom.minidom

# classe geral das listas geradas pelos arquivos .xml

class Lista:

    def __init__(self, arquivo):
        endereco = "data/"+arquivo+".xml"
        arvore = xml.dom.minidom.parse(endereco)
        self.lista = arvore.documentElement

#subclasse da Lista, específica para a lista de pessoas
class ListaPessoa(Lista):

    def __init__(self, arquivo):
        Lista.__init__(self, arquivo)
        pessoas = self.lista.getElementsByTagName("pessoa") #gera uma lista de pessoas
        num = len(pessoas)
        self.id = [Pessoa()]*num
        for pessoa in pessoas: #para cada item da lista de pessoas, cria um objeto Pessoa, com os atributos definidos
            indice = int(pessoa.getAttribute("id"))
            nome = pessoa.getElementsByTagName("nome")[0]
            status = pessoa.getElementsByTagName("status")[0]
            ordem = pessoa.getElementsByTagName("ordem")[0]
            self.id[indice].id=indice
            self.id[indice].nome = nome.childNodes[0].data
            self.id[indice].status = int(status.childNodes[0].data)
            self.id[indice].ordem = int(ordem.childNodes[0].data)

#classe para organizar os dados das pessoas
class Pessoa:

    def __init__(self):
        print("Nova")
        self.id = 0
        self.status = 0
        self.ordem = 0
        self.nome = ""