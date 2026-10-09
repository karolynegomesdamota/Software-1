# Import
import time
import json
# From
from characters_package import choose_character

# When this function is called, a player name is asked and then a welcome message is displayed.
# Then the program reads 2 text files (one for introduction and another one for instructions).
# Finally, both the information requested here and the one returned from choose_character are stored in a dictionary and saved in a json file.
# The function returns items to be later used during the game in the main code.


def game_start():

    player_name = input ("\nEnter your name: ")
    time.sleep(0.5)

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

    return items # This is returned to be used within the main code.