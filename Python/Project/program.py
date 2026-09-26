from Menus import main_menu, room_menu, way_home_menu
from Rooms import second_hand, cut_wood, trade_in_, get_water
from Classes import Character

player_name = input ("\nEnter your name: ")
player_age = int(input ("Enter your age: "))

print(f"\nThe name of the player is: {player_name}")
print(f"The age of the player is: {player_age}")

# Panel functions

def print_panel ():
    print(f"\nThis is everything you have: ")
    print("Seeds: " + str(items["seeds"]))
    print("Money: " + str(items["money"]))
    print("Trees: " + str(items["trees"]))
    print("Water: " + str(items["water"]))
    print("Jacket: " + str(items["jacket"]))

# Lake functions:

# Boat lore:

def lore_boat():
    print(f"\nIf you choose to go this way, you will need a boat to get through the lake.")
    print(f"In order for you to build the boat, you will need to get wood. You will need 5 trees to build it.")
    print(f"You can get trees from The Wood. For each tree to cut, you will need to plant 2 seeds.")
    print(f"Check your bag to see how many seeds you have. If you do not have enough, you can trade-in some for some money in the trade-in store.")

    print(f"Once you have enough trees, come back here to build your boat.")

# Check wood

def check_wood():

    boat = int(input("\nPress 1 to build the boat: \n1 - Build boat.\n2 - Go back.\n\n"))
    if boat == 1:
        if items["trees"] >= 5:
            build_boat()
            goal()
        else:
            print("\nYou don't have enough trees! Go get some in The Wood!")
    elif boat == 2:
        way_home = way_home_menu() # This to make the way home menu to show and ask for a new option
        return way_home # This to pass the new option inside the already first chosen option.

    else:
        print_command_not_found()

# Build boat

def build_boat():
    if items["trees"] == 5:
        items["trees"] = 0
        items["boat"] = 1
        print (f"\nYou now have " + str(items["trees"]) + " trees and " + str(items["boat"]) + " boat!")

# Desert functions:

# Desert lore:

def lore_desert():
    print(f"\nIf you choose to go this way, you will need a water to get through the desert.")
    print(f"In order for you to get water, you will need to pump it from the well. You will need 10 liters of water to cross the desert and the farmer who owns the well will charge you 1 coin per liter.")
    print(f"Check your bag to see how much money you have. If you do not have enough, you can trade some items in the trade-in store.")

    print(f"Once you have enough water, come back here to start your journey.")

# Check water

def check_water():

    start_desert = int(input("\nPress 1 to start your journey: \n1 - Go through the desert.\n2 - Go back\n\n"))
    if start_desert == 1:
        if items["water"] >= 10:
            goal()
        else:
            print("\nYou don't have enough water! Go pump some from the well!")
    elif start_desert == 2:
        way_home = way_home_menu() # This to make the way home menu to show and ask for a new option
        return way_home # This to pass the new option inside the already first chosen option.
    else:
        print_command_not_found()

# Freezing mountain functions:

# Freezing mountain lore:

def lore_freezing_mountain():
    print(f"\nIf you choose to go this way, you will need a jacket to get through the freezing mountains.")
    print(f"In order for you to get a jacket, you will need to buy it from the second hand store. It costs 10 coins.")
    print(f"Check your panel to see how much money you have. If you do not have enough, you can trade some items in the trade-in store.")

    print(f"Once you have a jacket, come back here to start your journey.")

# Check jacket

def check_jacket():

    start_mountain = int(input("\nPress 1 to start your journey: \n1 - Go through the mountain. \n2 - Go back\n\n"))
    if start_mountain == 1:
        if items["jacket"] >= 1:
            goal()
        else:
            print("\nYou don't have a jacket! Go buy one!")
    elif start_mountain == 2:
        way_home = way_home_menu() # This to make the way home menu to show and ask for a new option
        return way_home # This to pass the new option inside the already first chosen option.
    else:
        print_command_not_found()

# Goal functions:

def goal():
    print("\nYou now have everything needed! Let's go home!")
    print(3 * "\nLoading...\n")
    print("Congratulations! You got home!")

# Print command not found

def print_command_not_found():
    print("\nCommand not found. Try again!")

# Main program

character1 = Character("Cris", 10, 0)
character2 = Character("Toti", 0, 10)
character3 = Character("Bal", 5, 5)

if player_age < 12:
    print ("\nYou are a minor!")
else:
    print (f"\nWelcome, {player_name}!")
    print (f"\nChoose your character:")
    print (f"\nPlease note this cannot be changed later on!")
    choose_character = int(input(f"\n 1 - {character1.name} with {character1.seeds} seeds and {character1.money} coins. \n 2 - {character2.name} with {character2.seeds} seeds and {character2.money} coins. \n 3 - {character3.name} with {character3.seeds} seeds and {character3.money} coins.\n\n"))
    while choose_character != 1 or 2 or 3:
        if choose_character == 1:
            print(f"\nYou chose {character1.name}!")
            items = {"seeds":character1.seeds, "money":character1.money, "trees":0, "water":0, "jacket":0}
            break
        elif choose_character == 2:
            print(f"\nYou chose {character2.name}!")
            items = {"seeds":character2.seeds, "money":character2.money, "trees":0, "water":0, "jacket":0}
            break
        elif choose_character == 3:
            print(f"\nYou chose {character3.name}!")
            items = {"seeds":character3.seeds, "money":character3.money, "trees":0, "water":0, "jacket":0}
            break
        else:
            print_command_not_found()
            choose_character = int(input(f"\n 1 - {character1.name} with {character1.seeds} seeds and {character1.money} coins. \n 2 - {character2.name} with {character2.seeds} seeds and {character2.money} coins. \n 3 - {character3.name} with {character3.seeds} seeds and {character3.money} coins.\n\n"))


print("\nHere some intro story...")

command = main_menu()

while command != 4:
    if command == 1:
        way_home = way_home_menu()
        while way_home != 4:
            if way_home == 1:
                lore_boat()
                way_home = check_wood() # This to update the way home after it is asked in the check wood function.
            elif way_home == 2:
                lore_desert()
                way_home = check_water() # This to update the way home after it is asked in the check wood function.
            elif way_home == 3:
                lore_freezing_mountain()
                way_home = check_jacket() # This to update the way home after it is asked in the check wood function.
            elif way_home == 4:
                main_menu()
            else:
                print_command_not_found()
                way_home = way_home_menu()
    elif command == 2:
        print_panel ()
        print("\nGoing back to the main menu...")

    elif command == 3:
        room = room_menu()
        while room != 5:
            if room == 1:
                room = cut_wood(items) # TODO: Rename function and variable within it to make more sense and to be more clear.
            elif room == 2:
                room = second_hand(items) # TODO: Rename function and variable within it to make more sense and to be more clear.
            elif room == 3:
                room = get_water(items) # TODO: Rename function and variable within it to make more sense and to be more clear.
            elif room == 4:
                room = trade_in_(items) # TODO: Rename function and variable within it to make more sense and to be more clear.
            else:
                print_command_not_found()
                room = room_menu()
    else:
            print_command_not_found()

    command = main_menu()