#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 15:31:24 2021

@author: wieland
"""

y = 0
ref = 0

inseln = ["Bermudas", "Fidschi", "Komoren", "Kuba"]
index = [1, 3, 0, 2]

while y < 4 :
    ref = index[y]
    print("Insel:", inseln[ref])
    y += 1
    

    