import sqlite3
import time
import os


class SaveBills:
    def __init__(self):
        self.check()
        self.conn = sqlite3.connect('teste.db')
        self.cur = self.conn.cursor()

    def check(self):
        if not os.path.exists('teste.db'):
            conn = sqlite3.connect('teste.db')
            cur = conn.cursor()
            cur.execute('''CREATE TABLE market (pessoa text, price real, items int, data date, hora text);''')
            conn.commit()

    def save(self, name, price, items):
        date, hour = time.strftime('%d-%m-%Y', time.gmtime()), time.strftime('%H:%M:%S', time.gmtime())
        self.cur.execute('''INSERT INTO market (pessoa, price, items, data, hora)
                            VALUES (?, ?, ?, ?, ?)''', (name, price, items, date, hour))
        self.conn.commit()

    def view(self, specific_name=''):
        specific_name = 'WHERE pessoa LIKE %s' % specific_name if len(specific_name) > 1 else specific_name
        r = self.cur.execute('''SELECT * FROM market ORDER BY hora %s''' % specific_name)
        for acc in r.fetchall():
            print acc

s = SaveBills()
print s.view()
