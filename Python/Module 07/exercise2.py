import random

def roll_dice (sides):
    random_dice_number = random.randint (1,sides)
    return random_dice_number

sides = int(input("Enter the amount of sides of your dice: "))

returned_from_function = roll_dice(sides)

if returned_from_function != sides:
    print(returned_from_function)
    while returned_from_function != sides:
        returned_from_function = roll_dice(sides)
        print(returned_from_function)
else:
    print(returned_from_function)


"""
Note for myself:

1) This part is exactly the same, but the amount of sides is passed by the input.
Simply added the variable as a parameter inside the () and replaced the upper value of the range for 'random' by that.
That way, whatever the user enters as sides is set as the max possible value produced.

import random

def roll_dice (sides):
    random_dice_number = random.randint (1,sides)
    return random_dice_number

sides = int(input("Enter the amount of sides of your dice: ")) # Needed to add int because random.randint was not able to process a string.

2) Then, I needed to figure out how to "capture" the return value of the function to use it in my if.
Initially, I was calling the function and then trying to create a variable and equalling it to the call.
That caused a problem (the function was being called twice).
Therefore, I only used one single statement to call it and also to store the result in a variable.

returned_from_function = roll_dice(sides) # Same logic from the previous exercise, but here we add the variable in order to pass the arguments (values) to the function.

3) Finally, I only needed to alter the names from the previous code.

if returned_from_function != sides:                   # If what comes from the function is not equal to the sides (sides = max result) provided by the user.
    print(returned_from_function)                     # Print the what comes from the function
    while returned_from_function != sides:            # And, in a loop, call the function again to generate more/different results. It stops when what comes from the function equals the sides (sides = max result)
        returned_from_function = roll_dice(sides)
        print(returned_from_function)                 # For every try, print what comes from the function.
else:
    print(returned_from_function)                     # If the first value coming from the function is already equal to the sides (sides = max result), print the number and stop.
"""
