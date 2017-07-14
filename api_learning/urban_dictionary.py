# coding:utf-8

import requests
import json


class UrbanD(object):
    def __init__(self, term):
        self.response = None
        self.api_key = "####################################" # Your api key here
        self.link = "https://mashape-community-urban-dictionary.p.mashape.com/define?term={}" . format(term)
        self.headers = {'X-Mashape-Key': self.api_key, 'Accept': 'text/plain'}
        self.__get()

    def __get(self):
        try:
            self.response = json.loads(requests.get(self.link, headers=self.headers).text)['list']
        except Exception as e:
            print "Raised a exception as %s" % e

if __name__ == '__main__':
    print UrbanD('wat').response
