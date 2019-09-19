from services import *

def main():
    servicos = Services()

    # variaveis que podem ser alteradas pelo usuario
    pesoMaximoDaMochila = 25
    melhorBeneficio = 500
    qtdInicialDeIndividuos = 10
    numeroDeGeracoes = 50
    taxaReproducao = 0.5 #procentagem

    #lendo arquivo itens.txt

    itens = servicos.lerItens()
    populacao = servicos.gerarPopulacao(itens,qtdInicialDeIndividuos)
    #populacao = servicos.dizimacao(populacao,pesoMaximoDaMochila)

    servicos.reproducao(populacao,taxaReproducao)
    #servicos.mostrarPopulacao(populacao)

if __name__ == "__main__":
    main()