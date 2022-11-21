#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 13:52:12 2020

@author: wieland
"""

from datetime import date

class Datum:
    def __init__(self, tag = 1, monat = 1, jahr = 2021):
        self.__tag = tag
        self._monat = monat
        self.jahr = jahr

    def ausgeben(self):
        print("Heute ist der {0:02}.{1:02}.{2}".format(self.__tag, self._monat, self.jahr))
        
    def setze(self, t, m, j) :
        altesJahr = self.jahr
        self.jahr = j
        
        monate = [31,28,31,30,31,30,31,31,30,31,30,31]
        
        if (m < 1) or (m>12) or (j < 1900) or (j>2299) or (t<1) or (t>monate[m-1]) :
            print("Datum ungültig!")
            self.jahr = altesJahr
            return
        
        self._monat = m
        self.__tag = t
     
    def __del__(self):
        print("Hier Destruktor")
        
    Nikolaus = (6, 12, 2021)

d = Datum (8,11)
d.ausgeben()

d._monat = 5
d.ausgeben()

d.__tag = 1
d.ausgeben()

d = Datum(1, 11, 2020)
d.ausgeben()

print(d.Nikolaus)

