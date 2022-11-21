# ---------------------------------------------------
# Dateiname: Defist.py
# Klasse NewList, von Basisklasse list abgeleitet
# Objektorientierte Programmierung mit Python
# Kap. 10
# Michael Weigend 20.4.2006
#----------------------------------------------------
class Defaultlist(list):
    def __init__(self, s=[], default=0):
        self.default = default
        list.__init__(self, s)

    def __getitem__(self, index):
        try:
            return super().__getitem__(index)
        except IndexError:
            return self.default

    def __add__ (self, other):
        result = list.__add__ (self, other)
        print("other:", other)
        return Defaultlist(result, self.default)
        

p = ["Bronze", "Silber", "Gold"]
medaillen = Defaultlist(p, "Papier")

print(medaillen)

print(medaillen[2])

print(medaillen[3])

m2 = Defaultlist(["Eisen", "Glas", "Rost"], "Unbekannt")
m3 = Defaultlist(["Plaste", "Blech", "Holz"], "Nix")

m = medaillen + m2 + m3 # entspricht (medaillen.__add__(m2)).__add__(m3)

print(m)
print(m[10])
print(p[10])