#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 15:27:24 2020

@author: wieland
"""

celsius = list()
for j in range(101):
    celsius.append(5 * (j - 32) / 9.0)
    
e = input ("Geben Sie eine Temperatur zwischen 0 und 100 °F ein: ")
t = int(e)

if (t < 0) or (t > 100):
    print("Falsche Eingabe")
else:
    print("Das sind %.1f°C." % celsius[t])