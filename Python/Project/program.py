from Menus import main_menu, room_menu, path_menu
from Prints import print_command_not_found, print_panel
import time
import json
import os
from Game_start import game_start

save_data_file_path = 'Project/saved_game_data.json'

if os.path.exists(save_data_file_path):
    continue_previous_game = int(input("\nDo you want to continue the previous game?\n\n1 - Yes\n2 - No\n\n"))
    if continue_previous_game == 1:
        print("\nContinuing the previous game...")
        with open("Project/saved_game_data.json", "r") as file:
            file_data = json.load(file)
            player_name = {file_data['chosen_character']}
            player_age = {file_data['player_age']}
            chosen_character = {file_data['chosen_character']}
            items = file_data['items']
            print(f"\nPlayer name: {file_data['player_name']}")
            print(f"\nCharacter previously chosen: {file_data['chosen_character']}")
            print_panel(items)
    elif continue_previous_game == 2:
        print("\nStarting new game...")
        items, chosen_character = game_start()
else:
    items, chosen_character = game_start()

while True:

    command = main_menu()

    if command == 1:
        path_menu(items)
    elif command == 2:
        print_panel (items)
    elif command == 3:
        room_menu(items)
    elif command == 4:
        print("\nExiting game...")
        time.sleep(1)
        print("\nExit completed!\n")
        break
    else:
        print_command_not_found()