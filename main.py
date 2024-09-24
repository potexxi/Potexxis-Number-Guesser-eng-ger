

input ("Wählen Sie eine Sprache");
input ("Choose a language");

x = input ("Type/Tippe english or/oder deutsch: ");

y = 'deutsch'
u = 'english'

if x == y:
    input("Wilkommen zu Potexxi's Zahlen Guesser!");
    z = input ("Gebe eine Zahl ein: ")
    import time
    symbols = ['⣾', '⣷', '⣯', '⣟', '⡿', '⢿', '⣻', '⣽']
    i = 3
    i = (i + 1) % len(symbols)
    print('\r\033[K%s Lese deine Gedanken...' % symbols[i], flush=True, end='')
    time.sleep(4)

    input ("   drücke ENTER, um meine Zahl aufzudecken")

    print (z)
    input ("Richtig?");


if x == u:
    input("Welcome to Potexxis's Number Guesser!");
    o = input ("Insert a number: ");

    import time

    symbols = ['⣾', '⣷', '⣯', '⣟', '⡿', '⢿', '⣻', '⣽']
    i = 3
    i = (i + 1) % len(symbols)
    print('\r\033[K%s Read your thoughts...' % symbols[i], flush=True, end='')
    time.sleep(4)

    input("   press ENTER to reveal my number");

    print(o);
    input("Right?");




