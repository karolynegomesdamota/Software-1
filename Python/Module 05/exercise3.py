numbers = []

number = input("Enter a number (or press Enter to quit): ")
while number != "":
    number = float(number)
    numbers.append(number)
    number = input("Enter a number (or press Enter to quit): ")


print (f"Smallest number: {min(numbers)}")
print (f"Largest number: {max(numbers)}")

# Append adds a number to the end of the list.
# Ask in class: How is it possible that append is adding values to the list if it's out of the while.
# Note to myself: min() and max() gets the smallest and biggest number from a list. The problem is: it analysis it as a string and orders it alphabetically, so I need to make the values float.
# Note to myself: Ava explained me that to make the result float, I needed to enter number = float(number), so I directly enter a float to the list.
