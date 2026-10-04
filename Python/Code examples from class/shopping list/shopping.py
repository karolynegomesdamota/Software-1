
# This to create

with open("save.txt", "w") as file:
   file.write("writing first item\n")

# This to add

with open("save.txt", "a") as file:
   file.write("adding an extra item")

"""

# This to read

with open("save.txt", "r") as file:
   file_data = file.read()
   print("\nThis is read:")
   print(file_data)

with open("save.txt", "r") as file:
   file_data = file.readline()
   print("\nThis is readline:")
   print(file_data)

with open("save.txt", "r") as file:
   file_data = file.readlines()
   print("\nThis is readlines:")
   print(file_data)

"""

# Exercise 1:

# Creating and adding items.

# Exercise 2.

# read() and print it

with open("save.txt", "r") as file:
   file_data = file.read()
   print("\nThis is read print:")
   print(file_data)

# file.readlines() and print how many items there are in the list

with open("save.txt", "r") as file:
   file_data = file.readlines()
   print(f"\nItems in the list: {len(file_data)}")