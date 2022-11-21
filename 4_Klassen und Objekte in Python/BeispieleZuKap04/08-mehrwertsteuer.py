#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 15 15:11:31 2020

@author: wieland
"""

class Steuer:
    def __init__(self, anteil):
        self.anteil = anteil

# Überladen des ()-Operators als Funktor
    def __call__(self, betrag):
        return self.anteil * betrag


mehrwertsteuer = Steuer(0.16)
print(mehrwertsteuer(1000))  # Aufruf der Methode über Objektname
        
