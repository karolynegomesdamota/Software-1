import time
from local_trades_package import second_hand, the_woods, trade_in_store, the_well
from prints_package import print_command_not_found

# This function serves to simply display the local trades menu options and to require the player to choose one.
# If the player chooses an invalid option, the program displays an error and asks again for a command.

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
            the_woods(items)
        elif room == 2:
            second_hand(items)
        elif room == 3:
            the_well(items)
        elif room == 4:
            trade_in_store(items)
        elif room == 5:
            return
        else:
            print_command_not_found()