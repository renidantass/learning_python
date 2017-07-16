# coding:utf-8
"""
    Exercícios de: https://github.com/pythoneiros/Exercicios#lista-de-exercícios-já-propostos
"""


def vetor(args):
    pars, imps = [], []
    for arg in args:
        if arg % 2 == 0:
            pars.append(arg)
        imps.append(arg)
    print "Pares: ", pars
    print "Impares: ", imps

vetor([2, 4, 3])