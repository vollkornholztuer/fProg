#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 15:49:03 2021

@author: wieland
"""

li = [] #list()
for i in range(5):
    z = int(input("Bitte {}. Zahl: ".format(i+1)))
    li.append(z)
    
li.sort()

print("Median ist", li[2])
    