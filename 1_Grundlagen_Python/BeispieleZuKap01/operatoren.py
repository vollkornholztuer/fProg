#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 15:08:53 2020

@author: wieland
"""

a = 10 * 5 + 10
print(a)

a = 10
a *= 5 + 10      
print(a)

b = 0
c = 0
b = b == c
print(b)
a >>= b + 2
print(a)

a = 3; b = 2

a = a << (a + b)
b += a
a *= b
print("a =", a, " b =", b)

