# coding:utf-8
"""
    Exercícios de: https://github.com/pythoneiros/Exercicios#lista-de-exercícios-já-propostos
"""


from bs4 import BeautifulSoup
import requests


class Scrapping(object):
    def __init__(self, link):
        self.response = None
        self.link = link
        self.__get()
        self.getting_links()

    def getting_links(self):
        soup = BeautifulSoup(self.response, 'html.parser')
        with open('links.txt', 'w') as f:
            for link in soup.find_all('a'):
                f.write("%s\n" % link)

    def __get(self):
        try:
            self.response = requests.get(self.link).text
        except Exception as e:
            raise Exception(e)

s = Scrapping('https://www.google.com.br/?gws_rd=cr,ssl&ei=2sBrWbvtE4GFwQSHl7CYBw')