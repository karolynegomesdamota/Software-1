from Menus import room_menu

items = {}

def trade_in_():
    #print_panel () Comment for a moment to test if the package works
    print("\nPlease note that the full amount of units of what you have will be exchanged!")
    print("\nToday's exchange rate: 1 seed = 1 coin.")
    what_trade_in = int(input("\nChoose what you want to trade-in: \n1 - Money into seeds \n2 - Seeds into money\n3 - Go back\n\n"))
    if what_trade_in == 1:
        items["seeds"] = 10
        items["money"] = 0
        print("\nYou now have " + str(items["seeds"]) + " seeds and " + str(items["money"]) + " coins.")

        # TODO: Implement some logic for when the player selects some trade for something they have 0.

    elif what_trade_in == 2:
        items["seeds"] = 0
        items["money"] = 10
        print("\nYou now have " + str(items["seeds"]) + " seeds and " + str(items["money"]) + " coins.")

        # TODO: Implement some logic for when the player selects some trade for something they have 0.

    elif what_trade_in == 3:
        room = room_menu()
        return room
    #else not needed due to main program already showing error