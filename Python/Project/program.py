player_name = input ("\nEnter your name: ")
player_age = int(input ("Enter your age: "))

print(f"\nThe name of the player is: {player_name}")
print(f"The age of the player is: {player_age}")

# Backpack functions

items = []

def print_backpack ():
    print(f"\nThese are all the items in your backpack: {items}")

def add_backpack ():
    item = input ("Add an item to your backpack: ")
    items.append(item)

def remove_backpack ():
    item = input ("Remove an item from your backpack: ")
    items.remove(item)

def choose_action_backpack ():
    action = input("Type 'add' or 'remove': ")
    if action == "add":
        add_backpack ()
    elif action == "remove":
        remove_backpack ()
    else:
        print("Error! Start over.")

# Energy functions

energy = 0

def print_energy ():
    print(f"\nThis is your energy: {energy}")

def choose_action_energy ():
    action = input("Type 'sleep' or 'exit': ")
    if action == "sleep":
        sleep()
        print_energy ()
    elif action == "exit":
        print("\nExiting energy tab.")

def sleep ():
    global energy
    if energy < 100:
        while energy < 100:
            energy = energy + 20
            print(f"Increasing +20 energy: {energy}")
    else:
        print("You have enough energy.")

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


# Goal functions:

def goal():
    print("\nYou now have everything needed! Let's go home!")
    print(3 * "\nLoading...\n")
    print("Congratulations! You got home!")

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

# Classes

# Class characters

class Character:
    def __init__(self, name, items, money, energy):
        self.name = name
        self.items = items
        self.money = money
        self.energy = energy

character1 = Character("Cris", 10, 10, 10)
character2 = Character("Toti", 5, 5, 5)
character3 = Character("Bal", 2, 2, 2)

# Main program

if player_age < 12:
    print ("\nYou are a minor!")
else:
    print (f"\nWelcome, {player_name}!")
    print (f"\nChoose your character:")
    print (f"\nPlease note this cannot be changed later on!")
    choose_character = int(input(f"\n 1. {character1.name} with {character1.items} in bag, {character1.money} euros and {character1.energy} of energy. \n 2. {character2.name} with {character2.items} in bag, {character2.money} euros and {character2.energy} of energy. \n 3. {character3.name} with {character3.items} in bag, {character3.money} euros and {character3.energy} of energy.\n\n"))
    while choose_character != 1 or 2 or 3:
        if choose_character == 1:
            print(f"\nYou chose {character1.name}!")
            items = {"seeds":character1.items, "money":character1.money, "energy":character1.energy, "wood":10, "water":10, "jacket":1}
            break
        elif choose_character == 2:
            print(f"\nYou chose {character2.name}!")
            items = {"seeds":character2.items, "money":character2.money, "energy":character2.energy, "wood":5, "water":0, "jacket":0}
            break
        elif choose_character == 3:
            print(f"\nYou chose {character3.name}!")
            items = {"seeds":character3.items, "money":character3.money, "energy":character3.energy, "wood":10, "water":0, "jacket":0}
            break
        else:
            print("\nError! Choose one of the options.")
            choose_character = int(input(f"\n 1. {character1.name} with {character1.items} in bag, {character1.money} euros and {character1.energy} of energy. \n 2. {character2.name} with {character2.items} in bag, {character2.money} euros and {character2.energy} of energy. \n 3. {character3.name} with {character3.items} in bag, {character3.money} euros and {character3.energy} of energy.\n\n"))

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
        # Open "panel" to show what is in the characters bag and also its energy.
        print("\nYour panel info:")
        print("Print backpack")
        print("Print energy")
        print("Print money")
    elif command == 3:
        # Open rooms that will help to get what is needed to get the requirements.
        print("\nRooms:")
        print("Room 1 - Wood")
        print("Room 2 - Second hand store")
        print("Room 3 - Well")
        print("Room 4 - Trade-in store")
        print("Room 5 - Bedroom (to sleep)")
    else:
        print("Command not found.")

    print ("\nMain menu: ")
    command = int(input("Choose a command: \n1 - Ways to get to the goal \n2 - Panel info \n3 - Rooms \n4 - Lopeta\n\n"))