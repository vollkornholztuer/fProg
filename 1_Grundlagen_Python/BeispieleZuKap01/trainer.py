#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 11:07:54 2020

@author: wieland
"""

# trainer.py
import random 
import time

print("Multiplikationstrainer")
print("----------------------")
startzeit = time.time()
for i in range(5):
    a = random.randint(1,20) 
    b = random.randint(1,10)
    ergebnis =- 1

    while ergebnis != a * b:
        ergebnis = int(input(str(a) + "*" + str(b) + "=")) #4
        if ergebnis == a * b:   
            print("Richtig!")
        else:
            print("Falsch! Versuchen Sie es noch einmal!")
            
zeit = int(time.time() - startzeit)
print("Für die Aufgaben haben Sie", zeit, "Sekunden benötigt.")