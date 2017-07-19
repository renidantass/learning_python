# coding:utf-8
from urllib.request import urlopen
from urllib.parse import quote
from json import loads


class Genderize(object):
    def __init__(self, name):
        self.name = quote(name)
        self.link = "https://api.genderize.io/?name={}" .format(self.name)

    def get_info(self):
        try:
            return loads(urlopen(self.link).read())['gender'], loads(urlopen(self.link).read())['probability']
        except Exception as e:
            raise Exception(e)

if __name__ == '__main__':
    name = input("Type your name: ")
    gender, percentage = Genderize(name).get_info()
    print("Your gender are probability [{:.2f}%%||{:.2f}%%]: {}" .format(percentage, percentage * 100, gender))
