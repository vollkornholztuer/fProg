#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 09:14:17 2020

@author: wieland
"""

class CPerson:
    __anzahl = 0       # statisches Element
    
    def __init__(self, vorn, nm) :
        self.__vorname = vorn
        self.__name = nm
        #self.__anzahl = 17
        CPerson.__anzahl += 1
        print(CPerson.__anzahl)
        
    def __del__(self) :
        CPerson.__anzahl -= 1
        print("Hier Destruktor", CPerson.__anzahl)
        
    @staticmethod
    def gibAnzahl() :    # statische Methoden ohne self!
        return CPerson.__anzahl
    
    @staticmethod
    def setAnzahl(anz) :
        CPerson.__anzahl = anz
        
print(CPerson.gibAnzahl())

misterx = CPerson("Knut","Wuchtig")
print(misterx.gibAnzahl())

if True:
    mistery = CPerson("Hasso","Zorn")
    print(misterx.gibAnzahl())
    print(mistery.gibAnzahl())  

print("Nach IF:") 
#CPerson.setAnzahl(7)  
print(CPerson.gibAnzahl())
    

    
