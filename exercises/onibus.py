# coding:utf-8
"""
    Create a scrapper to osascoinformatica.com.br that show bus schedule
    by: line number of bus
"""
from bs4 import BeautifulSoup
from operator import itemgetter
from os import path
import requests


class BScheduler(object):
    def __init__(self, link=None):
        self._default_link = 'http://www.osascoinformatica.com.br'
        self.link = self.menu() if link is None else link
        self.response = self._get()
        self.soup = BeautifulSoup(self.response, 'lxml')

    def _get(self):
        try:
            return requests.get(self.link).text
        except Exception as e:
            raise e

    def get_categories(self):
        try:
            response = requests.get('http://www.osascoinformatica.com.br/cmto/index.php').text
            soup = BeautifulSoup(response, 'lxml')
            select = soup.find('select')
            options = select.findAll('option')
            values = [opt['value'] for opt in options if opt['value'] != '/cmto/']
            categories = list(map(lambda x: path.basename(x), values))
            return values
        except Exception as e:
            raise e

    def menu(self):
        cont, cont_cel = 0, 1
        cels = 0
        categories = {idx: category for (idx, category) in enumerate(self.get_categories())}
        print('[opção] <-----> linha do ônibus'.center(55, ' '))
        for category in categories:
            print('[{}] <-----> {}'.center(45, ' ').format(category, path.basename(categories[category])))
        entr = int(input("[Entrada] <--- ".center(40, ' ')))
        if entr in categories:
            print("\033[96mVocê escolheu a linha {}".center(54, ' ').format(path.basename(categories[entr])))
        return '{}{}'.format(self._default_link, categories[entr])

    def working_days(self):
        print('Horário dias úteis'.center(75, '~'))
        soup = self.soup
        table = soup.find('table')
        tds = soup.findAll('td')
        working_days = tds[2].p.text
        working_days = working_days[working_days.find(':')+1:]
        hour = working_days.split(';')
        for h in hour:
            print('{} - '.format(h), end='')
        print()
        print('Horário dias úteis'.center(75, '~'))

bus = BScheduler()
bus.working_days()