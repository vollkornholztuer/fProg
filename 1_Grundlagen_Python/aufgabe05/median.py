# Schreiben Sie ein Python-Skript, das fünf Ganzzahlen im Dialog einliest, in einer Liste speichert, ihren Median berechnet und ausgibt.
# Der Median von fünf Ganzzahlen ist der mittlere Wert dieser Zahlen, z.B. bei 7, 3, 2, 5, 9 ist es die 5.
# Sie müssen die eingegeben Zahlen also zunächst sortieren.

print('Dieses Skript berechnet den median aus beliebig eingegebenen Ganzzahlen')

# Teilt Eingaben nach Leerzeichen
inputList = input('Enter space-seperated integers:').split()
# konvertiert Eingaben nach int, packt sie in die Liste
integerList = [int(item) for item in inputList]

integerList.sort()      # Sortiert Liste nach Wert (klein zuerst)
print(integerList)

if len(integerList) % 2 == 0:   # Berechnung Median bei gerader Anzahl an Werten
    medianLeft = integerList[int(len(integerList)/2)]
    medianRight = integerList[int(len(integerList)/2) - 1]
    median = (medianLeft + medianRight) / 2
else:      # Berechnung Median bei ungerader Anzahl an Werten
    median = integerList[int(len(integerList)/2)]

print('Der Median dieser Zahlen ist:', median)
