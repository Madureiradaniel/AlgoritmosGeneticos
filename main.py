from services import *

def main():
    servicos = Services()

    # variaveis que podem ser alteradas pelo usuario
    pesoMaximoDaMochila = 30
    melhorBeneficio = 200
    qtdInicialDeIndividuos = 20
    taxaReproducao = 0.5 #procentagem
    criterioParada = -1

    #lendo arquivo itens.txt
    itens = servicos.lerItens()

    #gerando populacao
    populacao = servicos.gerarPopulacao(itens,qtdInicialDeIndividuos)

    cont = 1
    while criterioParada == -1:
        print("GERACAO ==== " + str(cont))
        #criterioParada = servicos.criterioParada(populacao, criterioParada, pesoMaximoDaMochila, melhorBeneficio)

        if criterioParada == -1:
            populacao = servicos.reproducao(populacao,taxaReproducao)
            populacao = servicos.mutacao(populacao)
            populacao = servicos.dizimacao(populacao, pesoMaximoDaMochila)
            criterioParada = servicos.criterioParada(populacao, criterioParada, pesoMaximoDaMochila, melhorBeneficio)
            print("GERACAO ==== " + str(cont))
            cont += 1



if __name__ == "__main__":
    main()