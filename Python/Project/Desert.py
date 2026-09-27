import time
from Goal import goal
from Print_CommandNotFound import print_command_not_found
from Menus import way_home_menu

# Desert functions:

# Desert lore:

def lore_desert():
    print(f"\nIf you choose to go this way, you will need water to get through the desert.")
    time.sleep(5)
    print(f"In order for you to get water, you will need to pump it from the well. You will need 10 liters of water to cross the desert.")
    time.sleep(10)
    print(f"The farmer who owns the well will charge you 1 coin per liter.")
    time.sleep(5)
    print(f"Check your bag to see how much money you have. If you do not have enough, you can trade some items in the trade-in store.")
    time.sleep(10)
    print(f"Once you have enough water, come back here to start your journey.")
    time.sleep(5)

# Check water

def check_water(items):

    start_desert = int(input("\nPress 1 to start your journey: \n1 - Go through the desert\n2 - Go back\n\n"))
    if start_desert == 1:
        if items["water"] >= 10:
            goal()
        else:
            print("\nYou don't have enough water! Go pump some from the well!")
    elif start_desert == 2:
        way_home = way_home_menu() # This to make the way home menu to show and ask for a new option
        return way_home # This to pass the new option inside the already first chosen option.
    else:
        print_command_not_found()