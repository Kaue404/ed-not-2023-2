comps = 0

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
    global comps # Use a variável compsdo escopo global
    comps = 0

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
            comps += 1
            return meio
        
        #Senão, se o valor de busca é MENOR do que o valor
        #do meio, reinicia a busca na metade esquerda da lista
        elif val < lista[meio]:
            comps += 2
            fim = meio - 1

        #Por fim, se o valor de busca é MAIOR que o valor
        #do meio, reiniciado a busca na metade direita da (sub)lista
        else:
            comps += 2
            ini = meio + 1

    #Se chegamos até esse ponto, o valor de busca NÃO EXISTE na lista
    return -1

##################################################################

# Para a busca binária, a lista PRECISA estar ordenada
nums = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 47]

print(nums)

pos11 = busca_binaria(nums, 11)
print(f"Valor 11 encontrado na poisção {pos11}")

pos41 = busca_binaria(nums, 41)
print(f"Valor 41 encontrado na poisção {pos41}")

pos8 = busca_binaria(nums, 8)
print(f"Valor 8 encontrado na poisção {pos8}")

print("-" * 40)

# FAZENDO A BUSCA EM UM ARQUIVO COM 1M+ NOMES

# Importando a lista de nomes
import sys
sys.dont_write_bytecode = True #Impede a criação do cache

from data.nomes import nomes
from time import time

# Buscando o nome EDSON PEREIRA
hora_ini = time()
pos1 = busca_binaria (nomes, 'EDSON PEREIRA')
hora_fim = time()
print(f"EDSON PEREIRA encontrado na posição' {pos1}, comparações: {comps}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms\n")

# Buscando o nome MARIA PEREIRA
hora_ini = time()
pos2 = busca_binaria (nomes, 'MARIA PEREIRA')
hora_fim = time()
print(f"MARIA PEREIRA encontrado na posição' {pos2}, comparações: {comps}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms\n")

# Buscando o nome VALDIR SILVA
hora_ini = time()
pos3 = busca_binaria (nomes, 'VALDIR SILVA')
hora_fim = time()
print(f"VALDIR SILVA encontrado na posição' {pos3}, comparações: {comps}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms\n")

# Buscando o nome GILCICLEIDE GARCIA
hora_ini = time()
pos4 = busca_binaria (nomes, 'GILCICLEIDE GARCIA')
hora_fim = time()
print(f"GILCICLEIDE GARCIA encontrado na posição' {pos4}, comparações: {comps}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms\n")

# Buscando o nome AADRIANA LIMA
hora_ini = time()
pos4 = busca_binaria (nomes, 'AADRIANA LIMA')
hora_fim = time()
print(f"AADRIANA LIMA encontrado na posição' {pos4}, comparações: {comps}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms\n")