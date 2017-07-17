# coding:utf-8
"""
    Exercícios de: https://github.com/pythoneiros/Exercicios#lista-de-exercícios-já-propostos
"""


def dividir(args, vezes):
    dividido = []
    tam_lista = len(args)
    for i in range(vezes):
        start = int(i*tam_lista/vezes)
        end = int((i+1)*tam_lista/vezes)
        dividido.append(args[start:end])
    return dividido

print dividir([1,2,3,4,5,6,7,8,9], 3) # Example
