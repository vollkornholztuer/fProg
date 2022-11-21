#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 09:44:41 2020

@author: wieland
"""
import sys

def DictFib(n):
    fib = {0:0, 1:1}
    for j in range(2, n+1):
        fib[j] = fib[j-1] + fib[j-2]
    return fib[n]

def FibStat(k):
    dicStat = {}.fromkeys(range(k+1), 0)
    
    def Fib(n): 
        dicStat[n] = dicStat[n] + 1
        if n <= 0 : return 0
        elif n == 1 : return 1
        else: return Fib(n-1) + Fib(n-2)
        
    l = Fib(k)
    return dicStat

DictFib(15)

ww = FibStat(33)
for j in range(0, 33, 4) :
    print([(i, ww[i]) for i in range(j, j+4) if i in ww.keys()])
    
if x < y :
    print ("x ist kleiner")
    x = y
    