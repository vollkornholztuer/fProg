#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 15:11:31 2020

@author: wieland
"""

def gen(n):
    z = n
    while True:
        yield z
        z -= 1  

a = gen(5)
j = a.__next__()

while j:
    print(j)
    j = a.__next__()
    
a.close()
j = a.__next__()
