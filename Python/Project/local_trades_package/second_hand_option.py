# Import
import time
# From
from prints_package import print_command_not_found
from saved_data_package import save_game

def second_hand(items): # Items are passed (coming from main code) in order to evaluate the conditions.

    # This next block of code serves simply to display text and to set the pricing for the item:

    money_needed_jacket = 10
    print("\nSeller: Right now the only item left we have is a jacket!")
    time.sleep(1)
    print(f"\nSeller: You will need {money_needed_jacket} coins to get this jacket!")
    time.sleep(1)

    # The next part asks the player whether they want to buy the item or not and perform calculations to evaluate if they can buy it.
    # If the player chooses to buy the item, it will be checked if they have equal or more the price of the item.
        # If they do have the money, they will obtain the item and the money will be reduced accordingly.
        # If they don't have the money, a message will appear informing them and giving instruction on what to do.
    # If they choose not to buy the item, they will be kicked out of the store and sent back to the local trades menu.

    # If the player chooses an invalid option, the program displays an error and asks again for a command.

    while True:

        while True:
            try:
                ask_buy_jacket = int(input(f"\nSeller: Would you like to buy it?\n\n1 - Yes \n2 - No\n\n"))
                break
            except ValueError:
                print("\nCommand not valid. Try again!")
                time.sleep(1)

        if ask_buy_jacket == 1 and items["money"] >= money_needed_jacket:
            items["money"] = items["money"] - money_needed_jacket
            items["jacket"] = 1
            save_game(items)
            print("\nYou now have a jacket! 🧥")
            time.sleep(1)
            break
        elif ask_buy_jacket == 1 and items["money"] < money_needed_jacket:
            print("\nYou don't have enough money! Go trade-in some item in the trade-in store to get more coins!")
            time.sleep(1)
            break
        elif ask_buy_jacket == 2:
            print("\nSeller: Go away then!")
            time.sleep(1)
            print("\nYou have been kicked out of the store!")
            time.sleep(1)
            return
        else:
            print_command_not_found()
