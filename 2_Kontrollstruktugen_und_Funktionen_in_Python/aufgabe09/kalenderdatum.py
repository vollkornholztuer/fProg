print('Dieses Programm berechnet den Wochentag vom eingegebenen Kalenderdatum')
t = int(input('Geben Sie den Tag ein (1-31)'))
m = int(input('Geben Sie den Monat ein (1-12)'))
h = int(input('geben sie den Jahrhundert ein (0-99)'))
j = int(input('Geben Sie das Jahr im Jahrhundert ein (0-99)'))

if m == 1:
    m = 13
elif m == 2:
    m = 14
else:
    m = m


w = int((t + ((m + 1) * 26)/10 + (5*j)/4 + h/4 - 2*h - 1) % 7)
print(w)

wochentag = ['Sonntag', 'Montag', 'Dienstag',
             'Mittwoch', 'Donnerstag', 'Freitag', 'Samstag']

print('Der Wochentag am angegebenen Datum war ein', wochentag[w])
