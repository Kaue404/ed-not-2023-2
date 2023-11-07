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
lista.insert(0, 'morango')
print(lista)