# ---------------------------------------------------
# Dateiname: geldproperties.py
# Klasse Geld mit privaten Attributen und Properties
# Objektorientierte Programmierung mit Python
# Kap. 10
# Michael Weigend 20.9.2009
#----------------------------------------------------
class Geld(object):
    __wechselkurs={'USD':0.84998,
                   'GBP':1.39480,
                   'EUR':1.0,
                   'JPY':0.007168} 
    def __init__(self, waehrung='EUR', betrag=0.0):
        self.__waehrung = waehrung
        self.__betrag = float(betrag)

    @property
    def betrag(self):
        return self.__betrag

    @property
    def waehrung(self):
        return self.__waehrung

    def getEuro(self):                                 
        return self.__betrag *   \
              self.__wechselkurs[self.__waehrung]

    @betrag.setter
    def betrag(self, neuerBetrag):
        self.__betrag = float (neuerBetrag)
    
    @waehrung.setter
    def waehrung(self, neueWaehrung):
        if neueWaehrung in self.__wechselkurs.keys():
            alt = self.__wechselkurs[self.__waehrung]
            neu = self.__wechselkurs[neueWaehrung]
            self.__betrag = alt/neu * self.__betrag
            self.__waehrung = neueWaehrung
   
    def add (self, geld):                              
        summe_in_Euro = self.getEuro()+geld.getEuro()
        summe = Geld(self.__waehrung,
             summe_in_Euro/self.__wechselkurs[self.__waehrung])
        return summe

bestellung = Geld()
bestellung.betrag = 47.11
bestellung.waehrung = 'USD'
beitrag = Geld('EUR', 120)

print(bestellung.betrag, bestellung.waehrung)

summe = beitrag.add(bestellung)
print(summe.betrag, summe.waehrung)
