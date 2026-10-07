import time
from prints_package import print_command_not_found
from saved_data_package import save_game

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
    return how_much_water, money_needed

def get_water(items, how_much_water, money_needed): #Parameters passed here because if not it had no way to access the data once I moved this out of the program

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