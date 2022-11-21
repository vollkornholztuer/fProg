import random
z = random.randint(0, 9)
lives = 3

print('Das ist ein Zahlenratespiel. Die zahl liegt zufällig zwischen 0 und 9. - 0 und 9 sind inbegriffen.')
print('Du hast 3 Versuche um die Zahl richtig zu erraten')

win = 0

while lives > 0:
    userInput = int(input('Errate die Zahl:'))

    if userInput == z:
        win = 1
        lives = 0
    else:
        lives -= 1
        if (userInput > z):
            print('die gesuchte Zahl ist kleiner')
        else:
            print('die gesuchte Zahl ist größer')

if win == 1:
    print('Du hast das Spiel gewonnen! - Starte das Programm neu um es nochmal zu spielen!')
else:
    print('Du hast das Spiel verloren. - Die gesuchte Zahl war', z)
    print('Starte das Programm neu um es nochmal zu spielen!')
