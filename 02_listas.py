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

print("-" * 40)

#5) SUBSTITUINDO VALORES EXISTENTES

print("ANTES: ", legumes)

#Substituindo o valor da posição 3
legumes[3]= "vagem"
#Substituindo o valor da posição 0
legumes[0]= "mandioca"
#Substituindo o valor da última posição
legumes[-1]= "milho"

print("DEPOIS: ", legumes)

print("-" * 40)

#6) DETERMINANDO A QUANTIDADE DE ELEMENTOS NA LISTA: len()
print("Número de elementos na lista de valores: ", len(valores))
print("Número de elementos na lista de legumes: ", len(legumes))

print("-" * 40)

#7) REMOVENDO O ÚLTIMO ELEMENTO DE UMA LISTA: pop()
print("ANTES: ", valores)
removido = valores.pop()
print("valor removido: ", removido)
print("DEPOIS: ", valores)

print("-" * 40)

#8) REMOVENDO UM ELEMENTO POR SUA POSIÇÃO: pop() com parâmentro
removido = valores.pop(3) #Remove o elemento da posição 3
print("Valor removido da posição 3: ", removido)
print(valores)
removido = valores.pop(0) #Remove o primeiro elemento
print("Valor removido da primeira posição: ", removido)
print(valores)

print("-" * 40)

#9) REMOVENDO UM ELEMENTO PELO SEU VALOR: remove()
print("ANTES: ", legumes)
legumes.remove("abobrinha")
print("APÓS REMOÇÃO DE abobrinha: ", legumes)

print("-" * 40)

# Acrescentando alguns legumes para aumentar a lista
legumes.append("beterraba")
legumes.append("abobrinha")
legumes.append("batata doce")
legumes.append("mandioquinha")
legumes.append("cará")
legumes.append("nabo")

#10) FATIANDO UMA LISTA
#    fatiar significa copiar uma parte da lista (uma sublista) para uma nova lista

print(legumes)

# Cria uma sublista que contém os elementos da posição 2 até a posição 7
# (posição 8 NÃO entra)
sublista2_7 = legumes[2:8]
print("Sublista de 2 a 7: ", sublista2_7)

# Cria uma sublista que contém os elementos do início até a posição 5
# (posição 6 NÃO entra)
sublista0_5 = legumes[:6]
print("Sublista de 0 a 5: ", sublista0_5)

# Cria uma sublista que contém os elementos da posição 8 até o final
sublista8_fim = legumes[8:]
print("Sublista de 8 até o fim: ", sublista8_fim)