#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 09:45:21 2020

@author: wieland
"""
import random
           
anzahl = 6
m = set()
for i in range(6):
    while True:
        z = random.randint(1,49)
        if not z in m:
            m.add(z)
            break
    
while True:
    zusatz = random.randint(1,49)
    if not zusatz in m:
        break

l = list(m)
l.sort()

print("Die Lottozahlen: ", l, "(", zusatz, ")")

