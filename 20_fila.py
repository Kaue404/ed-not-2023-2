from lib.queue import Queue

# Cria uma fila
fila = Queue()

# Insere algumas pessoas na fila
fila.enqueue("Leotildes")
fila.enqueue("Orozimbo")
fila.enqueue("Waldisney")
fila.enqueue("Adamastor")

print(fila)

# Atende uma pessoa
atendido = fila.dequeue()
print(f"Atendido: {atendido}")
print(fila)

# Uma nova pessoa chegou à fila
fila.enqueue("Marcinéia")
print(fila)

# Consultando quem será o próximo a ser atendido,
# sem retirá-lo da fila
proximo = fila.peek()
print(f"Próximo: {proximo}")
print(fila)