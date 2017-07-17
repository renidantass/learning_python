# coding:utf-8
"""
    Exercícios de: https://github.com/pythoneiros/Exercicios#lista-de-exercícios-já-propostos
"""


def move_list(args, times):
    for _ in range(times):
        tmp = args.pop()
        args.insert(0, tmp)
    return args

print move_list([1,2,3], 4) # Example
