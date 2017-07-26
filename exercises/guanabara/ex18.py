# coding:utf-8
""" 
    Exercícios proposto por: https://www.youtube.com/channel/UCrWvhVmt0Qac3HgsjQK62FQ
    Canal Curso Em Vídeo
    Profº Gustavo Guanabara
"""
import math


angulo = float(raw_input("Digite o ângulo: "))
angulo = math.radians(angulo)
seno = math.sin(angulo)
cos = math.cos(angulo)
tg = math.tan(angulo)
angulo = math.degrees(angulo)
print "Sen {}º: {:.2f} \nCos {}º: {:.2f}\nTg {}º: {:.2f}" .format(angulo, seno, angulo, cos, angulo, tg)
