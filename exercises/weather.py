#!/usr/bin/python3
# coding:utf-8
"""
    Create a program to show weather on desktop :d
"""
from tkinter import *
from datetime import datetime
import requests


class Weather(object):
    """
        Manipulate API
    """
    def __init__(self):
        self._key = "5b318944fb61cfbae7a2dc89f20b9d5d"
        self._city, self._country = self.__get_location()
        self._link = "http://api.openweathermap.org/data/2.5/weather?q={},\
{}&APPID={}&units=metric".format(self._city, self._country, self._key)

    def get(self):
        try:
            r = requests.get(self._link).json()
            return r['main']['temp'], r['main']['temp_min'], r['main']['temp_max']
        except Exception as e:
            raise e

    def __get_location(self):
        try:
            r = requests.get('https://api.ipdata.co').json()
            return r['city'].title(), r['country_code'].lower()
        except Exception as e:
            raise e


class WWindow(Tk):
    """
        Manipulate Tk to show something
    """
    def __init__(self):
        super().__init__()
        self.wm_title("Clima")
        self.geometry('200x85+0+0')
        self.attributes("-type", "splash")
        self.attributes('-topmost', 0)
        self.mn, self.crrnt, self.mx = StringVar(), StringVar(), StringVar()
        self.lh = StringVar()
        self.minT = Label(textvariable=self.mn)
        self.minT.pack()
        self.current = Label(textvariable=self.crrnt)
        self.current.pack()
        self.maxT = Label(textvariable=self.mx)
        self.maxT.pack()
        self.last_update = Label(textvariable=self.lh).pack()
        self.get_climate()

    def get_climate(self):
        mn, current, mx = Weather().get()
        self.mn.set("Temp min: {}".format(mn))
        self.crrnt.set("Temperatura atual: {}".format(current))
        self.mx.set("Temp max: {}".format(mx))
        self.lh.set("Última atualização: {}".format(datetime.now().strftime("%H:%M:%S")))
        self.after(250, self.get_climate)

main =  WWindow()
main.mainloop()
