class Item(object):

    def __init__(self,nome,beneficio,peso):

        # extamente a ordem do TXT
        self.nome = nome
        self.beneficio = beneficio
        self.peso = peso


    def __repr__(self):
        return str(self.nome)
