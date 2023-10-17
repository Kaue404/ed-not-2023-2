from lib.stack import Stack

# Criando uma nova pilha
pilha = Stack()

palavra = "LARANJA"

# Empilhando as letras da palavra
for letra in palavra:
    pilha.push(letra)
    print(pilha)