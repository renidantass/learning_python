# coding:utf-8
import requests


class Genderize(object):
	""" This API don't need specificy API KEY """
	def __init__(self, name):
		self.response = None
		self.name = name
		self.link = "https://api.genderize.io/?name={}" .format(self.name)
		self.__get()

	def __get(self):
		try:
			self.response = requests.get(self.link).json()['gender']
		except Exception as e:
			print "Raised a exception as %s" % e

if __name__ == '__main__':
	print Genderize('Reni').response
