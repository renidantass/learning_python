# coding:utf-8
"""
    Exercícios de: https://github.com/pythoneiros/Exercicios#lista-de-exercícios-já-propostos
"""


def dividir(args, quant):
    grupos = []
    quantidade_grupo = len(args) // quant
    idx = 0
    while idx < len(args):
        grupo = args[idx:quantidade_grupo + idx]
        grupos.append(grupo)
        idx += quantidade_grupo
    return grupos

print dividir([1,2,3,4,5,6,7,8], 2)
