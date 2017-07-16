# coding:utf-8
"""
    Exercícios de: https://github.com/pythoneiros/Exercicios#lista-de-exercícios-já-propostos
"""
import re


def main():
    default_ip = re.compile(r'^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$')
    with open('lista_ips.txt') as f:
        for line in f:
            if default_ip.match(line):
                with open('ips_validos.txt', 'a+') as vips:
                    vips.write(line)

main()