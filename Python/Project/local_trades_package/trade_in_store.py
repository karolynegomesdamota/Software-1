import time
from prints_package import print_command_not_found, print_panel
from saved_data_package import save_game

def trade_in_(items): #Parameters passed here because if not it had no way to access the data once I moved this out of the program
    print("\nYour bag:")
    print_panel(items)
    print("\nPlease note that the full amount of units of what you have in your bag will be exchanged!")
    time.sleep(1)
    print("\nToday's exchange rate: 1 seed = 1 coin.")
    time.sleep(1)

    while True:

        while True:
            try:
                what_trade_in = int(input("\nChoose what you want to trade-in: \n1 - Money into seeds \n2 - Seeds into money\n3 - Go back\n\n"))
                break
            except ValueError:
                print("\nCommand not valid. Try again!")
                time.sleep(1)

        if what_trade_in == 1:
            if items["money"] >= 1:
                items["seeds"] = items["seeds"] + items["money"]
                items["money"] = 0
                save_game(items)
                print("\nTrading:\n")
                time.sleep(1)
                for i in range(items["seeds"]):
                    print("🪙" * (items["seeds"] - i))
                    print("🌱" * (i + 1))
                    time.sleep(1)
                time.sleep(1)
                print("\nYou now have handed over all your money and have a total of " + str(items["seeds"]) + " seeds.")
                time.sleep(1)
                break
            else:
                print("\nYou don't any money to trade!")
                time.sleep(1)

        elif what_trade_in == 2:
            if items["seeds"] >= 1:
                items["money"] = items["money"] + items["seeds"]
                items["seeds"] = 0
                save_game(items)
                print("\nTrading:\n")
                time.sleep(1)
                for i in range(items["money"]):
                    print("🌱" * (items["money"] - i))
                    print("🪙" * (i + 1))
                    time.sleep(1)
                print("\nYou now have handed over all your seeds and have a total of " + str(items["money"]) + " coins.")
                time.sleep(1)
                break
            else:
                print("\nYou don't any seeds to trade!")
                time.sleep(1)

        elif what_trade_in == 3:
            return

        else:
                print_command_not_found()