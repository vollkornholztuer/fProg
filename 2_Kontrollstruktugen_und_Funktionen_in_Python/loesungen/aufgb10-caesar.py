#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 16:31:34 2020

Fortgeschrittene Programmierung
HS Coburg
Woche 2, Aufgabe 10

@author: wieland
"""

def shiftchar(inp, shift):
    code = ord(inp)
    oa = ord('A')
    oz = ord('Z')
        
    if code >= oa and code <= oz:
        c = (code - oa + shift) % 26
        return (chr(c + oa))
# =============================================================================
#         if code + shift >= oa:
#             if code + shift <= oz:
#                 return chr(code + shift)
#             else:
#                 return chr(oa - 1 + shift - oz + code)
#         else:
#             return chr(oz + 1 + shift - oa + code)
# =============================================================================
    oa = ord('a')
    oz = ord('z')
    if code >= oa and code <= oz:
        c = (code - oa + shift) % 26
        return (chr(c + oa))
    
    return inp

def caesar_encode(src, dist):
    o = ""
    
    for i in src:
        o += shiftchar(i, dist)
        
    return o

def caesar_decode(src, dist):
    return caesar_encode(src, -dist)

### Hauptteil
text = "Franz jagt im komplett verwahrlosten Taxi quer durch Bayern."

print("Nachricht: ", text, "\n")
verschl = caesar_encode(text, 15)

print("Verschlüsselte Nachricht: ", verschl)
entschl = caesar_decode(verschl, 15)

print("Entschlüsselte Nachricht: ", entschl)


# text2 = input("Ihre Nachricht: ")
text2 = "Gallia est omnis divisa in partes tres, quarum unam incolunt belgae, aliam aquitani, tertiam qui ipsorum lingua celtae, nostra galli appellantur."
verschl = caesar_encode(text2, 4)

print("\nNachricht: ", text2, "\n")
print("Verschlüsselte Nachricht: ", verschl)

