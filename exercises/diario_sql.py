# coding:utf-8
"""
    Exercícios de: https://github.com/pythoneiros/Exercicios#lista-de-exercícios-já-propostos
"""
import sqlite3
import os
import time


class Diario:
    def __init__(self):
        self.check()
        self.write()

    def create(self):
        conn = sqlite3.connect('diario.db')
        cur = conn.cursor()
        cur.execute('''CREATE TABLE diario (texto text, data text, hora text);''')
        conn.commit()

    def check(self):
        if not os.path.exists('diario.db'):
            self.create()
    
    def write(self):
		try:
			text = raw_input("Hoje meu dia: ")
			date = time.strftime("%d-%m-%Y", time.gmtime())
			hour = time.strftime("%H:%M:%S", time.gmtime())
			conn = sqlite3.connect('diario.db')
			cur = conn.cursor()
			cur.execute('''INSERT INTO diario(texto, data, hora) VALUES('{}', '{}', '{}');'''.format(text, date, hour))
			conn.commit()
		except Exception as e:
			raise Exception(e)

d = Diario()
