# Import
import time
# From
from prints_package import print_command_not_found
from paths_package import lore_boat, lake_menu, lore_desert, desert_menu, lore_freezing_mountain, freezing_mountain_menu

# This function serves to simply display the path menu options and to require the player to choose an option.
# If the player chooses an invalid option, the program displays an error and asks again for a command.

def path_menu(items):

    while True:

        while True:
            try:
                path = int(input("\nPaths to Molitorreno: \n\n1 - Crossing the Lake \n2 - Crossing the Desert \n3 - Crossing the Freezing Mountains \n4 - Go back\n\n"))
                break
            except ValueError:
                print("\nCommand not valid. Try again!")
                time.sleep(1)

        time.sleep(1)

        if path == 1:
            lore_boat()
            lake_menu(items)
        elif path == 2:
            lore_desert()
            desert_menu(items)
        elif path == 3:
            lore_freezing_mountain()
            freezing_mountain_menu(items)
        elif path == 4:
            return
        else:
            print_command_not_found()