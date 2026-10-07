import time
from Goal import goal
from Prints import print_command_not_found
import sys

# Lake functions:

# Boat lore:

def lore_boat():
    print(f"\nIf you choose to go this way, you will need a boat to get through the lake.")
    time.sleep(1)
    print(f"In order for you to build the boat, you will need to get wood. You will need 5 trees to build it.")
    time.sleep(1)
    print(f"You can get trees from The Wood. For each tree to cut, you will need to plant 2 seeds.")
    time.sleep(1)
    print(f"Check your bag to see how many seeds you have. If you do not have enough, you can trade-in some for some money in the trade-in store.")
    time.sleep(1)
    print(f"Once you have enough trees, come back here to build your boat.")
    time.sleep(1)

# Lake menu

def lake_menu(items):

    while True:

        boat = int(input("\n1 - Build boat\n2 - Cross the lake\n3 - Go back\n\n"))

        if boat == 1:
            if items["trees"] >= 5:
                build_boat(items)
            else:
                print("\nYou don't have enough trees! Go get some in The Wood!")
                time.sleep(2)
        elif boat == 2:
            if items["boat"] >= 1:
                goal("lake")
                sys.exit()
            else:
                print("\nYou don't have your boat yet! Build it first!")
                time.sleep(2)
        elif boat == 3:
            return
        else:
            print_command_not_found()

# Build boat

def build_boat(items):
    items["trees"] = items["trees"] - 5
    items["boat"] = 1
    print (f"\nYou now have a boat!")
    time.sleep(1)