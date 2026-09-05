airports = {}

options = int(input ("\nAirport Data Management \n1. Enter a new airport \n2. Fetch airport information \n3. Quit \nPlease choose an option (1-3): "))

while options != 3:
    if options == 1:
        ICAO_code_enter = input("Enter the ICAO code: ")
        name_airport_add = input("Enter the airport name: ")
        airports["ICAO"]= ICAO_code_enter
        airports["name"]= name_airport_add
        print(f"Airport {name_airport_add} with ICAO code {ICAO_code_enter} has been added.")
        options = int(input ("\nAirport Data Management \n1. Enter a new airport \n2. Fetch airport information \n3. Quit \nPlease choose an option (1-3): "))

    elif options == 2:
        ICAO_code_fetch = input("Enter the ICAO code: ")
        if airports["ICAO"] == ICAO_code_fetch:
            name_airport_fetch = airports["name"] # This was done because the print was not accepting {airports["name"]} inside of the string.
            print(f"The airport with ICAO code {ICAO_code_fetch} is {name_airport_fetch}.")
        else:
            print(f"No airport found with ICAO code {ICAO_code_fetch}.")
        options = int(input ("\nAirport Data Management \n1. Enter a new airport \n2. Fetch airport information \n3. Quit \nPlease choose an option (1-3): "))

print("Thank you for using the Airport Data Management system. Goodbye!")












"""
Note for myself:

The correct code accepted by Moodle is above, but in my opinion the following code makes much more sense since it stores the information added to airports.

Below my notes about the code:

airports = []

options = int(input ("\nAirport Data Management \n1. Enter a new airport \n2. Fetch airport information \n3. Quit \nPlease choose an option (1-3): "))

while options != 3:

    if options == 1:
        ICAO_code_enter = input("Enter the ICAO code: ")
        name_airport_enter = input("Enter the airport name: ")
        airports.append({"id":ICAO_code_enter, "name":name_airport_enter})          # This format to add to the list a dictionary.
        print(f"Airport {name_airport_enter} with ICAO code {ICAO_code_enter} has been added.")
        options = int(input ("\nAirport Data Management \n1. Enter a new airport \n2. Fetch airport information \n3. Quit \nPlease choose an option (1-3): "))

    elif options == 2:
        ICAO_code_fetch = input("Enter the ICAO code: ")
        for i in airports:                                                                                # Loops through the list
            if i["id"] == ICAO_code_fetch:                                                                # If the ID inside each dictionary matches, then proceed. Here I learned that 'i' becomes the name of the dictionary. So if i want to access something inside of it: i["key"].
                name_airport_fetch = i["name"]                                                            # This was needed due to formatting, since the print was not accepting {i[name]}
                print(f"The airport with ICAO code {ICAO_code_fetch} is {name_airport_fetch}.")
                options = int(input ("\nAirport Data Management \n1. Enter a new airport \n2. Fetch airport information \n3. Quit \nPlease choose an option (1-3): "))
        if i["id"] != ICAO_code_fetch:                                                                   # This was added here out of the for/in, in order to give the first 'if' the possibility to loop through every dictionary before returning that airport was not found.
            print(f"No airport found with ICAO code {ICAO_code_fetch}.")
            options = int(input ("\nAirport Data Management \n1. Enter a new airport \n2. Fetch airport information \n3. Quit \nPlease choose an option (1-3): "))

print("Thank you for using the Airport Data Management system. Goodbye!")
"""

"""
Note for myself:

# UNDERSTANDING DIFFERENCES

In a list:

1) We create a variable and equal it to [].
2) We use variable.append() or variable.remove() to add/remove items.
3) To access data variable[index]

Note: There are other features. Check https://metropolia-sw.github.io/sw1-python/en/06_list_structure_and_for_loop.html.

In a tuple:

1) We create a variable and equal it to ().
2) To access data variable[index]

Note:
- It cannot be changed (add/remove).
- It is usually used for fixed information as months, days of the week, etc.
- Less memory usage.

MORE FEATURES PENDING TO ADD AFTER CLASS.

In a set:

1) We create a variable and equal it to set().
2) We use variable.add() or variable.add() to add/remove items.

Note:
- Items are not printed in order.
- It cannot have 2 identical values within it.
- The values do not need to be the same type (string, number, etc).

In a dictionary:

1) We create a variable and equal it to {}.
2) Inside of {}, we add "key":"value"
3) If I variable["key"] it prints the value.
4) To add something: variable["new key"] = "new value".
5) To change something: variable["key that is already there"] = "new value".

In a dictionary inside a list:

print(variable): Prints the list with every single dictionary that is inside.
print(variable[0]): Print the first dictionary within the list with all its keys as values.
print(variable[0]["key"]) prints whatever value comes after "key" for the first dictionary within the list.

Note: If you add a dictionary to a list using append, variable.append() only takes one dictionary at a time.
"""