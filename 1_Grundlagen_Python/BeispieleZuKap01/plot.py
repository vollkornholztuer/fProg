#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 10:38:12 2020

@author: wieland
"""

import sys

try:
    import matplotlib.pyplot as plt
    import numpy as np
    
except:
    print("Cannot find libraries. Exiting.", file=sys.stderr)
    sys.exit(1)
    
ofname = "plotbsp.pdf"

x = np.arange(-17, 17, 0.01)
y = np.sin(x) / x

fig, ax = plt.subplots()

ax.plot(x, y, c='r')
ax.set_xlabel(r'$x$')
ax.set_ylabel(r'$f(x) = \frac{sin(x)}{x}$')

fig.savefig(ofname)


    