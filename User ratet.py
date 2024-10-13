import random
import time

geheimzahl = random.randint(1,100)

print("Willkommen zum Zahlenratespiel!")
time.sleep(2)
input("Druecke ENTER um zu beginnen!")
print("Ich denke mir eine Zahl zwischen 1 und 100 aus!")
time.sleep(2)
print("Ich bin bereit!\n")

versuche = 0
geraten = False

while not geraten:
    tipp = int(input("Dein Tipp: "))
    versuche += 1

    if tipp < geheimzahl:
        print("Zu niedrig!\n")

    if tipp > geheimzahl:
        print("Zu hoch!\n")

    if tipp == geheimzahl:
        geraten = True
        print(f"Glueckwunsch! Du hast die Zahl {geheimzahl} in {versuche} Versuchen erraten!")
        time.sleep(5)
