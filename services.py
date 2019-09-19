from item import *
from individuo import *

class Services(object):

    #pega os itens do arquivo txt (nome,beneficio,peso)
    def lerItens(self):
        itens = []
        arquivo = open('itens.txt', 'r')

        for linha in arquivo:
            row = linha.replace("\n","").split(",")
            item = Item(row[0],row[1],row[2])
            itens.append(item)
        arquivo.close()

        return itens

    #retorna uma populacao com itens dizendo se tem ou nao na mochila
    def gerarPopulacao(self,itens,qtdInicialDeIndividuos):
        self.populacao = []
        for i in range(qtdInicialDeIndividuos):
            self.individuo =  Individuo(itens)
            self.populacao.append(self.individuo)
        return self.populacao

    def mostrarPopulacao(self,populacao):
        cont = 1
        for individuo in populacao:
            print("Individuo: "+str(cont)+" itens: " + str(individuo.pack) + " Fitness(Peso Total): " + str(individuo.fitness))
            cont += 1

