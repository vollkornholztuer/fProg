# Schreiben Sie ein Python-Skript, das den Radius einer Kugel im Dialog einliest und die Oberfläche sowie das Volumen der Kugel ausgibt.
# Die Zahl PI können Sie dem Bibliotheksmodul math entnehmen.

import math

radius = float(input('Geben Sie den Radius der Kugel ein\n'))
print('Eingegebener Radius ist:', radius)

volume = 4/3 * math.pi * math.pow(radius, 3)
print('Das Volumen der Kugel beträgt:', round(volume, 2), 'Volumenneinheiten')

surface = 4 * math.pi * math.pow(radius, 2)
print('Die Oberfläche beträgt:', round(surface, 2), 'Flächeneinheiten')
