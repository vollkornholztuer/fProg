from Ding import Ding


class Quader(Ding):
    def __init__(self, symbol, laenge, breite, hoehe):
        Ding.__init__(self, laenge*breite*hoehe, symbol)
        self.__laenge = float(laenge)
        self.__breite = float(breite)
        self.__hoehe = float(hoehe)

    def __str__(self):
        return f"Quader: Element: {self.__symbol} - Breite: {self.__breite} - Länge: {self.__laenge} - Höhe {self.__hoehe}"

    def getMasse(self):
        return super().getMasse()

    def getVolumen(self):
        return super().getVolumen()


Silberbarren = Quader('Ag', 200, 50, 100)

print(Silberbarren)
print(Silberbarren.getMasse)
print(Silberbarren.getVolumen)
