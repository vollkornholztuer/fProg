#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 11:21:48 2020

@author: wieland
"""

class StackError(Exception) :
    @property
    def message(self):
        return "Einfacher Stackfehler"
    
class StackEmpty(StackError) :
    @property    
    def message(self):
        return "Stack leer"

class StackFull(StackError) :
    def __init__(self, x):
        self.__f = x
        
    @property    
    def message(self):
        return "Stack voll ({0} kann nicht hinzugefügt werden)".format(self.__f)

class SimpleStack :
    def __init__(self, maxEntries) :
        self.__stack = [0 for i in range(maxEntries)]
        self.__top = 0
        self.__max = maxEntries
        
    def isFull(self) : 
        return self.__top == self.__max  
    
    def isEmpty(self) :
        return self.__top == 0
    
    def push(self, x) :
        if (self.isFull()):
            raise StackFull(x)
            
        self.__stack[self.__top] = x
        self.__top += 1
        
    def pop(self) :
        if (self.isEmpty()):
            raise StackEmpty
        self.__top -= 1
        return self.__stack[self.__top]
    

stack = SimpleStack(30)
i = 0
try:
    for i in range(35) :
        stack.push(i)

    for i in range(5) :
        print(stack.pop())
        
except StackError as se:
    print(se.message)
    

    
    
    
        
    

