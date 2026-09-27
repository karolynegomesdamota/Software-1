from Menus import main_menu, room_menu, way_home_menu
from Rooms import second_hand, cut_wood, trade_in_, get_water
from Prints import print_command_not_found, print_panel, print_story
from Paths import lore_boat, check_wood,  lore_desert, check_water, lore_freezing_mountain, check_jacket
import time
from Characters import choose_character

player_name = input ("\nEnter your name: ")
player_age = int(input ("Enter your age: "))

#print(f"\nThe name of the player is: {player_name}")
#print(f"The age of the player is: {player_age}")

if player_age < 12:
    print ("\nYou are a minor!")
else:
    print (f"\nWelcome, {player_name}!")

    items, chosen_character = choose_character()

    print_story(chosen_character)
    time.sleep(2)

    command = main_menu()

    while command != 4:
        if command == 1:
            way_home = way_home_menu()
            while way_home != 4:
                if way_home == 1:
                    lore_boat()
                    way_home = check_wood(items) # This to update the way home after it is asked in the check wood function.
                elif way_home == 2:
                    lore_desert()
                    way_home = check_water(items) # This to update the way home after it is asked in the check wood function.
                elif way_home == 3:
                    lore_freezing_mountain()
                    way_home = check_jacket(items) # This to update the way home after it is asked in the check wood function.
                elif way_home == 4:
                    main_menu()
                else:
                    print_command_not_found()
                    way_home = way_home_menu()
        elif command == 2:
            print_panel (items)

        elif command == 3:
            room = room_menu()
            while room != 5:
                if room == 1:
                    room = cut_wood(items) # TODO: Rename function and variable within it to make more sense and to be more clear.
                elif room == 2:
                    room = second_hand(items) # TODO: Rename function and variable within it to make more sense and to be more clear.
                elif room == 3:
                    room = get_water(items) # TODO: Rename function and variable within it to make more sense and to be more clear.
                elif room == 4:
                    room = trade_in_(items) # TODO: Rename function and variable within it to make more sense and to be more clear.
                else:
                    print_command_not_found()
                    room = room_menu()
        else:
            print_command_not_found()

        command = main_menu()