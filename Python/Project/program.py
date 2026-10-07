from Menus import main_menu, room_menu, path_menu
from Rooms import second_hand, cut_wood, trade_in_, get_water, second_hand_lore, get_water_lore, cut_wood_lore
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
        room = room_menu()
        while room != 5:
            if room == 1:
                how_many_trees, seeds_needed = cut_wood_lore()
                cut_wood(items, how_many_trees, seeds_needed) # TODO: Rename function and variable within it to make more sense and to be more clear.
                room = room_menu()
            elif room == 2:
                money_needed_jacket = second_hand_lore()
                second_hand(items, money_needed_jacket) # TODO: Rename function and variable within it to make more sense and to be more clear.
                room = room_menu()
            elif room == 3:
                how_much_water, money_needed = get_water_lore()
                get_water(items, how_much_water, money_needed) # TODO: Rename function and variable within it to make more sense and to be more clear.
                room = room_menu()
            elif room == 4:
                trade_in_(items) # TODO: Rename function and variable within it to make more sense and to be more clear.
                room = room_menu()
            else:
                print_command_not_found()
                room = room_menu()
    elif command == 4:
        print("\nExiting game...")
        time.sleep(1)
        print("\nExit completed!\n")
        break
    else:
        print_command_not_found()