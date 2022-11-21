#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 13:52:12 2020

@author: wieland
"""

from datetime import date

class Datum:
    def __init__(self, tag = 1, monat = 1, jahr = 2020):
        self.__tag = tag
        self._monat = monat
        self.jahr = jahr

    @property
    def tag(self) :
        return self.__tag
   
    @tag.setter
    def tag(self, einTag):
        print("Hier setter-Methode für tag")
        self.__tag = einTag
        
    def setzeAufHeute(self):
        self.__tag = date.today().day
        self._monat = date.today().month
        self.jahr = date.today().year
        
    def ausgeben(self):
        print("Heute ist der {0:02}.{1:02}.{2}".format(self.__tag, self._monat, self.jahr))
        
    Nikolaus = (6, 12, 2020)

d = Datum (8,11)
d.ausgeben()

d.setzeAufHeute()
d.ausgeben()        
        
d._monat = 5
d.ausgeben()

d.__tag = 1
d.ausgeben()

d.tag = 1
d.ausgeben()


print(d.Nikolaus)

