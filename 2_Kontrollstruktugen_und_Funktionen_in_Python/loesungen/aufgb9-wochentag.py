#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 16:09:41 2020

Fortgeschrittene Programmierung
HS Coburg
Woche 2, Aufgabe 9

@author: wieland
"""

def istSchaltjahr(jahr) :
    if jahr % 4 != 0:
        return False
    
    if jahr % 100 == 0:
        if jahr % 400 == 0:
            return True
        else:
            return False
        
    return True

def wochentag(tag, monat, jahr):
    w = 0
    if monat <= 2:
        monat += 12
        jahr -= 1
    
    h = jahr // 100
    j = jahr % 100
    
    w = tag + (monat + 1) * 13 // 5 + 5 * j // 4 + h // 4 - 2 * h - 1;
    
    #print("w:", w, " (w%7 =", w%7, ")")
        
    return w % 7

monatslaenge = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
wochentage = ("Sonntag", "Montag", "Dienstag", "Mittwoch",\
                        "Donnerstag", "Freitag", "Samstag")

tag = int(input("Bitte geben Sie den Tag ein:"))
monat = int(input("Bitte geben Sie den Monat ein:"))
jahr = int(input("Bitte geben Sie das Jahr ein:"))

if jahr < 100:
    jahr += 2000
    
isj = istSchaltjahr(jahr)

if monat <= 0 or monat > 12 or tag <= 0 or \
    (monat != 2 and tag > monatslaenge[monat-1]) or\
    (monat == 2 and tag > monatslaenge[monat-1] + isj):
        print("{:02}.{:02}.{:} ist ein ungültiges Datum".format(tag,\
            monat, jahr))
else:
    wt = wochentag(tag, monat, jahr)
    print("Der {:02}.{:02}.{:} ist ein {:}".format(tag,\
            monat, jahr, wochentage[wt]))
        

        