# coding:utf-8
""" 
    Exercícios proposto por: https://www.youtube.com/channel/UCrWvhVmt0Qac3HgsjQK62FQ
    Canal Curso Em Vídeo
    Profº Gustavo Guanabara
"""
from playsound import playsound
from os.path import exists
from sys import argv

if exists(argv[1]):
    playsound(argv[1])
else:
    print('arquivo não encontrado')
