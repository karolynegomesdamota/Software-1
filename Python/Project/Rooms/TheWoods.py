import time
from Menus import room_menu
from Prints import print_command_not_found

def cut_wood(items): #Parameters passed here because if not it had no way to access the data once I moved this out of the program
    how_many_trees = int(input("\nHow many trees do you need? "))
    time.sleep(1)
    seeds_needed = how_many_trees * 2
    print(f"\nYou will need to plant {seeds_needed} seeds if you want to cut that many trees!")
    time.sleep(1)
    cut_tree = int(input("\n1 - Start cutting \n2 - Go back\n\n"))
    time.sleep(1)

    if cut_tree == 1 and items["seeds"] >= seeds_needed:
        items["seeds"] = items["seeds"] - seeds_needed
        items["trees"] = how_many_trees
        print("\nCutting trees:\n")
        for i in range(how_many_trees):
            print(f"Tree number {i+1} cut!")
            time.sleep(1)
        print("\nYou now have " + str(items["seeds"]) + " seeds and " + str(items["trees"]) + " trees.")
    elif cut_tree == 1 and items["seeds"] < seeds_needed:
        print("\nYou don't have enough seeds! Go trade money to get more!")
    elif cut_tree == 2:
        room = room_menu()
        return room
    else:
        print_command_not_found()
        cut_wood(items)
