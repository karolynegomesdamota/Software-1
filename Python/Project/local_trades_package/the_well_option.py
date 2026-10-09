# Import
import time
# From
from prints_package import print_command_not_found
from saved_data_package import save_game

def the_well(items): # Items are passed (coming from main code) in order to evaluate the conditions.

    # This next block asks the player how many liters of water they need, sets the price for the water and informs the player of the price.

    while True:
                try:
                    how_much_water = int(input("\nHow many litres of water do you need? "))
                    time.sleep(1)
                    break
                except ValueError:
                    print("\nCommand not valid. Try again!")
                    time.sleep(1)

    money_needed_water = how_much_water * 1
    print(f"\nWe charge for water in order to cover the costs of keeping it clean.\nYou will need {money_needed_water} coins to get that much water!")
    time.sleep(1)

    # The part asks the player if they want to pump water or go back.
    # If the player tries to pump water, it will be checked if they have equal or more the price charged for the amount they chose.
        # If they do have the money, they will obtain the water and the money will be reduced accordingly.
        # If they don't have the money, a message will appear informing them and giving instruction on what to do.
    # If they choose to go back, they will be sent back to the local trades menu.

    # If the player chooses an invalid option, the program displays an error and asks again for a command.

    while True:

        while True:
            try:
                pump_water = int(input("\n1 - Start pumping\n2 - Go back\n\n"))
                time.sleep(1)
                break
            except ValueError:
                print("\nCommand not valid. Try again!")
                time.sleep(1)

        if pump_water == 1 and items["money"] >= money_needed_water:
            items["money"] = items["money"] - money_needed_water
            items["water"] = how_much_water
            save_game(items)
            print(f"\nYour money: - {money_needed_water} 🪙")
            time.sleep(1)
            print("\nPumping water:\n")
            time.sleep(1)
            for i in range(how_much_water):
                print("💧" * (i + 1))
                time.sleep(1)
            print("\nYou now have now " + str(items["water"]) + " litres of water!")
            time.sleep(1)
            break
        elif pump_water == 1 and items["money"] < money_needed_water:
            print("\nYou don't have enough money! Go trade-in some item in the trade-in store to get more coins!")
            time.sleep(1)
        elif pump_water == 2:
            return
        else:
            print_command_not_found()