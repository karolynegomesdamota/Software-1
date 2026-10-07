# Import
import time
# From
from prints_package import print_command_not_found
from saved_data_package import save_game

# This function asks the player how many trees they need, sets the amount of seeds needed and informs the player.

def the_woods_lore():

    while True:
                try:
                    how_many_trees = int(input("\nHow many trees do you need? "))
                    break
                except ValueError:
                    print("\nCommand not valid. Try again!")
                    time.sleep(1)

    seeds_needed = how_many_trees * 2
    print(f"\nYou will need to plant {seeds_needed} seeds if you want to cut that many trees!")
    time.sleep(1)
    return how_many_trees, seeds_needed # This is returned to be passed to the following function.

# If the player tries to cut trees, it will be checked if they have equal or more the amount of sees needed.
    # If they do have enough seeds, they will obtain the trees and the seeds will be reduced accordingly from their bag.
    # If they don't have the seeds, a message will appear informing them and giving instruction on what to do.
# If they choose to go back, they will be sent back to the local trades menu.

# If the player chooses an invalid option, the program displays an error and asks again for a command.

def the_woods(items, how_many_trees, seeds_needed): # Items are passed (coming from main code) in order to evaluate the conditions.

    while True:

        while True:
            try:
                cut_tree = int(input("\n1 - Start cutting \n2 - Go back\n\n"))
                break
            except ValueError:
                print("\nCommand not valid. Try again!")
                time.sleep(1)

        if cut_tree == 1 and items["seeds"] >= seeds_needed:
            items["seeds"] = items["seeds"] - seeds_needed
            items["trees"] = items["trees"] + how_many_trees
            save_game(items)
            print("\nCutting trees:\n")
            time.sleep(1)
            for i in range(how_many_trees):
                print("🪵" * (i + 1))
                time.sleep(1)
            print("\nYou now have " + str(items["trees"]) + " trees!")
            time.sleep(1)
            break
        elif cut_tree == 1 and items["seeds"] < seeds_needed:
            print("\nYou don't have enough seeds! Go trade money to get more!")
            time.sleep(1)
        elif cut_tree == 2:
            return
        else:
            print_command_not_found()