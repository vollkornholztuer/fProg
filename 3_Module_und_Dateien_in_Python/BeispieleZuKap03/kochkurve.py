#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 11:35:23 2020

@author: wieland
"""

import turtle

def kochkurve (laenge , ebene ):
    if(ebene >0):
            kochkurve ( laenge /3.0 , ebene -1)
            turtle.left (60)
            kochkurve ( laenge /3.0 , ebene -1)
            turtle.right (120)
            kochkurve ( laenge /3.0 , ebene -1)
            turtle.left (60)
            kochkurve ( laenge /3.0 , ebene -1)
    else :
        turtle.forward ( laenge )
        
def init ():
    turtle.reset ()
    turtle.setworldcoordinates ( -0.1 , -0.9 , 1.1 , 0.3)
    turtle.speed (0)
    turtle.hideturtle ()
    
if __name__ == '__main__':
    n=int( input (" Anzahl   Rekursionen :"))
    init ()
    kochkurve (1.0 , n)
    turtle.right (120)
    kochkurve (1.0 , n)
    turtle.right (120)
    kochkurve (1.0 , n)
    turtle.exitonclick ()