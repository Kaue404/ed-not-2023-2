"""
    Dicionário é uma estrutura de dados fornecida pela linguagem Python,
    capaz de armazenar múltiplos valores em uma única variável, por meio
    de pares de chave-valor (key-value).

    Um dicionário é delimitado por chaves{}. Diferentemente das listas,
    que têm posições numeradas, os dicionários possuem posições NOMEADAS.
    Cada um das posições nomeadas de um dicionário (ou seja, um par
    chave-valor) é chamado de PROPRIEDADE. 
"""

pessoa = {
    # "chave" : valor
    "nome": "Orozimbo Oliveira Osório", # -> propiedade
    "sexo": "M",
    "idade": 89,
    "peso": 76,
    "altura": 1.66,
    "aposentado": True,
    "filhos": ["Zeferina", "Asdrúbal", "Gercina"]
}

# Acessandoo os valores armazenados no dicionário
print("Nome: ", pessoa["nome"])
print("Idade: ", pessoa["idade"])
print("Aposentado? ", pessoa["aposentado"])

# Calculando o IMC (Índice de Massa Corporal)
imc = pessoa["peso"] / pessoa["altura"] ** 2 # ** = ^

# Dentro de aspas duplas, é necessário usar aspas simples
print(f"O IMC de {pessoa['nome']} é {imc}.")

###############################################################

# Representações formas geométricas planas

forma1 = {
    "base": 7.5,
    "altura": 12,
    "tipo": "R" #Retãngulo
}
forma2 = {
    "base": 6,
    "altura": 2.5,
    "tipo": "T" # Triângulo
}
forma3 = {
    "base": 5,
    "altura": 3,
    "tipo": "E" # Elipse / círculo
}
forma4 = {
    "fruta": 10,
    "legume": 7,
    "tipo": "T" 
}
forma5 = {
    "base": "tomate",
    "altura": False,
    "tipo": 16 
}

from math import pi

def calcular_area(forma):
    if forma["tipo"] == "R": # Retângulo
        return forma["base"] * forma["altura"]
    elif forma ["tipo"] == "T": # Triângulo
        return forma["base"] * forma["altura"] / 2
    elif forma ["tipo"] == "E": # Elipse/Círculo
        return(forma["base"] / 2) * (forma["altura" / 2]) * pi
    else:
        return None
    
####################################################################

# Calculando a área das formas

print(f"Base: {forma1['base']}; altura: {forma1['altura']}; tipo: {forma1['tipo']}; área: {calcular_area(forma1)}")

print(f"Base: {forma2['base']}; altura: {forma2['altura']}; tipo: {forma2['tipo']}; área: {calcular_area(forma2)}")

print(f"Base: {forma3['base']}; altura: {forma3['altura']}; tipo: {forma3['tipo']}; área: {calcular_area(forma3)}")

print(f"Base: {forma4['base']}; altura: {forma4['altura']}; tipo: {forma4['tipo']}; área: {calcular_area(forma4)}")

print(f"Base: {forma5['base']}; altura: {forma5['altura']}; tipo: {forma5['tipo']}; área: {calcular_area(forma5)}")