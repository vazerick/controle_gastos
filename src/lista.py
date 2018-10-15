from xml.dom.minidom import parse
import xml.dom.minidom

# classe geral das listas geradas pelos arquivos .xml

class Lista:

    def __init__(self, nome):
        endereco = "data/"+nome+".xml"
        arquivo = xml.dom.minidom.parse(endereco)
        lista = arquivo.documentElement # lê o nó <lista> do arquivo
        itens = lista.getElementsByTagName(nome)  # gera a lista de nós de cada item

        self.id = [] # lista vazia para abrigar os itens

        for item in itens:  # para cada item da lista, cria um dicionário com os atributos definidos
            nome = item.getElementsByTagName("nome")[0]
            status = item.getElementsByTagName("status")[0]
            ordem = item.getElementsByTagName("ordem")[0]
            self.id.append(
                {
                    'nome': nome.childNodes[0].data,
                    'status': int(status.childNodes[0].data),
                    'ordem': int(ordem.childNodes[0].data)
                }
            )


#indice = int(pessoa.getAttribute("id"))


"""
criar:
    metodos:
        retornar uma lista em ordem das pessoas, para gerar os combos
        adicionar pessoas
            salvar o arquivo após adicionar pessoas
        deletar pessoas (desligar o status)
        ligar pessoas (ligar o status) 
        
ver como fazer com as categorias (deixar as sub-categorias para um próximo passo)    
"""