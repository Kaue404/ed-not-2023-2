from lib.stack import Stack

# Criando uma nova pilha
pilha = Stack()

palavra = "LARANJA"

# Empilhando as letras da palavra
for letra in palavra:
    pilha.push(letra)
    print(pilha)

print( '-' * 80 )

inverso = ""

# Desmepilhando e colocando cada letra retirada
# dentro da string inverso
while not pilha.is_empty():
    inverso += pilha.pop()
    print(pilha)

print( '-' * 80 )

print(f"Palavra original: {palavra}")
print(f"Palavra invertida: {inverso}")