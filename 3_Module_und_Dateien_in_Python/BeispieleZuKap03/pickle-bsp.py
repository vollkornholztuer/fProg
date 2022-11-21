#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 16 15:16:46 2020

@author: wieland
"""

import pickle

dd = {1: 'q', 2: [1, 2, 3], 'ww': 'Eine Zeichenkette'}
datei = open('meinedatei.bin', 'wb')
pickle.dump(dd, datei)
datei.close()

dat = open('meinedatei.bin', 'rb')
lex = pickle.load(dat)
print(lex)
dat.close()

