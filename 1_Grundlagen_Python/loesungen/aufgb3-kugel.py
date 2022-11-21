#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 15:05:03 2021

@author: wieland
"""

import math

e = input("Bitte geben Sie einen Radius ein: ")
r = float(e)

o = 4.0 * math.pi * r**2
v = 4.0/3 * math.pi * r**3

print("Radius:", r, "Oberfläche:", round(o, 2), "Volumen: %.2f" % v)