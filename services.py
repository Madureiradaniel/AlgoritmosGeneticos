from item import *
from individuo import *
from random import *

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

    #retorna uma populacao com itens dizendo se tem ou nao na mochila já com seu fitness
    def gerarPopulacao(self,itens,qtdInicialDeIndividuos):
        self.populacao = []
        for i in range(qtdInicialDeIndividuos):
            self.individuo =  Individuo(itens)
            self.individuo.calculaFitness()
            self.populacao.append(self.individuo)
        return self.populacao


    #so existirao individuos validos, que nao ultrapassaraqm a capacidade da mochila
    def dizimacao(self,populacao, pesoMaximoDaMochila):

        removidos = []
        for individuo in populacao:
            if individuo.fitness > pesoMaximoDaMochila:
                removidos.append(individuo)
        print("Individos Removidos -> " + str(len(removidos)))

        for individuo in removidos:
            populacao.remove(individuo)

        return populacao


    #reproducao aleatoria
    def reproducao(self,populacao,taxaReproducao):

        #selecionar de acordo com a taxa
        qtdIndividuos = round(len(populacao) * taxaReproducao)

        #so numeros pares
        if qtdIndividuos % 2 == 0:
            qtdIndividuos
        else:
            qtdIndividuos -= 1

        individuosSelecionados = []
        for i in range(qtdIndividuos):
            individuosSelecionados.append(populacao[randint(1,qtdIndividuos)])


        ponto = randint(1,len(individuosSelecionados[0].pack))
        print("Ponto do Cruzamento: " + str(ponto))

        print("= = = = = CRUZAMENTO = = = = =")
        #cruzamento
        for individuo in range(len(individuosSelecionados)):
            if individuo % 2 == 0:
                continue
            else:
                print("========pais=======")
                print(individuosSelecionados[individuo].pack)
                print(individuosSelecionados[individuo - 1].pack)
                for p in range(ponto):
                   individuosSelecionados[individuo].pack[p] = individuosSelecionados[individuo - 1].pack[p]
                   individuosSelecionados[individuo - 1].pack[p] = individuosSelecionados[individuo].pack[p]

                print("========Filho======")
                print(individuosSelecionados[individuo].pack)
                individuosSelecionados[individuo].calculaFitness()
                populacao.append(individuosSelecionados[individuo])

        return populacao

    def mutacao(self,populacao):

        ponto = randint(0,5)

        individuoEscolhido = populacao[randint(1,(len(populacao) - 1))]

        if individuoEscolhido.pack[ponto][1] == 0:
            individuoEscolhido.pack[ponto][1] = 1
        else: individuoEscolhido.pack[ponto][1] = 0

        individuoEscolhido.calculaFitness()

        return populacao

    def criterioParada(self,populacao,criterioParada, capacidadeMochila, melhorBenefico):

        for individuo in populacao:
            if individuo.fitness == capacidadeMochila:
                print("************Otima solucao************")
                print(str(individuo.pack) + "Fitness: " + str(individuo.fitness) +"Beneficio: " + str(individuo.beneficio) )
                criterioParada = 0
                break

        return criterioParada


    def mostrarPopulacao(self,populacao):
        cont = 1
        for individuo in populacao:
            print("Individuo: "+str(cont)+" itens: " + str(individuo.pack) + " Fitness(Peso Total): " + str(individuo.fitness) + " Beneficio: " + str(individuo.beneficio))
            cont += 1

