from Menus import room_menu

def second_hand(items): #Parameters passed here because if not it had no way to access the data once I moved this out of the program
    money_needed_jacket = 10
    print("\nSeller: Right now the only item left we have is a jacket!")
    print(f"\nSeller: You will need {money_needed_jacket} coins to get this jacket!")
    ask_buy_jacket = int(input("\nSeller: Would you like to buy it? \n\n1 - Yes. \n2 - No.\n\n"))
    if ask_buy_jacket == 1 and items["money"] >= money_needed_jacket:
        items["money"] = items["money"] - money_needed_jacket
        items["jacket"] = 1
        print("\nYou now have " + str(items["money"]) + " coins and " + str(items["jacket"]) + " jacket.")
    elif ask_buy_jacket == 1 and items["money"] < money_needed_jacket:
        print("\nYou don't have enough money! Go trade-in some item in the trade-in store to get more coins!")
    elif ask_buy_jacket == 2:
        print("\nSeller: Go away then!\n\nYou have been kicked out of the store!")
        room = room_menu()
        return room
    #else not needed due to main program already showing error
