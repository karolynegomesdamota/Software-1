from Goal import goal
from Print_CommandNotFound import print_command_not_found
from Menus import way_home_menu

# Lake functions:

# Boat lore:

def lore_boat():
    print(f"\nIf you choose to go this way, you will need a boat to get through the lake.")
    print(f"In order for you to build the boat, you will need to get wood. You will need 5 trees to build it.")
    print(f"You can get trees from The Wood. For each tree to cut, you will need to plant 2 seeds.")
    print(f"Check your bag to see how many seeds you have. If you do not have enough, you can trade-in some for some money in the trade-in store.")

    print(f"Once you have enough trees, come back here to build your boat.")

# Check wood

def check_wood(items):

    boat = int(input("\nPress 1 to build the boat: \n1 - Build boat.\n2 - Go back.\n\n"))
    if boat == 1:
        if items["trees"] >= 5:
            build_boat(items)
            goal()
        else:
            print("\nYou don't have enough trees! Go get some in The Wood!")
    elif boat == 2:
        way_home = way_home_menu() # This to make the way home menu to show and ask for a new option
        return way_home # This to pass the new option inside the already first chosen option.

    else:
        print_command_not_found()

# Build boat

def build_boat(items):
    if items["trees"] == 5:
        items["trees"] = 0
        items["boat"] = 1
        print (f"\nYou now have " + str(items["trees"]) + " trees and " + str(items["boat"]) + " boat!")