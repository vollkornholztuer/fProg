#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 11:41:38 2020

@author: eed
"""

class ListTransaction() :
    def __init__(self, theList):
        self.theList  = theList
        
    def __enter__(self):
        self.workingcopy = list(self.theList)
        return self.workingcopy
    
    def __exit__(self, exctype, value, tb) :
        if exctype == None:
            self.theList[:] = self.workingcopy
        return False
    
items = [1, 2 ,3]
with ListTransaction(items) as working :
    working.append(4)
    working.append(5)

print(items)

try:
    with ListTransaction(items) as working :
        working.append(6)
        working.append(7)
        raise RuntimeError("Unser Fehler")
        
except RuntimeError as e:
    print(e)
    
print(items)

    