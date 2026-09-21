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
            break
        elif choose_character == 2:
            print(f"\nYou chose {character2.name}!")
            break
        elif choose_character == 3:
            print(f"\nYou chose {character3.name}!")
            break
        else:
            print("\nError! Choose one of the options.")
            choose_character = int(input(f"\n 1. {character1.name} with {character1.items} in bag, {character1.money} euros and {character1.energy} of energy. \n 2. {character2.name} with {character2.items} in bag, {character2.money} euros and {character2.energy} of energy. \n 3. {character3.name} with {character3.items} in bag, {character3.money} euros and {character3.energy} of energy.\n\n"))

print("\nHere some intro story...")

print ("\nMain menu: ")
command = int(input("Choose a command: \n1 - Ways to get to the goal \n2 - Panel info \n3 - Rooms \n4 - Lopeta\n\n"))
while command != 4:
    if command == 1:
        # Open the 3 options to get to the goal and explain what is needed for each one.
        print("\nThese are the 3 ways to get home:")
        print("1 - Lake. You need to build boat. To build boat, you need wood.")
        print("2 - Desert. You need water. To get water, you have to pump it from the well.")
        print("3 - Freezing mountain. You need a jack. To get a jacket, you need to buy it from the second hand store.")
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