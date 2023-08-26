def busca_binaria(lista, val):
    """
        ALGORITMO DE BUSCA BINÁRIA
        Dados uma lista, que deve estar PREVIAMENTE ORDENADA,
        e um valor de busca, divide a lista em duas partes,
        procurando pelo valor de busca apenas na metade onde
        o valor poderia estar. Novas subdivisões são feitas
        até que se encontre o valor de busca ou que reste
        apenas uma sublista vazia, quando então se conclui
        que o valor de busca não existe na lista.
    """
    ini = 0             #Início da lista
    fim = len(lista) -1 #Fim da lista

    while ini <= fim:
        #Calculando o meio da lista
        meio = (ini + fim) // 2 #Divisão inteira

        #Verifica se o valor que está no meio da lista
        #é igual ao valor de busca, em caso afirmativo,
        #retornamos a posição do meio, pois o valor de
        #busca foi encontrado.
        if val == lista[meio]:
            return meio
        
        #Senão, se o valor de busca é MENOR do que o valor
        #do meio, reinicia a busca na metade esquerda da lista
        elif val < lista[meio]:
            fim = meio - 1

        #Por fim, se o valor de busca é MAIOR que o valor
        #do meio, reiniciado a busca na metade direita da (sub)lista
        else:
            ini = meio + 1

    #Se chegamos até esse ponto, o valor de busca NÃO EXISTE na lista
    return -1