import time
from goal_package import goal
from prints_package import print_command_not_found
import sys

# Freezing mountain functions:

# Freezing mountain lore:

def lore_freezing_mountain():
    print(f"\nCrossing the Frozen Mountains:: ")
    print(f"\nIf you choose to go this way, you will need a jacket to get through the freezing mountains.")
    print(f"In order for you to get a jacket, you will need to buy it from the second hand store. It costs 10 coins.")
    print(f"Check your back to see how much money you have. If you do not have enough, you can trade some items in the trade-in store.")
    print(f"Once you have a jacket, come back here to start your journey.")
    time.sleep(1)

# Freezing mountain menu

def freezing_mountain_menu(items):

    while True:

        while True:
            try:
                start_mountain = int(input("\n1 - Go through the mountain\n2 - Go back\n\n"))
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
        elif start_mountain == 2:
            return
        else:
            print_command_not_found()