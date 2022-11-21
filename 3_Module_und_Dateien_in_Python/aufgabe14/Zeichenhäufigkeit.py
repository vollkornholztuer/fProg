def haeufigkeiten(string):
    for i in string:
        if not thisDict.__contains__(i):  # in i ist mein char drin
            thisDict[i] = string.count(i)


userInput = str(input("Geben sie einen String ein \n"))
thisDict = {}
haeufigkeiten(userInput)
print(thisDict)
