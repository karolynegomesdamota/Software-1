from Menus import room_menu

def get_water(items): #Parameters passed here because if not it had no way to access the data once I moved this out of the program
    how_much_water = int(input("\nHow many litres of water do you need? "))
    money_needed = how_much_water * 1
    print(f"\nYou will need {money_needed} coins to get that much water!")
    pump_water = int(input("\nPress 1 to start pumping water: \n1 - Start pumping\n2 - Go back\n\n"))
    if pump_water == 1 and items["money"] >= money_needed:
        items["money"] = items["money"] - money_needed
        items["water"] = how_much_water
        print("\nYou now have " + str(items["water"]) + " litres of water and " + str(items["money"]) + " coins.")
    elif pump_water == 1 and items["money"] < money_needed:
        print("\nYou don't have enough money! Go trade-in some item in the trade-in store to get more coins!")
    elif pump_water == 2:
        room = room_menu()
        return room
    #else not needed due to main program already showing error