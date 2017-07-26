# coding:utf-8
""" 
    Exercícios proposto por: https://www.youtube.com/channel/UCrWvhVmt0Qac3HgsjQK62FQ
    Canal Curso Em Vídeo
    Profº Gustavo Guanabara
"""
import math



compr_co = float(raw_input("Comprimento do cateto oposto: "))
compr_ca = float(raw_input("Comprimento do cateto adjacente: "))
hipot_q = (math.pow(compr_co, 2)) + (math.pow(compr_ca, 2))
hipot_q = math.sqrt(hipot_q)
print '{:.2f}'.format(hipot_q)
