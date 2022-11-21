inseln = ["Bermudas", "Fidschi", "Komoren",
          "Kuba"]  # Liste von Strings mit namen
index = [1, 3, 0, 2]  # Liste von Integers, die dann als Index dienen

y = 0
ref = 0

while y < 4:
    # der Wert am Index der Liste "index" wird in "ref" gespeichert
    ref = index[y]
    # mit "ref" wird auf die insel-Liste zugegriffen und der Wert wird ausgegeben
    print("Insel:", inseln[ref])
    y += 1
