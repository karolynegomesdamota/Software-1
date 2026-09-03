name = input("Enter names: ")

names = set()

while name != "":
    if name in names:
        print("Existing name")
        name = input("Enter names: ")
    else:
        print("New name")
        names.add(name)
        name = input("Enter names: ")

for name in names:
    print(name)

"""
Notes for myself:
- For lists, we add with append.
- For sets, we add with add.
"""