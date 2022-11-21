#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 17 15:55:21 2020

@author: wieland
"""

import csv
reader = csv.reader((open("browser-data.csv","r")))
#for row in reader:
#    print(row)
    
#reader = csv.DictReader((open("browser-data.csv","r")))
for row in reader:
    print(row)
