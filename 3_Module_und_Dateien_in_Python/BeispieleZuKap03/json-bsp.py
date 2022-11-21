#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 16:00:28 2020

@author: wieland
"""

import json

demo = ({1: 'a', 2: 3},
        "eine Zeichenkette",
        16,
        [1, 2, "simsalabim"],
        ('j', 'a', ' ', 'm', 'e', 'i'),
        None,
        True)
g = open("bsp.json", 'w')
json.dump(demo, g)
g.close()

g = open("bsp.json", 'r')
o = json.load(g)
g.close()
print(o)
