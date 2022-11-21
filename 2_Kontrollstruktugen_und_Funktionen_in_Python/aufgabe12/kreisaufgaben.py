from cmath import pi
import math

# global umfangGesamt
# global flaecheGesamt

global umfangGesamt
global flaecheGesamt


r = int(0)


def umfangKreis(radius):
    u = 2 * radius * pi
    print("Umfang:", u, "Längeneinheiten")


def flaecheKreis(radius):
    a = pi * math.pow(radius, 2)
    print("Flächeninhalt:", a, "Flächeneinheiten")


def summeUmfangKreis(radiusliste):
    print(radiusliste)
    umfangGesamt = float(0)

    for r in range(len(radiusliste)):
        u = 2 * radiusliste[r] * pi
        umfangGesamt += u

    print("Gesamtumfänge d. Kreise:", umfangGesamt, "Längeneinheiten")


def summeFlaecheKreis(radiusliste):
    print(radiusliste)
    flaecheGesamt = float(0)

    for r in range(len(radiusliste)):
        a = pi * math.pow(radiusliste[r], 2)
        flaecheGesamt += a

    print("Gesamtflächen d. Kreise:", flaecheGesamt, "Flächeneinheiten")
