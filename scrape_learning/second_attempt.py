# coding:utf-8
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from random import randint

class TPirateBay:
    """ Make a search on thepiratebay and return a link for something """
    def __init__(self, term):
        self.term = term.replace(' ', '%20')
        self.header = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
        self.link = "https://thepiratebay.org/search/{}/0/99" .format(self.term)

    def search(self):
        """ Return a magnet link based on search term """
        try:
            req = urlopen(Request(self.link, headers=self.header)).read()
            soup = BeautifulSoup(req, 'html.parser')
            results = soup.find('div', {'id': 'SearchResults'}).find('div', {'id': 'content'})
            results = results.find('div', {'id': 'main-content'}).find('table', {'id': 'searchResult'})
            links = [x for x in results.findAll('a', {'title': 'Download this torrent using magnet'})]
            return links[randint(0, 6)]['href'] # Return a random link
        except Exception as e:
            raise Exception(e)

if __name__ == '__main__':
    term = input("Term: ")
    print(TPirateBay(term).search()) # Just a little example