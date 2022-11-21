#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 13:18:32 2020

@author: wieland
"""

import pygal

def eineZeile(s):
    tab, nl, komma = '\t', '\n', ','
    zeitraum = s[:s.index(tab)]
    if komma in s:
        zahl = int(s[s.index(tab)+1: s.index(komma)])
        nachkomma = int(s[s.index(komma)+1: s.index(nl)])
    else:
        zahl, nachkomma = int(s[s.index(tab)+1: s.index(nl)]), 0
    return (zeitraum, zahl+nachkomma/100)

f = open("infl.txt")
ds = f.readlines()
werte = [eineZeile(j) for j in ds]
xVal = [j[0] for j in werte]
yVal = [j[1] for j in werte]
print("Werte:", werte)
print('\n')

# Erzeuge Liniendiagramm
linie = pygal.Line()
linie.title = "Inflation 2010 - 2019"
linie.x_labels = xVal
linie.add('2010-2019', yVal)
linie.render_to_file('infl_linie.svg')

# Erzeuge Balkendiagramm
chart = pygal.Bar()
chart.title = "Inflation 2010 - 2019"
chart.x_labels = xVal
chart.add('2010-2019', [j for j in yVal])
chart.render_to_file("infl_balken.svg")

# Erzeuge gestaffelte Diagramme
bb = pygal.Bar(x_label_rotation = 60)
bb.title = "Inflation 2010 - 2019"
bb.add('2010-2012', [j for j in yVal[0:3]])
bb.add('2013-2015', [j for j in yVal[3:6]])
bb.add('2016-2018', [j for j in yVal[6:9]])
bb.render_to_file("infl_gest.svg")
