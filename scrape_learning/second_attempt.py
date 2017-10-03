# coding:utf-8
from urllib2 import Request, urlopen
from bs4 import BeautifulSoup
from random import randint
from sys import argv
import sqlite3


class TDataBase:
    """
        Class to manage database
    """
    def __init__(self):
        self._db_name = "tpb.db"
        self._conn = sqlite3.connect(self._db_name)
        self._cur = self._conn.cursor()
        self._cur.execute("""CREATE TABLE IF NOT EXISTS tpblinks (id INTEGER PRIMARY KEY, name TEXT, link TEXT)
                            """)

    def store_link(self, name, link):
        """
            Stores a link or many links :d
        """
        try:
            self._cur.execute("""INSERT INTO tpblinks (name, link) VALUES(?, ?)""", (name, link))
            self._conn.commit()
            print 'enviado ao db'
            return 1
        except Exception as e:
            return -1

    def retrieve_link(self, name):
        """
            This retrieve a link based on name :p
        """
        response = self._cur.execute("""SELECT * FROM tpblinks WHERE name = ?""", [name]).fetchall()
        return response if len(response) > 0 else -1


class TPirateBay:
    """ 
        Make a search on thepiratebay and return a link for something 
    """
    def __init__(self, term):
        self.term = term.replace(' ', '%20')
        self.header = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}
        self.link = "https://thepiratebay.org/search/{}/0/99" .format(self.term)

    def search(self):
        """ 
            Return a magnet link based on search term 
        """
        try:
            req = urlopen(Request(self.link, headers=self.header)).read()
            soup = BeautifulSoup(req, 'html.parser')
            results = soup.find('div', {'id': 'SearchResults'}).find('div', {'id': 'content'})
            results = results.find('div', {'id': 'main-content'}).find('table', {'id': 'searchResult'})
            links = [x['href'] for x in results.findAll('a', {'title': 'Download this torrent using magnet'})]
            return self.term.replace('%20', ' '), links[randint(0, 6)] # Return only the first
        except Exception as e:
            raise Exception(e)

def menu():
    db = TDataBase()
    choose = int(raw_input("[1] - Search link on db\n[2] - Search link on ThePirateBay\n[3] - Quit\n:"))
    if choose == 1:
        # term = ' '.join(argv[1:]) if len(argv) > 1 else exit('no term found')
        term = raw_input("Termo de pesquisa: ")
        link = db.retrieve_link(term)[0]
        print "{} = {} (already stored)".format(link[1], link[2])
    elif choose == 2:
        # term = ' '.join(argv[1:]) if len(argv) > 1 else exit('no term found')
        term = raw_input("Termo de pesquisa: ")
        (name, link) = found = TPirateBay(term).search()
        db.store_link(name, link)
        print '{} = {} (was stored)'.format(name, link)
    elif choose == 3:
        print 'Exiting...\n'
        quit(0)

if __name__ == '__main__':
    menu()