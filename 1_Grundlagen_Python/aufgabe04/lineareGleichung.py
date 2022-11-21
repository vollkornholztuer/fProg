# Zur Darstellung eines Punktes im zweidimensionalen kartesischen Koordinatensystem verwenden Sie ein Python-Tupel mit zwei Datenelementen vom Typ float .
#
# Schreiben Sie ein Skript, das zwei Variablen von diesem Tupel definiert, mit unterschiedlichen Werten initialisiert und die Gerade durch die beiden Punkte ermittelt.
# Falls die x-Koordinaten der Punkte verschieden sind, sollen die Parameter m und c der Geradengleichung
#
# y = m · x + c
#
# berechnet und auf dem Bildschirm ausgegeben werden.
#
#
# Beispielausgabe:
#
# Erster Punkt: P1 = (-1.1, 3.5)
# Zweiter Punkt: P2 = (2.4, -0.7)
# Für die Gerade y = mx + c durch P1 und P2 gilt:
# m= -1.200 und c = 2.180


p1x = float(input('Geben sie die x-Koordinate des ersten Punktes ein:'))
p1y = float(input('Geben sie die y-Koordinate des ersten Punktes ein:'))
p2x = float(input('Geben sie die x-Koordinate des zweiten Punktes ein:'))
p2y = float(input('Geben sie die y-Koordinate des zweiten Punktes ein:'))

punkt1 = (p1x, p1y)
punkt2 = (p2x, p2y)

# p1 = (-1.1, 3.5)
# p2 = (2.4, -0.7)

m = (punkt1[1] - punkt2[1]) / (punkt1[0] - punkt2[0])

c = m * punkt1[0]-punkt1[1]

print('für die Gerade y = mx + c durch P1 und P2 gilt:')
print('m =', m, 'und c =', c)
