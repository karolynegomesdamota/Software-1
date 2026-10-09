from main_menus_package import main_menu, path_menu, local_trades
from prints_package import print_command_not_found, print_panel
import time
import json
import os
from game_start_package import game_start

# This variable has been created to record the exact location where the file that saves the game will be.

save_data_file_path = 'Project/saved_data_package/saved_game_data.json'

# Here the program checks if the file exists.
# If yes, it retrieves the information from the previous game. Even within this, the player can choose to initiate a new game.
# If the player chooses to continue, the recorded information will be printed and assigned to variables to be used during the game.
# If not, it will trigger a new game to start.

# If the player chooses an invalid option, the program displays an error and asks again for a command.

if os.path.exists(save_data_file_path):

    while True:

        while True:
                try:
                    continue_previous_game = int(input("\nDo you want to continue the previous game?\n\n1 - Yes\n2 - No\n\n"))
                    time.sleep(1)
                    break
                except ValueError:
                    print("\nCommand not valid. Try again!")
                    time.sleep(1)

        if continue_previous_game == 1:
            print("\nContinuing the previous game...")
            time.sleep(1)
            with open("Project/saved_data_package/saved_game_data.json", "r") as file:
                file_data = json.load(file)
                player_name = {file_data['chosen_character']}
                chosen_character = {file_data['chosen_character']}
                items = file_data['items']
                print(f"\nPlayer name: {file_data['player_name']}")
                time.sleep(1)
                print(f"\nCharacter previously chosen: {file_data['chosen_character']}")
                time.sleep(1)
                print_panel(items)
                break
        elif continue_previous_game == 2:
            print("\nStarting new game...")
            items = game_start()
            break
        else:
            print_command_not_found()

else:
    items = game_start()

# This part calls the main menu (displays the options) and forces the player to choose a command.
# If the command is not valid, the program will display an error and request the command again.
# The options are:
    # Opening the paths menu (paths to get to the goal).
    # Printing the content of the character's bag.
    # Opening the local trades menu.
    # Exit

# If the player chooses an invalid option, the program displays an error and asks again for a command.

while True:

    while True:
        try:
            command = main_menu()
            break
        except ValueError:
            print("\nCommand not valid. Try again!")
            time.sleep(1)

    if command == 1:
        path_menu(items)
    elif command == 2:
        print_panel (items)
    elif command == 3:
        local_trades(items)
    elif command == 4:
        print("\nExiting game...")
        time.sleep(1)
        print("\nExit completed!\n")
        time.sleep(1)
        break
    else:
        print_command_not_found()