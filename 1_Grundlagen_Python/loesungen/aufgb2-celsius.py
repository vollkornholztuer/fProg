#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 15:27:24 2021

@author: wieland
"""

  
e = input ("Geben Sie eine Temperatur zwischen 0 und 100 °F ein: ")
t = int(e)

if (t < 0) or (t > 100):
    print("Falsche Eingabe")
else:
    c = (5 * (t - 32) / 9)
    print("Das sind %.1f°C." % c)
    
e = input ("Geben Sie eine Temperatur zwischen 0 und 100 °C ein: ")
t = int(e)

if (t < 0) or (t > 100):
    print("Falsche Eingabe")
else:
    f = (9 * t / 5 + 32)
    print("Das sind {:.1f}°F.".format(f))
    
