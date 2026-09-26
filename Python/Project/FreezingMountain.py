from Goal import goal
from Print_CommandNotFound import print_command_not_found
from Menus import way_home_menu

# Freezing mountain functions:

# Freezing mountain lore:

def lore_freezing_mountain():
    print(f"\nIf you choose to go this way, you will need a jacket to get through the freezing mountains.")
    print(f"In order for you to get a jacket, you will need to buy it from the second hand store. It costs 10 coins.")
    print(f"Check your panel to see how much money you have. If you do not have enough, you can trade some items in the trade-in store.")

    print(f"Once you have a jacket, come back here to start your journey.")

# Check jacket

def check_jacket(items):

    start_mountain = int(input("\nPress 1 to start your journey: \n1 - Go through the mountain. \n2 - Go back\n\n"))
    if start_mountain == 1:
        if items["jacket"] >= 1:
            goal()
        else:
            print("\nYou don't have a jacket! Go buy one!")
    elif start_mountain == 2:
        way_home = way_home_menu() # This to make the way home menu to show and ask for a new option
        return way_home # This to pass the new option inside the already first chosen option.
    else:
        print_command_not_found()