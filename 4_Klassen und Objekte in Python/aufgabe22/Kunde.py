# Sources
# https://www.google.com/search?q=python+count+created+objects&oq=python+count+created+objects&aqs=chrome..69i57.6294j0j1&sourceid=chrome&ie=UTF-8
# https://stackoverflow.com/questions/6179182/python-how-to-count-the-number-of-objects-created
# https://www.includehelp.com/python/program-to-count-number-of-objects-created.aspx
# https://www.digitalocean.com/community/tutorials/python-static-method
# https://www.geeksforgeeks.org/destructors-in-python/

class Kunde:
    # Zum zählen der erstellten objekte
    counter = 0

    def __init__(self, nr=0, name=""):
        self.__nummer = nr
        self.__name = name
        print("Kunde wurde erstellt. - Name: " +
              self.__name + " - Nummer: " + str(self.__nummer))

        # Zum hochzählen, weil erstelltes Objekt
        Kunde.counter += 1

    def getNummer(self):
        return self.__nummer

    def getName(self):
        return self.__name

    def __str__(self):
        beschr = str(self.__nummer) + ": " + self.__name
        return beschr

    @staticmethod
    def getAmountOfObject():
        text = "Es wurden " + str(Kunde.counter) + " Kunden erstellt"
        return text

    def __del__(self):
        Kunde.counter -= 1
        print('Destruktor aufgerufen. - Kunde wurde gelöscht')


kunde1 = Kunde(1, "Bob")
kunde2 = Kunde(2, "Beep")
kunde3 = Kunde(3, "Boop")

print(Kunde.getAmountOfObject())

print(kunde1.__str__())
print(kunde2.__str__())
print(kunde3.__str__())

del kunde1
del kunde2
del kunde3

print(Kunde.getAmountOfObject())
