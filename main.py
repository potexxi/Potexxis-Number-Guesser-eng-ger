
import time

print ("Wählen Sie eine Sprache")
time.sleep(1.5)

print ("Choose a language")
time.sleep(1.5)

x = input ("Type/Tippe english or/oder deutsch: ")

y = 'deutsch'
u = 'english'

if x != y and x != u:
    print ("ERROR!")
    time.sleep(3)

elif x == y:
    print("Wilkommen zu Potexxi's Zahlen Guesser!")
    time.sleep(2)
    z = input ("Gebe eine Zahl ein: ")
    symbols = ['⣾', '⣷', '⣯', '⣟', '⡿', '⢿', '⣻', '⣽']
    i = 3
    i = (i + 1) % len(symbols)
    print('\r\033[K%s Lese deine Gedanken...' % symbols[i], flush=True, end='')
    time.sleep(3.5)
    input ("   drücke ENTER, um meine Zahl aufzudecken")
    print (z)
    input ("Richtig?")


elif x == u:
    print("Welcome to Potexxis's Number Guesser!")
    time.sleep(2)
    o = input ("Insert a number: ")
    symbols = ['⣾', '⣷', '⣯', '⣟', '⡿', '⢿', '⣻', '⣽']
    i = 3
    i = (i + 1) % len(symbols)
    print('\r\033[K%s Read your thoughts...' % symbols[i], flush=True, end='')
    time.sleep(3.5)
    input("   press ENTER to reveal my number")
    print(o)
    input("Right?")
