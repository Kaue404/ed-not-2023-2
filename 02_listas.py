#LISTAS
#Listas são uma forma de armazenar mais de um valor em uma
#única variável. Os valores podem ser de tipos diferentes.

#Uma Lista de númeoros 
valores = [2, 3, 5, 7, 9, 11]

#Uma Lista com valores de tipos variados
mix = ["batata", 1.25, True, "Tomate", 44]

#Lista de strings
legumes = ["batata", "tomate", "abobrinha", "cenoura"]

# OPERAÇÕES SOBRE LISTAS

# 1) PERCURSO: significa percorrer a lista do primeiro ao
# último elemento, fazendo algo com cada um deles.

# Imprimindo cada um dos elementos da Lista, um por linha:
for val in valores:
    print(val)

print("-" * 40) #Traço de 40 hífens

#Imprimindo o dobro do valor de cada elemento da lista
for x in valores:
    print(x * 2)

print("-" * 40) #Traço de 40 hífens

# 2) INSERINDO UM NOVO ELEMENTO NO *FIM* DA LISTA

valores.append (15)
legumes.append ("cebola")

print(valores)
print(legumes)

# 3) INSERINDO UM NOVO ELEMENTO EM UMA POSIÇÕES ESPECIFICADA
#   Parâmetros:
#   1°: a posição onde sera inserindo o novo elemento
#   2°: o novo elemento a ser inserido

legumes.insert(2, "mandioquinha")
print(legumes)
legumes.insert(0, "beterraba")
print(legumes)

print("-" * 40)

# 4) ACESSANDO UM VALOR EM UMA POSIÇÃO ESPECÍFICA 
print("Elementos na QUARTA posição: ", valores[3])
print("Elemento na PRIMEIRA posição: ", valores[0])
print("Elemento na ÚLTIMA posição: ", valores[-1])
print("Elemento na PENÚLTIMA posição: ", valores[-2])
