#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 12:53:31 2020

@author: wieland
"""

def Umschlag(fn):
    def MachMal(*args, **kwargs) :
        print('args:', [j for j in args])
        print('kwargs:', [kwargs[j] for j in kwargs])
        return fn(*args, **kwargs)
    return MachMal

print('\nErster Umschlag')
print(Umschlag(lambda x, y: x+y)(3, 4))

def entpacken(a, b, c, d, e, f) :
    return a+b+c+d+e+f

print('\nZweiter Umschlag')
dd = {'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5, 'f' : 6}
print(entpacken(*dd))
Umschlag(entpacken)(**dd)

# geht als als Dekorator
@Umschlag
def malDrei(x):
    return 3 * x

print('\nUmschlag als Dekorator')
print(malDrei(5))
print(malDrei('Foo'))
 