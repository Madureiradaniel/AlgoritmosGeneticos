from services import *

def main():
    servicos = Services()
    # variaveis que podem ser alteradas pelo usuario
    pesoMaximoDaMochila = 22
    qtdInicialDeIndividuos = 10

    itens = servicos.lerItens()
    populacao = servicos.gerarPopulacao(itens,qtdInicialDeIndividuos)

    servicos.mostrarPopulacao(populacao)


if __name__ == "__main__":
    main()