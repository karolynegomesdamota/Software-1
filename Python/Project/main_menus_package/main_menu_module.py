# Import
import time

# This function serves to simply display the main menu options and to require the player to choose an option.
# The whole logic behind it is in the main code.

def main_menu():
    print ("\nMain menu: ")
    command = int(input("\n1 - Paths to Molitorreno \n2 - Bag \n3 - Local Trades \n4 - Exit\n\n"))
    time.sleep(1)
    return command