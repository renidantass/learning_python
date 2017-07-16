# coding:utf-8
"""
    Exercícios de: https://github.com/pythoneiros/Exercicios#lista-de-exercícios-já-propostos
"""


def main():
    tmp = raw_input("Digite a frase: ")
    if tmp == 'exit':
        exit(0)
    with open('diario.txt', 'a+') as f:
        f.write("%s\n" % tmp)

while 1:
    main()