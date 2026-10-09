# Import
import time
import sys
# From
from goal_package import goal
from prints_package import print_command_not_found

# This function serves simply to print information about the chosen path.

def lore_freezing_mountain():
    print(f"\nCrossing the Freezing Mountains: ")
    time.sleep(1)
    print(f"\nIf you choose to go this way, you will need a jacket to get through the freezing mountains.")
    print(f"In order for you to get a jacket, you will need to buy it from the second hand store. It costs 10 coins.")
    print(f"Check your back to see how much money you have. If you do not have enough, you can trade some items in the trade-in store.")
    print(f"Once you have a jacket, come back here to start your journey.")
    time.sleep(1)

# This function asks the player whether they want to go through the freezing mountains or go back to the previous menu.
# If the player chooses to go through the mountains, it will be checked if they have a jacket.
    # If they do, they will go through the mountains, reach their goal and the game will finish.
    # If they don't, a message will appear informing them and giving instruction on what to do.
# If they choose to go back, they will be sent back to the paths menu.

# If the player chooses an invalid option, the program displays an error and asks again for a command.

def freezing_mountain_menu(items):

    while True:

        while True:
            try:
                start_mountain = int(input("\n1 - Go through the mountain\n2 - Go back\n\n"))
                time.sleep(1)
                break
            except ValueError:
                print("\nCommand not valid. Try again!")
                time.sleep(1)

        if start_mountain == 1:
            if items["jacket"] >= 1:
                goal("freezing_mountain")
                sys.exit()
            else:
                print("\nYou don't have a jacket! Go buy one!")
                time.sleep(1)
        elif start_mountain == 2:
            return
        else:
            print_command_not_found()