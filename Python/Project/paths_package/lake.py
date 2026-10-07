import time
from goal_package import goal
from prints_package import print_command_not_found
import sys

# Lake functions:

# Boat lore:

def lore_boat():
    print(f"\nCrossing the Lake: ")
    print(f"\nIf you choose to go this way, you will need a boat to get through the lake.")
    print(f"In order for you to build the boat, you will need to get wood. You will need 5 trees to build it.")
    print(f"You can get trees from The Wood. For each tree to cut, you will need to plant 2 seeds.")
    print(f"Check your bag to see how many seeds you have. If you do not have enough, you can trade-in some for some money in the trade-in store.")
    print(f"Once you have enough trees, come back here to build your boat.")
    time.sleep(1)

# Lake menu

def lake_menu(items):

    while True:

        while True:
            try:
                boat = int(input("\n1 - Build boat\n2 - Cross the lake\n3 - Go back\n\n"))
                break
            except ValueError:
                print("\nCommand not valid. Try again!")
                time.sleep(1)

        if boat == 1:
            if items["trees"] >= 5:
                build_boat(items)
            else:
                print("\nYou don't have enough trees! Go get some in The Wood!")
                time.sleep(1)
        elif boat == 2:
            if items["boat"] >= 1:
                goal("lake")
                sys.exit()
            else:
                print("\nYou don't have your boat yet! Build it first!")
                time.sleep(1)
        elif boat == 3:
            return
        else:
            print_command_not_found()

# Build boat

def build_boat(items):
    items["trees"] = items["trees"] - 5
    items["boat"] = 1
    print (f"\nYou now have a boat! ⛵️")
    time.sleep(1)