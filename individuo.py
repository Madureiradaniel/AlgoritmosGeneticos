from random import randint

class Individuo(object):

    def __init__(self,itens):
        self.pack = []
        self.fitness = 0
        self.beneficio = 0

        #gera random qual item leva no pack(mochila)
        for item in itens:
            cromossomo = randint(0,1)
            self.pack.append([item,cromossomo])

    def calculaFitness(self):
        self.fitness = 0
        self.beneficio = 0
        for item in self.pack:
            if item[1] == 1:
                self.fitness += int(item[0].peso)
                self.beneficio += int(item[0].beneficio)



