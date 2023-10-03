# Variáveis de estatística
comps = trocas = passd = 0

def quick_sort(lista, ini = 0, fim = None):
    """
        ALGORITMO DE ORDENAÇÃO QUICK SORT

        Escolhe um dos elementos da lista para ser o pivô (na nossa
        implementação, será  o último elemento) e, na primeira
        passada, divide a lista, a partir da posição final do pivô,
        em uma sublista à esquerda, contendo apenas valores menores
        que o pivô, e outra sublista à direita, que contém apenas
        valores maiores que o pivô.
        Em seguida, recursivamente, repete o processo em cada uma das
        sublistas, até que toda a lista esteja ordenada.
    """

    # Quando não soubermos o valor da variável "fim",  atribuímos a
    # ela o valor da última posição da lista

    if fim is None: fim = len(lista) - 1

    print(f"ini = {ini}, fim = {fim}")

    # Para que o algoritmo trabalhe, é necessário que a faixa delimitada
    # pelas veriáveis "ini" e "fim" tenha, pelo menos, dois elementos.
    # Caso contrário, saímos da fução sem fazer nada
    if fim <= ini : return

    global comps, trocas, passd

    # Inicialização das variáveis
    pivot = fim
    div = ini - 1

    passd += 1      # Entrou na função, conta uma passada

    # Percorre a lista da posição "ini" até a posição "fim" - 1
    for pos in range(ini,fim):
        # Se o elemento da posição "pos" for MENOR que o elemento da
        # posição "pivot", executa algumas ações
        comps += 1
        if lista[pos] < lista[pivot]:
            div += 1    # Chega o "div" uma posição para a frente

            # Efetua a troca entre os elementos das posições "pos" e "div",
            # desde que essas variáveis tenham valor distinto entre si
            comps += 1
            if pos != div  and lista[pos] < lista[div]:
                lista[pos], lista[div] = lista[div], lista[pos]
                trocas += 1

    
    # Depois que "pos" chega em sua posição final, "div" deve ser
    # incrementado uma última vez
    div += 1

    # Caso os valores das posições "pivot" e "div" sejam diferentes entre
    # si, efetua a troca mútua dos elementos nessas posições, caso o
    # primeiro seja menor que o segundo
    comps += 1
    if pivot != div and lista[pivot] < lista[div]:
        lista[pivot], lista[div] = lista[div], lista[pivot]
        trocas += 1

    # NESTE PONTO, O ELEMENTO DA POSIÇÃO "div" ESTÁ EM SEU LOCAL CORRETO
    
    # Chamamos recursivivamente a função para ordernar a sublista à esquerda
    # da posição "div"
    quick_sort(lista, ini, div - 1)

    # A mesma coisa, só que para a sublista à direita de "div"
    quick_sort(lista, div + 1, fim)

####################################################################################

nums = [7, 5, 9, 0, 3, 4, 8, 1, 6, 2]

comps = trocas = passd = 0
quick_sort(nums)
print(nums)
print (f"Comparações: {comps}, trocas: {trocas}, passadas: {passd}")

####################################################################################


# TESTE COM O ARQUIVO DE 1M+ NOMES

# import sys
# sys.dont_write_bytecode = True #Impede a criação do cache

# Importando a lista de nomes
# from data.nomes_desord import nomes
# from time import time

# nomes10000 = nomes[:10000]

# hora_ini = time()
# quick_sort(nomes)
# hora_fim = time()
# print(nomes)    # Lista após ordenação
# print(f"Tempo gasto {(hora_fim - hora_ini) * 1000}ms\n") 
# print (f"Comparações: {comps}, trocas: {trocas}, passadas: {passd}")