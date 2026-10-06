import time
from Characters import choose_character
import json

def game_start():

    player_name = input ("\nEnter your name: ")

    while True:
        try:
            player_age = int(input ("Enter your age: "))
            break
        except ValueError:
            print("Age not valid. Try again!")

    if player_age < 12:
        print("\nYou are under 12! You cannot play this game!")
        time.sleep(1)
        print("\nExisting game...")
        time.sleep(1)
        print("\nExit completed!")
    else:
        print (f"\nWelcome, {player_name}!")
        time.sleep(2)

        items, chosen_character = choose_character()
        time.sleep(1)

        with open("Project/intro.txt", "r") as file:
            file_data = file.read()
            print(f"\n{file_data}")
        time.sleep(2)

        with open("Project/instructions.txt", "r") as file:
            file_data = file.read()
            print(f"\n{file_data}")
        time.sleep(2)

        save_data = {
        "player_name":player_name,
        "player_age":player_age,
        "chosen_character":chosen_character.name,
        "items":items
        }

        with open("Project/saved_game_data.json", "w") as file:
            json.dump(save_data, file)

    return items, chosen_character