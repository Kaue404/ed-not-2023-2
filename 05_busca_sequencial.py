def busca_sequencial(lista,val):
    """
    Funcões que realiza uma busca sequencial em uma lista
    procurando por val.
    Se val for encontrado, retorna a posição de val na lista
    Caso contrário, retorna o valor convencional -1.
    """
    # Pecorre a lista do início ao fim usando range() e len()
    # (precisamos ter acesso às posições dos elementos)
    for pos in range(len(lista)):
        # Encontrou val; retorna a posição onde foi encontrado
        if val == lista[pos]: return pos
    #<-- CUIDADO COM A IDENTAÇÃO AQUI
    # Percorreu toda a lista e não encontrou val: retorna -1
    return -1
##############################################################

# Para a busca sequencial, a lista NÃO PRECISA de estar ordenada
nums = [9, 21, 33, 12, 0, 18, -3, 30, -15, 6, 3, 27]

# TESTES

pos30 = busca_sequencial(nums, 30)
pos_menos3 = busca_sequencial(nums, -3)
pos19 = busca_sequencial(nums, 19)

print(nums)
print(f"Elemento 30 encontrado na posição {pos30}.")
print(f"Elemento -3 encontrado na posição {pos_menos3}.")
print(f"Elemento 19 encontrado na posição {pos19}.")

print('-' * 40)

# FAZENDO A BUSCA EM UM ARQUIVO COM 1M+ NOMES

# Importando a lista de nomes
import sys
sys.dont_write_bytecode = True #Impede a criação do cache

from data.nomes import nomes
from time import time

# Buscando o nome EDSON PEREIRA
hora_ini = time()
pos1 = busca_sequencial (nomes, 'EDSON PEREIRA')
hora_fim = time()
print(f"EDSON PEREIRA encontrado na posição' {pos1}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms\n")

# Buscando o nome MARIA PEREIRA
hora_ini = time()
pos2 = busca_sequencial (nomes, 'MARIA PEREIRA')
hora_fim = time()
print(f"MARIA PEREIRA encontrado na posição' {pos2}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms\n")

# Buscando o nome VALDIR SILVA
hora_ini = time()
pos3 = busca_sequencial (nomes, 'VALDIR SILVA')
hora_fim = time()
print(f"VALDIR SILVA encontrado na posição' {pos3}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms\n")

# Buscando o nome GILCICLEIDE GARCIA
hora_ini = time()
pos4 = busca_sequencial (nomes, 'GILCICLEIDE GARCIA')
hora_fim = time()
print(f"GILCICLEIDE GARCIA encontrado na posição' {pos4}")
print(f"Tempo gasto: {(hora_fim - hora_ini) * 1000}ms\n")