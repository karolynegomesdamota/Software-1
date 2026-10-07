import time
from prints_package import print_command_not_found
from saved_data_package import save_game

def the_woods_lore():

    while True:
                try:
                    how_many_trees = int(input("\nHow many trees do you need? "))
                    break
                except ValueError:
                    print("\nCommand not valid. Try again!")
                    time.sleep(1)

    seeds_needed = how_many_trees * 2
    print(f"\nYou will need to plant {seeds_needed} seeds if you want to cut that many trees!")
    time.sleep(1)
    return how_many_trees, seeds_needed

def the_woods(items, how_many_trees, seeds_needed): #Parameters passed here because if not it had no way to access the data once I moved this out of the program

    while True:

        while True:
            try:
                cut_tree = int(input("\n1 - Start cutting \n2 - Go back\n\n"))
                break
            except ValueError:
                print("\nCommand not valid. Try again!")
                time.sleep(1)

        if cut_tree == 1 and items["seeds"] >= seeds_needed:
            items["seeds"] = items["seeds"] - seeds_needed
            items["trees"] = items["trees"] + how_many_trees
            save_game(items)
            print("\nCutting trees:\n")
            time.sleep(1)
            for i in range(how_many_trees):
                print("🪵" * (i + 1))
                time.sleep(1)
            print("\nYou now have " + str(items["trees"]) + " trees!")
            time.sleep(1)
            break

        elif cut_tree == 1 and items["seeds"] < seeds_needed:
            print("\nYou don't have enough seeds! Go trade money to get more!")
            time.sleep(1)
        elif cut_tree == 2:
            return
        else:
            print_command_not_found()