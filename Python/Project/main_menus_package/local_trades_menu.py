import time
from local_trades_package import second_hand, the_woods, trade_in_, get_water, second_hand_lore, get_water_lore, the_woods_lore
from prints_package import print_command_not_found

def local_trades(items):

    while True:

        while True:
            try:
                room = int(input("\nLocal Trades in Molitorreno: \n\n1 - The Woods \n2 - Second hand store \n3 - The Well \n4 - Trade-in store \n5 - Go back\n\n"))
                break
            except ValueError:
                print("\nCommand not valid. Try again!")
                time.sleep(1)

        time.sleep(1)

        if room == 1:
            how_many_trees, seeds_needed = the_woods_lore()
            the_woods(items, how_many_trees, seeds_needed) # TODO: Rename function and variable within it to make more sense and to be more clear.
        elif room == 2:
            money_needed_jacket = second_hand_lore()
            second_hand(items, money_needed_jacket) # TODO: Rename function and variable within it to make more sense and to be more clear.
        elif room == 3:
            how_much_water, money_needed = get_water_lore()
            get_water(items, how_much_water, money_needed) # TODO: Rename function and variable within it to make more sense and to be more clear.
        elif room == 4:
            trade_in_(items) # TODO: Rename function and variable within it to make more sense and to be more clear.
        elif room == 5:
            return
        else:
            print_command_not_found()