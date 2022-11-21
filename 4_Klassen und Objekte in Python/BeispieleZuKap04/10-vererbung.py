#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 16:09:19 2020

@author: wieland
"""

class CPerson :
    def __init__(self, name) :
        self.__name = name;
        self._konto = 1000.0
        
    def abheben(self, betrag):
        self._konto -= betrag
        
    def getKontostand(self) : 
        return self._konto
    
class CSparer(CPerson) :
    def __init__(self, name) :
        super().__init__(name)
        self.__kredit = 0.0
        
    def abheben(self, betrag) :
        super().abheben(betrag)
        print("Verfügbarer Betrag: ", self.getKontostand())
        
    def setKredit(self, hoehe) :
        self.__kredit = hoehe
        self._konto += hoehe
        
    @property
    def kredit(self):
        return self.__kredit
    
    
misterz = CSparer("Wuchtig")
print("Kredithöhe: ", misterz.kredit)
misterz.setKredit(4000)
misterz.abheben(500)
print("Kredithöhe: ", misterz.kredit)

misterx = CPerson("Knut")
print(misterx.getKontostand())
misterx.kredit


        