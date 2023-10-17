from lib. stack import Stack
from data.nomes import nomes

p = Stack()

# Inversão da ordem dos nomes

# Empilhamento
for nome in nomes:
    p.push(nome)

lista_inversa = []

# Desempilhamento
while not p.is_empty():
    lista_inversa.append(p.pop())

# Imprime lista inversa
print(lista_inversa)