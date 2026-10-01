from Menus import main_menu, room_menu, way_home_menu
from Rooms import second_hand, cut_wood, trade_in_, get_water
from Prints import print_command_not_found, print_panel, print_story
from Paths import lore_boat, check_wood,  lore_desert, check_water, lore_freezing_mountain, check_jacket
import time
from Characters import choose_character

player_name = input ("\nEnter your name: ")

while True:
    try:
        player_age = int(input ("Enter your age: "))
        break
    except ValueError:
        print("Age not valid. Try again!")

if player_age < 12:
    print("\nYou are under 12! You cannot play this game!")
    time.sleep(1)
    print("\nExisting game...")
    time.sleep(1)
    print("\nExit completed!")
else:
    print (f"\nWelcome, {player_name}!")
    time.sleep(2)

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
                    check_wood(items)
                    break #This break causes the go back menu inside check wood to jump to the main menu. But the problem now is for some reason after "You don't have enough trees it is printing the lore again"
                elif way_home == 2:
                    lore_desert()
                    check_water(items)
                    break
                elif way_home == 3:
                    lore_freezing_mountain()
                    check_jacket(items)
                    break
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

        print("Is it here?")
        command = main_menu()

    print("\nExisting game...")
    time.sleep(1)
    print("\nExit completed!")