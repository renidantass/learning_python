# coding:utf-8
"""
    Exercícios de: https://github.com/pythoneiros/Exercicios#lista-de-exercícios-já-propostos
    Diário com colunas contendo texto | data
"""
import json
import time
import os


class Diary:
    def __init__(self):
        self.date = time.strftime('%d-%m-%Y', time.gmtime())
        self.hour = time.strftime('%H-%M-%S', time.gmtime())
        self.check()

    def write(self):
        while 1:
            tmp = raw_input("O dia hoje foi: ").decode('latin-1').encode('utf-8')
            if tmp == 'exit':
                exit(0)
            with open('diario.json', 'a+') as f:
                modelo = [{'data': self.date, 'hora': self.hour, 'conteudo_mensagem': tmp}]
                json.dump(modelo, f)

    def check(self):
        return 1 if os.path.exists('diario.json') else 0

d = Diary()
d.write()
