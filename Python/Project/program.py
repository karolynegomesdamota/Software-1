player_name = input ("Enter your name: ")
player_age = int(input ("Enter your age: "))

print(f"The name of the player is: {player_name}")
print(f"The age of the player is: {player_age}")

if player_age < 12:
    print ("You are a minor!")
else:
    print (f"Welcome, {player_name}!")
    print ("Main menu: ")
    command = input ("Write a command or type 'lopeta' to exit. \n")
    while command != "lopeta":
        if command == "dance":
            print("💃")
        elif command == "eat":
            print("😋")
        elif command == "run":
            print("🏃")
        else:
            print("Command not found.")

        print ("Main menu: ")
        command = input ("Write a command or type 'lopeta' to exit. \n")