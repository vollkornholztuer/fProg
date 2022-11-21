#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 20 09:54:56 2020

Fortgeschrittene Programmierung
HS Coburg
Woche 2, Aufgabe 12

@author: wieland
"""

from math import pi

def umfangKreis(radius):
    return 2.0 * pi * radius

def flaecheKreis(radius):
    return pi * radius**2

def summeUmfangKreis(radiusliste):
    sum = 0.0
    for r in radiusliste:
        sum += umfangKreis(r)
        
    return sum

def summeFlaecheKreis(radiusliste):
    sum = 0.0
    for r in radiusliste:
        sum += flaecheKreis(r)
        
    return sum

def umfangLambda(radius):
    return sum(map(umfangKreis, radius))

# Test
print("Umfang r=1:", umfangKreis(1))
print("Umfang r=3:", umfangKreis(3))
print("Fläche r=1:", flaecheKreis(1))
print("Fläche r=3:", flaecheKreis(3))

print("Summe Umfang bei r = 1,2,3: ", summeUmfangKreis([1, 2, 3]))
print("Summe Fläche bei r = 1,2,3: ", summeFlaecheKreis([1, 2, 3]))
print("Summe Fläche bei r = 1,2,3: ", umfangLambda([1, 2, 3]))
