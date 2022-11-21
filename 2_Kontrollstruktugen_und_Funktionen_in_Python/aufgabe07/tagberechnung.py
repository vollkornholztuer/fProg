print('Dieses Programm berechnet ihnen den Aktuellen Tag im Jahr')

day = int(input('Geben Sie den Tag in Ganzzahlen ein\n'))
month = int(input('Geben Sie den Monat in Ganzzahlen ein\n'))
year = int(input('Geben Sie das Jahr in Ganzzahlen ein\n'))

normalYear = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leapYear = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


monthDays = 0
if year % 4 == 0:
    for i in range(month-1):
        monthDays = monthDays + leapYear[i]
else:
    for i in range(month-1):
        monthDays = monthDays + normalYear[i]


calculatedDay = day + monthDays

print('Der heutige tag ist der', calculatedDay, 'Tag im Jahr')
