comps = trocas = passd = 0

def bubble_sort(lista):
    """
    ALGORITMO DE ORDENAÇÃO BUBBLE SORT
    Percorre a lista a ser ordenada em sucessivas passadas,
    trocando entre si dois elementos adjacentes sempre que
    o segundo for MENOR que o primeiro. Efetua tantas
    passadas quanto necessárias, até que, na última delas,
    nenhuma troca tenha sido realizada

    ESTÁ VERSÃO TEM UMA PEQUENA OTIMIZAÇÃO QUE VAI DIMINUINDO 
    A QUANTIDADE DE COMPARAÇÕES A CADA PASSADA.
    """

    # Usando as variáveis globais
    global comps, trocas, passd
    comps = trocas = passd = 0

    # Loop eterno, não sabemos de antemão quantas passadas
    # serão necessários
    while True:

        #Inicio de uma nova passada
        passd +=1

        # Controlada se houve trocas no passado
        trocou = False

        # Percusso da lista, do primeiro ao PENÚLTIMO elemento,
        # com acesso a cada posição, NA PRIMEIRA PASSADA
        # Nos demais passadas, o percurso vai diminuindo uma posição
        for pos in range(len(lista) - 1):

            # Se o número que está à frente na lista (pos + 1)
            # for MENOR do que aquele que está atrás (pos),
            # faz uma TROCA
            if lista[pos + 1] < lista[pos]:
                lista[pos + 1], lista[pos] = lista[pos], lista[pos + 1]
                trocou = True #Houve troca na passada
                trocas += 1

            # O if representa uma comparação
            comps += 1

        if not trocou:      # Não houve troca na passada
            break           # Interrompe o loop eterno

########################################################################

#Caso intermediário
nums = [7, 5, 9, 0, 3, 4, 8, 1, 6, 2]

#Melhor caso
#nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#Pior caso
#nums = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

print("ANTES: ", nums)
bubble_sort(nums)
print("DEPOIS: ", nums)
print(f"Comparações: {comps}, trocas: {trocas}, passadas: {passd}")

#######################################################################
# TESTE COM O ARQUIVO DE 1M+ NOMES

import sys
sys.dont_write_bytecode = True #Impede a criação do cache

#Importando a lista de nomes
from data.nomes_desord import nomes
from time import time

nomes10000 = nomes[:10000]

hora_ini = time()
bubble_sort(nomes10000)
hora_fim = time()
print(nomes10000)    # Lista após ordenação
print(f"Tempo gasto {(hora_fim - hora_ini) * 1000}ms\n")