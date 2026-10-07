from Prints import print_command_not_found
import time


def second_hand_lore():
    money_needed_jacket = 10
    print("\nSeller: Right now the only item left we have is a jacket!")
    time.sleep(1)
    print(f"\nSeller: You will need {money_needed_jacket} coins to get this jacket!")
    time.sleep(1)
    return money_needed_jacket

def second_hand(items, money_needed_jacket): #Parameters passed here because if not it had no way to access the data once I moved this out of the program

    while True:

        ask_buy_jacket = int(input(f"\nSeller: Would you like to buy it?\n\n1 - Yes \n2 - No\n\n"))

        if ask_buy_jacket == 1 and items["money"] >= money_needed_jacket:
            items["money"] = items["money"] - money_needed_jacket
            items["jacket"] = 1
            print("\nYou now have a jacket!")
            time.sleep(1)
            break
        elif ask_buy_jacket == 1 and items["money"] < money_needed_jacket:
            print("\nYou don't have enough money! Go trade-in some item in the trade-in store to get more coins!")
            time.sleep(1)
        elif ask_buy_jacket == 2:
            print("\nSeller: Go away then!")
            time.sleep(1)
            print("\nYou have been kicked out of the store!")
            time.sleep(1)
            return
        else:
            print_command_not_found()
