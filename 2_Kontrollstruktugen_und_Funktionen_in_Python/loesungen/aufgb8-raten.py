#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 15:59:24 2020

Fortgeschrittene Programmierung
HS Coburg
Woche 2, Aufgabe 8

@author: wieland
"""

import random
import sys

random.seed()
gesucht = random.randint(0,9)

for versuche in range(3):
    tipp = int(input("Bitte eine Zahl eingeben: "))
    
    if tipp == gesucht:
        print("RICHTIG! Du hast es geschafft!\n")
        sys.exit(0)
        
    if tipp < gesucht:
        print("Falsch, die gesuchte Zahl ist groesser.\n")
    else:
        print("Falsch, die gesuchte Zahl ist kleiner.\n")

print("Leider verloren. Die richtige Zahl war", gesucht,".")
