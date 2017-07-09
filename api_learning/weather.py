# coding:utf-8
""" Construct a module that interact with a API """
import requests
import json

class Weather(object):
    def __init__(self, city_name='Osasco', country_code=''):
        self.api_key = "################" # Your api key of OpenWeather here
        self.city_name = city_name
        self.ccode = country_code
        self.link = "http://api.openweathermap.org/data/2.5/weather?q={}&APPID={}" .format(self.city_name, self.api_key)

    def __enter__(self):
        try:
            req = requests.get(self.link).text
            response = json.dumps(json.loads(req))
            self.f  = open('resp.txt', 'w')
            json.dump(response, self.f)
        except Exception as e:
            print e

    def __exit__(self, exec_type, exec_value, exec_traceback):
        if not self.f.closed:
            self.f.close()

if __name__ == '__main__':
    with Weather('Osasco') as w:
        pass
