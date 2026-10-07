# Import
import time
# From
from prints_package import print_command_not_found
from saved_data_package import save_game

# This function asks the player how many liters of water they need, sets the price for the water and informs the player.

def get_water_lore():

    while True:
                try:
                    how_much_water = int(input("\nHow many litres of water do you need? "))
                    break
                except ValueError:
                    print("\nCommand not valid. Try again!")
                    time.sleep(1)

    money_needed = how_much_water * 1
    time.sleep(1)
    print(f"\nWe charge for water in order to cover the costs of keeping it clean.\nYou will need {money_needed} coins to get that much water!")
    time.sleep(1)
    return how_much_water, money_needed  # This is returned to be passed to the following function.

# If the player tries to pump water, it will be checked if they have equal or more the price charged for the amount they choose.
    # If they do have the money, they will obtain the water and the money will be reduced accordingly.
    # If they don't have the money, a message will appear informing them and giving instruction on what to do.
# If they choose to go back, they will be sent back to the local trades menu.

# If the player chooses an invalid option, the program displays an error and asks again for a command.

def get_water(items, how_much_water, money_needed): # Items are passed (coming from main code) in order to evaluate the conditions.

    while True:

        while True:
            try:
                pump_water = int(input("\n1 - Start pumping\n2 - Go back\n\n"))
                break
            except ValueError:
                print("\nCommand not valid. Try again!")
                time.sleep(1)

        if pump_water == 1 and items["money"] >= money_needed:
            items["money"] = items["money"] - money_needed
            items["water"] = how_much_water
            save_game(items)
            print("\nPumping water:\n")
            time.sleep(1)
            for i in range(how_much_water):
                print("💧" * (i + 1))
                time.sleep(1)
            print("\nYou now have now " + str(items["water"]) + " litres of water!")
            time.sleep(1)
            break
        elif pump_water == 1 and items["money"] < money_needed:
            print("\nYou don't have enough money! Go trade-in some item in the trade-in store to get more coins!")
            time.sleep(1)
        elif pump_water == 2:
            return
        else:
            print_command_not_found()