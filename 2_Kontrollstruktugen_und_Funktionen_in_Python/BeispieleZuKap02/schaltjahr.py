#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 14 09:22:56 2020

@author: wieland
"""

# schaltjahr.py

def istSchaltjahr(jahr):
    if jahr % 4 != 0:
        return False
        
    if jahr % 100 == 0:
        if jahr % 400 == 0:
            return True
        else: 
            return False

    return True

e = input("Bitte geben Sie eine Jahreszahl ein ")
j = int(e)

k = "ein" if istSchaltjahr(j) else "kein"
print(j, "ist", k, "Schaltjahr.")
