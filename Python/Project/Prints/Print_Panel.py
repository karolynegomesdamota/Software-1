import time

def print_panel (items):
    print(f"\nThis is everything you have in your bag: \n")
    print("Seeds: " + str(items["seeds"]))
    print("Money: " + str(items["money"]))
    print("Trees: " + str(items["trees"]))
    print("Water: " + str(items["water"]))
    print("Jackets: " + str(items["jacket"]))
    print("Boats: " + str(items["boat"]))
    time.sleep(1)