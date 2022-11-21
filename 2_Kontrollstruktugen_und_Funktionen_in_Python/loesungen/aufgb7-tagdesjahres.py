#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 15:33:34 2020

Fortgeschrittene Programmierung
HS Coburg
Woche 2, Aufgabe 7

@author: wieland
"""

monatslaenge = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

tag = int(input("Bitte Tag eingeben   "))
monat = int(input("Bitte Monat eingeben "))
jahr = int(input("Bitte Jahr eingeben  "))

if jahr < 100:
    jahr += 2000
    
if (jahr % 4 == 0) and (jahr % 100 != 0) or (jahr % 400 == 0):
    monatslaenge[1] = 29
    
tdj = tag
for i in range(monat - 1 ):
    tdj += monatslaenge[i]
    
ausgabe = "Der {0:02d}.{1:02d}.{2} ist der {3}. Tag des Jahres"
print(ausgabe.format(tag, monat, jahr, tdj))

    