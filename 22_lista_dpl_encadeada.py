from lib.doubly_linked_list import DoublyLinkedList

lista = DoublyLinkedList()
print(lista)

lista.insert(0, 'abacate')
lista.insert(1, 'mamão')
lista.insert(2, 'maçã')
lista.insert(3, 'abacaxi')

print(lista)

# Inserção intermediária
lista.insert(2, "ameixa")
print(lista)

# Inserção na primeira posição
# lista.insert(0, 'morango')
lista.insert_front('morango')
print(lista)

# Inserção na última posição
# lista.insert(lista.get_count(), 'jabuticaba')
lista.insert_back('jabuticaba')
print(lista)

# TESTES DE REMOÇÃO

# Remoção da primeira posição
# removido = lista.remove(0)
removido = lista.remove_front()
print(f"Removido da posição 0: {removido}")
print(lista)

# Remoção da última posição
# removido = lista.remove(lista.get_count() - 1)
removido = lista.remove_back()
print(f"Removido da última posição: {removido}")
print(lista)

# Remoção de posição intermediária
removido = lista.remove(2)
print(f"Removido da posição 2: {removido}")
print(lista)

# Tentativa de remoção de uma posição inexistente
# removido = lista.remove(8)

# TESTES DE CONSULTA
primeiro = lista.peek_front()
ultimo = lista.peek_back()
pos2 = lista.peek(2)
print(f"Primeiro: {primeiro}, último: {ultimo}, pos. 2: {pos2}")
print(lista)
