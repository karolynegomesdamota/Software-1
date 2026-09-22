player_name = input ("\nEnter your name: ")
player_age = int(input ("Enter your age: "))

print(f"\nThe name of the player is: {player_name}")
print(f"The age of the player is: {player_age}")

# Panel functions

def print_panel ():
    print(f"\nThis is the panel: ")
    print("Seeds: " + str(items["seeds"]))
    print("Money: " + str(items["money"]))
    print("Wood: " + str(items["wood"]))
    print("Water: " + str(items["water"]))
    print("Jacket: " + str(items["jacket"]))

# Lake functions:

# Boat lore:

def lore_boat():
    print(f"\nIf you choose to go this way, you will need a boat to get through the lake.")
    print(f"In order for you to build the boat, you will need to get wood. You will need 10 woods to build it.")
    print(f"You can get wood from the wood, but for each tree to cut, you will need to plant 2 seeds.")
    print(f"Check your bag to see how many seeds you have. If you do not have enough, you can buy more seed from the kiosk.")

    print(f"Once you have wood enough, come back here to build your boat.")

# Check wood

def check_wood():

    boat = int(input("\nPress 1 to build the boat: \n1 - Build boat.\n\n"))
    if boat == 1:
        if items["wood"] >= 10:
            build_boat()
            goal()
        else:
            print("You don't have enough wood! Go get some in the woods!")
    else:
        print("Error!")

# Build boat

def build_boat():
    if items["wood"] == 10:
        items["wood"] = 0
        items["boat"] = 1
        print (f"\nYou now have " + str(items["wood"]) + " of wood and " + str(items["boat"]) + " boat!")

# Desert functions:

# Boat lore:

def lore_desert():
    print(f"\nIf you choose to go this way, you will need a water to get through the desert.")
    print(f"In order for you to get water, you will need to pump it from the well. You will need 10 water to cross the desert.")
    print(f"Check your bag to see how much water you have. If you do not have enough, you can buy more water from the kiosk.")

    print(f"Once you have water enough, come back here to start your journey.")

# Check water

def check_water():

    start_desert = int(input("\nPress 1 to start your journey: \n1 - Go through the desert.\n\n"))
    if start_desert == 1:
        if items["water"] >= 10:
            goal()
        else:
            print("You don't have enough water! Go pump some from the well!")
    else:
        print("Error!")

# Freezing mountain functions:

# Freezing mountain lore:

def lore_freezing_mountain():
    print(f"\nIf you choose to go this way, you will need a jacket to get through the freezing mountains.")
    print(f"In order for you to get the jacket, you will need to get the jacket from the second hand store. You will need 10 euros to buy it.")
    print(f"You can get money by trading items you have, but for each seed you have, you will get 1 euro.")
    print(f"Check your panel to see how much money you have. If you do not have enough, you can trade some items in the trade-in store.")

    print(f"Once you have a jacket, come back here to start your journey.")

def check_jacket():

    start_mountain = int(input("\nPress 1 to start your journey: \n1 - Go through the mountain.\n\n"))
    if start_mountain == 1:
        if items["jacket"] >= 1:
            goal()
        else:
            print("You don't have a jacket! Go buy one!")
    else:
        print("Error!")

# Goal functions:

def goal():
    print("\nYou now have everything needed! Let's go home!")
    print(3 * "\nLoading...\n")
    print("Congratulations! You got home!")


# Room functions

# Room 1 - Wood

def cut_wood():
    how_many_trees = int(input("\nHow many trees do you need? "))
    seeds_needed = how_many_trees * 2
    print(f"\nYou will need {seeds_needed} seeds to get that many trees!")
    cut_tree = int(input("\nPress 1 to start cutting trees: \n1 - Start cutting.\n\n"))
    if cut_tree == 1 and items["seeds"] >= seeds_needed:
        items["seeds"] = items["seeds"] - seeds_needed
        items["tree"] = how_many_trees
        print("You now have " + str(items["seeds"]) + " seeds and " + str(items["tree"]) + " trees.")
    elif cut_tree == 1 and items["seeds"] < seeds_needed:
        print("You don't have enough seeds! Go get more in the kiosk!")
    else:
        print("Error!")

# Room 2 - Second hand

def second_hand():
    print("Right now the only item left we have is a jacket!")
    money_needed_jacket = 10
    print(f"\nYou will need {money_needed_jacket} money to get this jacket!")
    ask_buy_jacket = int(input("\nWould you like to buy it? \n1 - Yes. \n1 - No.\n\n"))
    if ask_buy_jacket == 1 and items["money"] >= money_needed_jacket:
        items["money"] = items["money"] - money_needed_jacket
        items["jacket"] = 1
        print("You now have " + str(items["money"]) + " money and " + str(items["jacket"]) + " jacket.")
    elif ask_buy_jacket == 1 and items["money"] < money_needed_jacket:
        print("You don't have enough money! Go trade-in something in the trade-in store!")
    else:
        print("Error!")

# Room 3 - Well

def get_water():
    how_much_water = int(input("\nHow much water do you need? "))
    money_needed = how_much_water * 1
    print(f"\nYou will need {money_needed} euros to get that much water!")
    pump_water = int(input("\nPress 1 to start pumping water: \n1 - Start pumping.\n\n"))
    if pump_water == 1 and items["money"] >= money_needed:
        items["money"] = items["money"] - money_needed
        items["water"] = how_much_water
        print("You now have " + str(items["water"]) + " water and " + str(items["money"]) + " money.")
    elif pump_water == 1 and items["money"] < money_needed:
        print("You don't have enough money! Go trade-in something in the trade-in store!")
    else:
        print("Error!")

# Room 4 - Trade-in

def trade_in_():
    print_panel ()
    print("\nPlease note all your items will be transferred to the new item!")
    what_trade_in = int(input("\nChoose what you want to trade-in: \n1 - Money into seeds \n2 - Seeds into money \n"))
    if what_trade_in == 1:
        items["seeds"] = 0
        items["money"] = 10

    elif what_trade_in == 2:
        items["seeds"] = 0
        items["money"] = 10
    else:
        print("Error!")
    print_panel ()

# Classes

# Class characters

class Character:
    def __init__(self, name, items, money):
        self.name = name
        self.items = items
        self.money = money

character1 = Character("Cris", 10, 0)
character2 = Character("Toti", 0, 10)
character3 = Character("Bal", 5, 5)



# Main program

if player_age < 12:
    print ("\nYou are a minor!")
else:
    print (f"\nWelcome, {player_name}!")
    print (f"\nChoose your character:")
    print (f"\nPlease note this cannot be changed later on!")
    choose_character = int(input(f"\n 1. {character1.name} with {character1.items} in bag, {character1.money} euros. \n 2. {character2.name} with {character2.items} in bag, {character2.money} euros. \n 3. {character3.name} with {character3.items} in bag, {character3.money} euros.\n\n"))
    while choose_character != 1 or 2 or 3:
        if choose_character == 1:
            print(f"\nYou chose {character1.name}!")
            items = {"seeds":character1.items, "money":character1.money, "wood":10, "water":10, "jacket":1}
            break
        elif choose_character == 2:
            print(f"\nYou chose {character2.name}!")
            items = {"seeds":character2.items, "money":character2.money, "wood":5, "water":0, "jacket":0}
            break
        elif choose_character == 3:
            print(f"\nYou chose {character3.name}!")
            items = {"seeds":character3.items, "money":character3.money, "wood":10, "water":0, "jacket":0}
            break
        else:
            print("\nError! Choose one of the options.")
            choose_character = int(input(f"\n 1. {character1.name} with {character1.items} in bag, {character1.money} euros. \n 2. {character2.name} with {character2.items} in bag, {character2.money} euros. \n 3. {character3.name} with {character3.items} in bag, {character3.money} euros.\n\n"))


print("\nHere some intro story...")

print ("\nMain menu: ")
command = int(input("Choose a command: \n1 - Ways to get to the goal \n2 - Panel info \n3 - Rooms \n4 - Lopeta\n\n"))
while command != 4:
    if command == 1:
        way_home = int(input("\nChoose a command: \n1 - Lake \n2 - Desert \n3 - Freezing mountain\n\n"))
        if way_home == 1:
            lore_boat()
            check_wood()
            break
        elif way_home == 2:
            lore_desert()
            check_water()
            break
        elif way_home == 3:
            lore_freezing_mountain()
            check_jacket()
            break
    elif command == 2:
        print_panel ()
    elif command == 3:
        room = int(input("\nChoose where you want to go: \n1 - Wood \n2 - Second hand store \n3 - Well \n4 - Trade-in store\n"))
        if room == 1:
            cut_wood()
            break
        elif room == 2:
            second_hand()
            break
        elif room == 3:
            get_water()
            break
        elif room == 4:
            trade_in_()
            break
        else:
            print("Command not found.")

    print ("\nMain menu: ")
    command = int(input("Choose a command: \n1 - Ways to get to the goal \n2 - Panel info \n3 - Rooms \n4 - Lopeta\n\n"))