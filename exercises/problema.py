# coding:utf-8
"""
    Exercícios de: https://github.com/pythoneiros/Exercicios#lista-de-exercícios-já-propostos
"""


print "\n-----------------------------------------------------"
print "Separador de pares e ímpares\n"

numeros = raw_input("Insira alguns números separados por espaço para \n que eu possa separar os pares dos ímpares\n\n:-) -> ").split(',')

pares = impares = []

for numero in numeros:
    if int(numero) % 2 == 0:
        pares.append(numero)
    impares.append(numero)

print "\nNumeros pares: %s"  %(pares)
print "Numeros impares: %s"  %(impares)