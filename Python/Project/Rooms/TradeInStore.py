import time
from Prints import print_command_not_found

def trade_in_(items): #Parameters passed here because if not it had no way to access the data once I moved this out of the program
    #print_panel () Comment for a moment to test if the package works
    print("\nPlease note that the full amount of units of what you have will be exchanged!")
    time.sleep(1)
    print("\nToday's exchange rate: 1 seed = 1 coin.")
    time.sleep(1)

    while True:

        what_trade_in = int(input("\nChoose what you want to trade-in: \n1 - Money into seeds \n2 - Seeds into money\n3 - Go back\n\n"))
        time.sleep(1)

        if what_trade_in == 1:
            if items["money"] >= 1:
                items["seeds"] = items["seeds"] + items["money"]
                items["money"] = 0
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