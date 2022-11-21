from unittest import result

choice = 0


def encrypt(userInput, dist):
    result = ""
    # Text durchgehen
    for i in range(len(userInput)):
        char = userInput[i]

        # Enkodierung Großbuchstaben
        if (char.isupper()):
            result += chr((ord(char) + dist-65) % 26 + 65)

        # Enkodierung Kleinbuchstaben
        else:
            result += chr((ord(char) + dist - 97) % 26 + 97)

    return result


def decrypt(userInput, dist):
    result = ""

    # text durchgehen
    for i in range(len(userInput)):
        char = userInput[i]

        # dekodierung Großbuchstaben
        if (char.isupper()):
            result += chr((ord(char) - dist - 65) % 26 + 65)

        else:
            result += chr((ord(char) - dist - 97) % 26 + 97)

    return result


userInput = str(input('Geben sie ihren Text ein\n'))
print('Eingegebener Text:', userInput)
choice = int(input('0 - für entschlüsselung, 1 - für verschlüsselung\n'))
dist = int(input(
    'Um wie viele Zeichen im Alphabet sollen die Buchstaben verschoben werden?\n'))

if choice == 1:
    print('Cipher:', encrypt(userInput, dist))
else:
    print('Cipher:', decrypt(userInput, dist))
