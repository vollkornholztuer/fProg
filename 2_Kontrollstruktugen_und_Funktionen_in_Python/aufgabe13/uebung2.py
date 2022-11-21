from cmath import pi


def check2pi(list):
    for i in range(len(list)):
        if list[i] > 0 and list[i] < 2*pi:
            filteredList.append(list[i])


def convertGradmass(b):
    g = float(b * 360 / 2*pi)
    return round(g, 2)


floatList = [-1.9, -0.69, 0, 0.23, 0.6, 1.1, 1.337, 1.9, 2.1, 3.45, 4.20, 6.9]
filteredList = []
convertedList = []

check2pi(floatList)
print('Gefilterte Liste:', filteredList)

convertedList = list(map(convertGradmass, filteredList))
print('Konvertierte Liste:', convertedList)
