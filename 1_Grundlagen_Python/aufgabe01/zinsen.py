# Schreiben Sie ein Programm Zinsen, das einen aktuellen Anfangskapitalwert K0 [Euro] mit einem Zinssatz p [%] nach n Jahren verzinst:
# Kn = K0 · (1 + p/100)^n

# Hinweis: Verwenden Sie die Methode Math.pow(a,b) aus der Klasse Math zum Berechnen von a hoch b.
# Testbeispiele:
# K0 = 1000.00, n = 5, p = 2.0 folgt K5 = 1104.08
# K0 = 1000.00, n = 5, p = −2.0 folgt K5 = 903.92


import math

print("hello world")

k0 = float(input('Was für ein Kapital hast du?\n'))
print(k0)
n = int(input('Für wie viele Jahre legst du dein Kapital an?\n'))
print(n)
p = float(input('Was hast du für einen Zinssatz?\n'))
print(p)

kn = k0 * math.pow(1 + p/100, n)
print(kn)
