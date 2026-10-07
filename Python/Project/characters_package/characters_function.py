import time
from .characters_class import Character
from prints_package import print_command_not_found

characters = []

characters.append(Character("Cris", 10, 0))
characters.append(Character("Toti", 0, 10))
characters.append(Character("Bal", 5, 5))


def choose_character():
    print(f"\nChoose your character:")
    time.sleep(1)
    print(f"\nEach character comes with different items in their bags. Choose one and then figure out how that will affect your game!")
    time.sleep(1)
    print(f"\nPlease note this cannot be changed later on!")
    time.sleep(1)
    choose_character = int(input(f"\n 1 - {characters[0].name} - Bag: {characters[0].seeds} seeds and {characters[0].money} coins. \n 2 - {characters[1].name} - Bag: {characters[1].seeds} seeds and {characters[1].money} coins. \n 3 - {characters[2].name} - Bag: {characters[2].seeds} seeds and {characters[2].money} coins.\n\n"))
    while choose_character != 1 or 2 or 3:
        if choose_character == 1:
            print(f"\nYou chose {characters[0].name}!")
            items = {"seeds":characters[0].seeds, "money":characters[0].money, "trees":0, "water":0, "jacket":0, "boat":0}
            time.sleep(1)
            chosen_character = characters[0]
            return items, chosen_character
        elif choose_character == 2:
            print(f"\nYou chose {characters[1].name}!")
            items = {"seeds":characters[1].seeds, "money":characters[1].money, "trees":0, "water":0, "jacket":0, "boat":0}
            time.sleep(1)
            chosen_character = characters[1]
            return items, chosen_character
        elif choose_character == 3:
            print(f"\nYou chose {characters[2].name}!")
            items = {"seeds":characters[2].seeds, "money":characters[2].money, "trees":0, "water":0, "jacket":0, "boat":0}
            time.sleep(1)
            chosen_character = characters[2]
            return items, chosen_character
        else:
            print_command_not_found()
            choose_character = int(input(f"\n 1 - {characters[0].name} - Bag: {characters[0].seeds} seeds and {characters[0].money} coins. \n 2 - {characters[1].name} - Bag: {characters[1].seeds} seeds and {characters[1].money} coins. \n 3 - {characters[2].name} - Bag: {characters[2].seeds} seeds and {characters[2].money} coins.\n\n"))
            time.sleep(2)