import time
symbols_for_loading = ['⣾', '⣷', '⣯', '⣟', '⡿', '⢿', '⣻', '⣽']


def loading_animation(language):
    for _ in range(10):
        for symbol in symbols_for_loading:
            if language == "english":
                print(f'\r{symbol} Reading your thoughts...', flush=True, end='')
            else:
                print(f'\r{symbol} Lese deine Gedanken...', flush=True, end='')
            time.sleep(0.1)
    print("\r", end='')


def number_guessing_game(language, welcome_message):
    print(f"\n{welcome_message}")
    time.sleep(1.5)

    if language == "english":
        number = input("Insert a number: ")
    else:
        number = input("Gebe eine Zahl ein: ")
    loading_animation(language)

    if language == "english":
        input("\rPress ENTER to reveal my number...")
        print(number)
        print("Right?")
    else:
        input("\rDrücke ENTER, um meine Zahl aufzudecken...")
        print(number)
        print("Richtig?")
    time.sleep(2)


def main():
    print("Choose a language / Wählen Sie eine Sprache")
    de = 'deutsch'
    eng = 'english'
    while True:
        language_choice = input("Type/Tippe english or/oder deutsch: ").strip().lower()
        if language_choice in [eng, de]:
            break
        else:
            print(f"\nInvalid choice: \"{language_choice}\" Please type {eng} or {de}!", end='')
            time.sleep(3)
            print(f"\rUngültige Auswahl: \"{language_choice}\" Gebe bitte {eng} oder {de} ein!")

    if language_choice == de:
        number_guessing_game("deutsch", "Willkommen zu Potexxi's Zahlen Guesser!")
    elif language_choice == eng:
        number_guessing_game("english", "Welcome to Potexxi's Number Guesser!")


main()