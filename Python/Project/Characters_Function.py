import time
from Classes import Character
from Print_CommandNotFound import print_command_not_found

character1 = Character("Cris", 10, 0)
character2 = Character("Toti", 0, 10)
character3 = Character("Bal", 5, 5)

def choose_character():
    print (f"\nChoose your character:")
    print (f"\nPlease note this cannot be changed later on!")
    choose_character = int(input(f"\n 1 - {character1.name} with {character1.seeds} seeds and {character1.money} coins. \n 2 - {character2.name} with {character2.seeds} seeds and {character2.money} coins. \n 3 - {character3.name} with {character3.seeds} seeds and {character3.money} coins.\n\n"))
    while choose_character != 1 or 2 or 3:
        if choose_character == 1:
            print(f"\nYou chose {character1.name}!\n")
            items = {"seeds":character1.seeds, "money":character1.money, "trees":0, "water":0, "jacket":0}
            time.sleep(2)
            return items
        elif choose_character == 2:
            print(f"\nYou chose {character2.name}!\nY")
            items = {"seeds":character2.seeds, "money":character2.money, "trees":0, "water":0, "jacket":0}
            time.sleep(2)
            return items
        elif choose_character == 3:
            print(f"\nYou chose {character3.name}!\nY")
            items = {"seeds":character3.seeds, "money":character3.money, "trees":0, "water":0, "jacket":0}
            time.sleep(2)
            return items
        else:
            print_command_not_found()
            choose_character = int(input(f"\n 1 - {character1.name} with {character1.seeds} seeds and {character1.money} coins. \n 2 - {character2.name} with {character2.seeds} seeds and {character2.money} coins. \n 3 - {character3.name} with {character3.seeds} seeds and {character3.money} coins.\n\n"))
            time.sleep(2)