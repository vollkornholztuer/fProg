# Schreiben Sie ein Python-Skript, das:
# a. eine Fahrenheit-Temperatur im Dialog einliest und in Celsius umrechnet sowie
# b. eine Celsius-Temperatur einliest und in Fahrenheit umrechnet.
# Verwenden Sie für die Temperaturen float -Variablen und geben Sie die Ergebnisse mit einer Stelle nach dem Dezimalpunkt aus. Die Umrechnungsformel lautet:
# 5 * (Fahrenheit - 32) = 9 * Celsius


tempChoice = int(input(
    'Wähle 0 um von Celsius nach Fahrenheit zu konvertieren,\n wähle 1 um von Fahrenheit nach Celsius zu konvertieren\n'))
print(tempChoice)

temp = float(input('gebe die zu konvertierende Temperatur ein:'))
print(temp)

if tempChoice == 0:
    convertedTemp = temp * 1.8 + 32
    print('Fahrenheit: ', convertedTemp)
else:
    convertedTemp = (temp - 32) * 5/9
    print('Celsius: ', convertedTemp)
