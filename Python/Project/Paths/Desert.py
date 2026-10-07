import time
from Goal import goal
from Prints import print_command_not_found
import sys

# Desert functions:

# Desert lore:

def lore_desert():
    print(f"\nIf you choose to go this way, you will need water to get through the desert.")
    time.sleep(1)
    print(f"In order for you to get water, you will need to pump it from the well. You will need 10 liters of water to cross the desert.")
    time.sleep(1)
    print(f"The farmer who owns the well will charge you 1 coin per liter.")
    time.sleep(1)
    print(f"Check your bag to see how much money you have. If you do not have enough, you can trade some items in the trade-in store.")
    time.sleep(1)
    print(f"Once you have enough water, come back here to start your journey.")
    time.sleep(1)

# Desert menu

def desert_menu(items):

    while True:

        start_desert = int(input("\n1 - Go through the desert\n2 - Go back\n\n"))

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