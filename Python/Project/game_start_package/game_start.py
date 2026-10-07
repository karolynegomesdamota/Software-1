import time
from characters_package import choose_character
import json

def game_start():

    player_name = input ("\nEnter your name: ")

    print (f"\nWelcome, {player_name}!")
    time.sleep(1)

    items, chosen_character = choose_character()

    with open("Project/texts_package/intro.txt", "r") as file:
        file_data = file.read()
        print(f"\n{file_data}")
    time.sleep(1)

    with open("Project/texts_package/instructions.txt", "r") as file:
        file_data = file.read()
        print(f"\n{file_data}")
    time.sleep(1)

    save_data = {
    "player_name":player_name,
    "chosen_character":chosen_character.name,
    "items":items
    }

    with open("Project/saved_data_package/saved_game_data.json", "w") as file:
        json.dump(save_data, file)

    return items, chosen_character