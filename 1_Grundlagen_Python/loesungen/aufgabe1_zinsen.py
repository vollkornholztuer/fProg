#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 15:18:38 2021

@author: wieland
"""
import math

k = input("Bitte geben Sie das Kapital ein: ")
p = input("Bitte geben Sie den Zinssatz ein: ")
n = int(input("Bitte geben Sie die Laufzeit (in Jahren) ein: "))

k = float(k)
p = float(p)
# n = int(n)

# r = math.pow((1+p/100.), n) * k
r = k * (1+p/100.)**n 

print("Nach", n, "Jahren wurden aus", k, "EUR mit", p,\
      "%% Zinsen %.2f EUR." % r)
 