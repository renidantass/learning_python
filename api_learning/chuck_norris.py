# coding:utf-8
""" Interact with ICNDb.com API / Chuck Norris DB """
import requests
import json


class Norris(object):
    def __init__(self, name_char='Chuck', tags2add='', tags2exclude=''):
        self.response, self.tags = None, ''
        self.name_char = name_char
        self.tags2add = tags2add
        self.tags2exclude = tags2exclude
        self.spelling_name()
        self.spelling_aargs()
        self.link = "https://api.icndb.com/jokes/random?{}{}" .format(self.name_char, self.tags)
        self.__get()

    def spelling_name(self):
        self.name_char = self.name_char.split()
        if len(self.name_char) > 0:
            if len(self.name_char) < 3:
                self.name_char[0] = 'firstName=' + self.name_char[0]
                self.name_char[1] = 'lastName=' + self.name_char[1]
                self.name_char = "".join("%s&%s" % (self.name_char[0], self.name_char[1]))
                return self.name_char
        return None

    def spelling_aargs(self):
        if len(self.tags2add) > 1:
            self.tags = '&' + self.tags2add
            if len(self.tags2exclude) > 1:
                self.tags = '&' + self.tags2exclude
        return None

    def __get(self):
        try:
            req = json.loads(requests.get(self.link).text)
            self.response = req['value']['joke']
        except Exception as e:
            print "Raised a exception %s" % e

if __name__ == '__main__':
    n = Norris('Chuck Norris', 'Nerdy', 'Explicit')
    print n.response
