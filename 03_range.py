# range() é uma função que gera uma fatia de números
# É muito usada em associação de listas.

#1) range() com 1 parâmentro: gera uma faixa que vai de 
#   0 (zero) até o valor parâmetro -1
for num in range(10):
    print(num)

print("-" * 40)

#2) range() com 2 parâmetros: gera uma sequência começando
#   pelo valor do primeiro parâmetro (inclusive) e indo até
#   o valor do segundo parâmetro (exclusive, NÃO ENTRA)
for i in range (10, 15):
    print(i)

print("-" * 40)

#3) range() com 3 parâmetros: 
#   1°: limite inferior (inclusive)
#   2°: limite superior (exclusive, NÃO ENTRA)
#   3°: passo (de quanto em quanto a sequência vai saltar; PODE SER NEGATIVO)
for i in range(1, 22, 3): # De 1 a 21 saltando de 3 em 3
    print(i)

print("-" * 40)

# range() com passso negativo
for i in range(10, 0, -1): # Contagem regressiva de 10 a 1
    print(i)