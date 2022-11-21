# Sank yu Kaddah

class sparseVector:
    def __init__(self):  # Konstruktor
        self.vector = {}  # Dictionary, kein Array

    def __getitem__(self, key):  # holt Wert aus dem Index
        if key in self.vector:
            return self.vector[key]
        return 0

    def __setitem__(self, key, value):  # setzt Wert zum Index rein
        self.vector[key] = float(value)


s = sparseVector()  # neuer Vektor (Dictionary)

s[17] = 3.14  # in Index 17, Value 3.14
s[34] = 6.28  # in Index 34, Value 6.28
s[1234] = 0.001  # in Index 1234, Value 0.001
# s[47] = (1.1, 1.2)

print("Wert[", 17, "] = ", s[17])
print("Wert[", 34, "] = ", s[34])
print("Wert[", 35, "] = ", s[35])

for i in range(10, 36):
    print("Wert[", i, "] = ", s[i], end=", ")
