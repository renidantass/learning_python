# coding:utf-8
from bs4 import BeautifulSoup
from urllib2 import Request, urlopen


class Scrapper(object):
    def __init__(self):
        self.link = 'https://www.r7.com/'
        self.headers = {'User-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:57.0) Gecko/20100101 Firefox/57.0'}
        self.response = self._get()
        self.soup = BeautifulSoup(self.response, 'lxml')

    def _get(self):
        try:
            return urlopen(Request(self.link, None, headers=self.headers)).read()
        except Exception as e:
            raise e

    def get_featured(self):
        """
            Get trends on r7
        """
        soup = self.soup
        try:
            featured = soup.find('div', {'class': 'box rw guerra'})
            link = featured.find('div', {'class': 'guerra-background'}).a['href'].strip()
            print 'Link da notícia:', link
            content = featured.find('div', {'class': 'guerra-content'})
            headline = content.find('div', {'class': 'guerra-headline'})
            label = headline.find('span', {'class': 'guerra-label'}).text.strip()
            print 'Label:', label
            title = headline.h1.text.strip()
            print 'Título:', title
            list = content.find('ul', {'class': 'guerra-list'})
            items = [li.text.strip() for li in list.findAll('li')]
            print 'Itens:'
            for item in items:
                print '\t - ' + item
        except Exception as e:
            raise e

scrap = Scrapper()
print scrap.get_featured()
