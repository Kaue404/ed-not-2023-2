comps = trocas = passd = 0

def selection_sort(lista):
    """
        ALGORITMO DE ORDENAÇÃO SELECTION SORT

        Isola (seleciona) o primeiro elemento da lista e, em seguida,
        encontra o menor valor no restante da lista. Se o valor
        encontra for menor que o valor previamente selecionado,
        efetua a troca entre eles. Continuando, seleciona o segundo
        elemento da lista, buscando pelo menor valor das posições
        subsequentes. Faz a troca entre os doois valores, se necessário.
        O processo se repete até que o penúltimo elemento da lista seja
        isolado, comparado com o último e feita a troca entre eles, se
        for o caso.
    """

    global comps, trocas, passd
    comps, trocas, passd = 0

    # Loop que vai da primeiro até a PENÚLTIMA posição 
    for pos_sel in range(len(lista) - 1):
        passd += 1

        # Inicio supondo que a posição o menor valor do resto da lista
        # é aquela imediatamente subsequente à posição selecionada
        pos_menor = pos_sel + 1


        # Percorre novamente a lista, da posição seguinte a pos_menor
        # até a última posição
        for pos in range(pos_menor + 1, len(lista)):
            # Se o valor encontrado na posiçáo pos for MENOR do que o
            # valor da posição pos_menor, então atualiza pos_menor para
            # a posição de pos
            comps += 1
            if lista[pos] < lista[pos_menor]: pos_menor = pos

        # Neste ponto, já terminamos de percorrer o restante da lista e 
        # já sabemos a posição do menor elemento que há nele. Comparamos,
        # então, os valores das posições pos_menor e pos_sel e, se o
        # primeiro for MENOR que o segundo, fazemos a troca entre eles
        comps += 1
        if lista[pos_menor] < lista[pos_sel]:
            lista[pos_menor], lista[pos_sel] = lista[pos_sel], lista[pos_menor]
            trocas += 1

        # print("PASSADA: ", passd)

################################################################################ 

#nums = [7, 5, 9, 0, 3, 4, 8, 1, 6, 2]

#print("ANTES: ", nums)
#selection_sort(nums)
#print("DEPOIS: ", nums)
#print(f"Comparações: {comps}, trocas: {trocas}, passadas: {passd}")

#######################################################################
# TESTE COM O ARQUIVO DE 1M+ NOMES

import sys
sys.dont_write_bytecode = True #Impede a criação do cache

#Importando a lista de nomes
from data.nomes_desord import nomes
from time import time

nomes10000 = nomes[:10000]

hora_ini = time()
selection_sort(nomes10000)
hora_fim = time()
print(nomes10000)    # Lista após ordenação
print(f"Tempo gasto {(hora_fim - hora_ini) * 1000}ms\n") 