import time
from Classes import Character
from Print_CommandNotFound import print_command_not_found

characters = []

characters.append(Character("Cris", 10, 0))
characters.append(Character("Toti", 0, 10))
characters.append(Character("Bal", 5, 5))


def choose_character():
    print (f"\nChoose your character:")
    print (f"\nPlease note this cannot be changed later on!")
    choose_character = int(input(f"\n 1 - {characters[0].name} with {characters[0].seeds} seeds and {characters[0].money} coins. \n 2 - {characters[1].name} with {characters[1].seeds} seeds and {characters[1].money} coins. \n 3 - {characters[2].name} with {characters[2].seeds} seeds and {characters[2].money} coins.\n\n"))
    while choose_character != 1 or 2 or 3:
        if choose_character == 1:
            print(f"\nYou chose {characters[0].name}!\n")
            items = {"seeds":characters[0].seeds, "money":characters[0].money, "trees":0, "water":0, "jacket":0}
            time.sleep(2)
            chosen_character = characters[0]
            return items, chosen_character
        elif choose_character == 2:
            print(f"\nYou chose {characters[1].name}!\nY")
            items = {"seeds":characters[1].seeds, "money":characters[1].money, "trees":0, "water":0, "jacket":0}
            time.sleep(2)
            chosen_character = characters[1]
            return items, chosen_character
        elif choose_character == 3:
            print(f"\nYou chose {characters[2].name}!\nY")
            items = {"seeds":characters[2].seeds, "money":characters[2].money, "trees":0, "water":0, "jacket":0}
            time.sleep(2)
            chosen_character = characters[2]
            return items, chosen_character
        else:
            print_command_not_found()
            choose_character = int(input(f"\n 1 - {characters[0].name} with {characters[0].seeds} seeds and {characters[0].money} coins. \n 2 - {characters[1].name} with {characters[1].seeds} seeds and {characters[1].money} coins. \n 3 - {characters[2].name} with {characters[2].seeds} seeds and {characters[2].money} coins.\n\n"))
            time.sleep(2)