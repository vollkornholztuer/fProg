#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 09:38:45 2020

Fortgeschrittene Programmierung
HS Coburg
Woche 2, Aufgabe 11

@author: wieland
"""

damen = set(["Anna", "Bine", "Carla", "Doris"])
herren = set(["Arne", "Ben", "Charly", "Dirk"])
tanzlehrer = set(["Lehrer"])
tanzpaare = set(tuple((d, h))
                for d in damen|tanzlehrer
                for h in herren|tanzlehrer
                if d != h)

#i = 1
for p in tanzpaare:
    print(p, end=" ")
    # print(i, ":", p)
#    i += 1
