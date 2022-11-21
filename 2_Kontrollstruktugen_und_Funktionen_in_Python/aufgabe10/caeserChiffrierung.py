# print('Dieses Programm entschlüsselt oder verschlüsselt Text nach der Caeser-Chiffrierung')
def caesar_encode(src, dist):
    list = []
    for i in src:
        list.append(i)
    print(list)

    newList = []

    for i in list:
        for j in range(alphaLower):
            if alphaLower[j] == list[i]:
                newList.append(alphaLower[j+1])
            elif alphaUpper[j] == list[i]:
                newList.append(alphaUpper[j+1])


def caesar_decode(src, dist):
    list = []
    for i in src:
        list.append(i)
    print(list)

    for i in list:
        for j in alphaLower:
            if alphaLower[j] == list[i]:
                test = 0

#
#
#


userInput = int(input('0 - für entschlüsselung, 1 - für verschlüsselung\n'))
src = 0
dist = 0

alphaLower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
              'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphaUpper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
              'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

if userInput == 0:  # entschlüsseln
    src = str(input('Geben Sie den zu entschlüsselnden Satz ein\n'))
    dist = int(input(
        'Geben Sie die Zahl an, womit die Buchstaben im Text beim Alphabet verschoben werden\n'))
    caesar_decode(src, dist)

elif userInput == 1:  # verschlüsseln
    src = str(input('Geben Sie den zu verschlüsselnden Satz ein\n'))
    dist = int(input(
        'Geben Sie die Zahl an, womit die Buchstaben im Text beim Alphabet verschoben werden\n'))
    caesar_encode(src, dist)
