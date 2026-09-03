player_name = input ("Enter your name: ")
player_age = int(input ("Enter your age: "))

print(f"The name of the player is: {player_name}")
print(f"The age of the player is: {player_age}")

# Backpack functions

items = []

def print_backpack ():
    print(f"These are all the items in your backpack: {items}")

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
    print(f"This is your energy: {energy}")

def choose_action_energy ():
    action = input("Type 'sleep' or 'exit': ")
    if action == "sleep":
        sleep()
        print_energy ()
    elif action == "exit":
        print("Exiting energy tab.")

def sleep ():
    global energy
    if energy < 100:
        while energy < 100:
            energy = energy + 20
            print(f"Increasing +20 energy: {energy}")
    else:
        print("You have enough energy.")

# Main program

if player_age < 12:
    print ("You are a minor!")
else:
    print (f"Welcome, {player_name}!")
    print ("Main menu: ")
    command = input ("Choose a command: \n1 - backpack \n2 - energy \n3 - lopeta \n")
    while command != "3":
        if command == "1":
            print_backpack ()
            choose_action_backpack ()
            print_backpack ()
        elif command == "2":
            print_energy ()
            choose_action_energy ()
        else:
            print("Command not found.")

        print ("Main menu: ")
        command = input ("Choose a command: \n1 - backpack \n2 - energy \n3 - lopeta \n")