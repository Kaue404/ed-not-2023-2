def calc_imc(peso, altura):
    return peso / altura ** 2

# p = 92
# a = 1.87
# imc = calc_imc(p, a)

# print (imc)

print(calc_imc(85, 1.72))

##################################################

from math import pi

"""
    Função que calcula a área de uma figura geométrica plana
"""

def calc_area(base, altura, tipo):
    resultado = None #Valor não existente

    if tipo == "R": # Retângulo
        resultado = base * altura
    elif tipo == "T": # Triângulo
        resultado = base * altura / 2
    elif tipo == "E": #Elipse
        resultado = (base / 2) * (altura / 2) * pi
    else: #Forma inválida ou desconhecida
        resultado = None

    return resultado 

print ("Retângulo 20x30: ", calc_area(20, 30, "R"))
print ("Triângulo 45x32: ", calc_area(45, 32, "T"))
print ("Elipse 10x15: ", calc_area(10, 15, "E"))
print ("Desconhecido 12x16: ", calc_area(12, 16, "X"))