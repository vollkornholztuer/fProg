#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 12:45:56 2020

@author: wieland
"""

def countdown(n):
    """
    Beispiel für statische Variablen
    """
    r = n
    def next():
        nonlocal r
        r -= 1
        return r
    return next

y = countdown(10)
z, li = y(), []
while z != 0:
    li.append(z)
    z = y()
print(li)
