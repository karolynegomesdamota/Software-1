# Import
import time
# From
from .characters_class import Character
from prints_package import print_command_not_found

# List created to store characters. Objects are created using a Class and at the same added to the list.

characters = []

characters.append(Character("Cris", 10, 0))
characters.append(Character("Toti", 0, 10))
characters.append(Character("Bal", 5, 5))

# Function created to choose one of the characters to play.
# Depending on which character is chosen from the list, the variables items and chosen characters are updated and returned.
# The information in passed in order to use it to do some actions during the game, especially the items variable.
# If the player chooses an invalid option, the program displays an error and asks again for a command.

def choose_character():
    print(f"\nChoose your character:")
    time.sleep(1)
    print(f"\nEach character comes with different items in their bags. Choose one and then figure out how that will affect your game!")
    time.sleep(1)
    print(f"\nPlease note this cannot be changed later on!")
    time.sleep(1)

    while True:

        while True:
            try:
                choose_character = int(input(f"\n 1 - {characters[0].name} - Bag: {characters[0].seeds} seeds and {characters[0].money} coins. \n 2 - {characters[1].name} - Bag: {characters[1].seeds} seeds and {characters[1].money} coins. \n 3 - {characters[2].name} - Bag: {characters[2].seeds} seeds and {characters[2].money} coins.\n\n"))
                time.sleep(1)
                break
            except ValueError:
                print("\nCommand not valid. Try again!")
                time.sleep(1)

        if choose_character == 1:
            print(f"\nYou chose {characters[0].name}!")
            time.sleep(1)
            items = {"seeds":characters[0].seeds, "money":characters[0].money, "trees":0, "water":0, "jacket":0, "boat":0}
            chosen_character = characters[0]
            return items, chosen_character # Returned to be used inside game_start. Why? To save this data to the save file for continuing the game later.
        elif choose_character == 2:
            print(f"\nYou chose {characters[1].name}!")
            time.sleep(1)
            items = {"seeds":characters[1].seeds, "money":characters[1].money, "trees":0, "water":0, "jacket":0, "boat":0}
            chosen_character = characters[1]
            return items, chosen_character # Returned to be used inside game_start. Why? To save this data to the save file for continuing the game later.
        elif choose_character == 3:
            print(f"\nYou chose {characters[2].name}!")
            time.sleep(1)
            items = {"seeds":characters[2].seeds, "money":characters[2].money, "trees":0, "water":0, "jacket":0, "boat":0}
            chosen_character = characters[2]
            return items, chosen_character # Returned to be used inside game_start. Why? To save this data to the save file for continuing the game later.
        else:
            print_command_not_found()