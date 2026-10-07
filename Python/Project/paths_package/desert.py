# Import
import time
import sys
# From
from goal_package import goal
from prints_package import print_command_not_found

# This function serves simply to print information about the chosen path.

def lore_desert():
    print(f"\nCrossing the Desert: ")
    print(f"\nIf you choose to go this way, you will need water to get through the desert.")
    print(f"In order for you to get water, you will need to pump it from The Well. You will need 10 liters of water to cross the desert.")
    print(f"The farmer who owns the well will charge you 1 coin per liter.")
    print(f"Check your bag to see how much money you have. If you do not have enough, you can trade some items in the trade-in store.")
    print(f"Once you have enough water, come back here to start your journey.")
    time.sleep(1)

# This function asks the player whether they want to go through the desert or go back to the previous menu.
# If the player chooses to go through the desert, it will be checked if they have equal or more the amount of water necessary.
    # If they do, they will go through the desert, reach their goal and the game will finish.
    # If they don't, a message will appear informing them and giving instruction on what to do.
# If they choose to go back, they will be sent back to the paths menu.

# If the player chooses an invalid option, the program displays an error and asks again for a command.

def desert_menu(items):

    while True:

        while True:
            try:
                start_desert = int(input("\n1 - Go through the desert\n2 - Go back\n\n"))
                break
            except ValueError:
                print("\nCommand not valid. Try again!")
                time.sleep(1)

        if start_desert == 1:
            if items["water"] >= 10:
                goal("desert")
                sys.exit()
            else:
                print("\nYou don't have enough water! Go pump some from the well!")
                time.sleep(1)
        elif start_desert == 2:
            return
        else:
            print_command_not_found()