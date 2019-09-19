from random import randint

#cria um individuo aleatorio, ou seja fala se contem um item ou nao na mochila
class Individuo(object):

    def __init__(self,itens):

        self.pack = []
        for item in itens:
            self.cromossomo = randint(0,1)
            self.pack.append([item,self.cromossomo])

