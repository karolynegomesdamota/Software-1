import random

def roll_dice ():
    random_dice_number = random.randint (1,6)
    return random_dice_number

dice = roll_dice()

if dice != 6:
    print(dice)
    while dice != 6:
        dice = roll_dice()
        print(dice)
else:
    print(dice)


"""
Notes for myself:

#Understanding functions

1) This would show anything on the Terminal since it is not being called. Even if it has a print inside.

import random
def roll_dice ():
    random_dice_number = random.randint (1,6)
    print(random_dice_number)
    return random_dice_number

2) Now, since a call is made, the Terminal would show whatever is inside the print. Keep in mind the return here does not play any role.
Therefore: The first example would should a number in the Terminal and the second example would should "blabla" in the Terminal.

import random
def roll_dice ():
    random_dice_number = random.randint (1,6)
    print(random_dice_number)
    return random_dice_number

import random
def roll_dice ():
    random_dice_number = random.randint (1,6)
    print("blabla")
    return random_dice_number

3) Return will be whatever you will use outside of the function.
Therefore, in the first example, if I dice = roll_dice(), and then print(dice). It will show a number.
But, if I do the same for the second one, it will show "None".

import random
def roll_dice ():
    random_dice_number = random.randint (1,6)
    print(random_dice_number)
    return random_dice_number

dice = roll_dice()
print(dice)

import random
def roll_dice ():
    random_dice_number = random.randint (1,6)
    print(random_dice_number)
    return

# Explaining remaining part of the code:

if dice != 6:                 # This works because of 'dice = roll_dice()'. And 'dice = roll_dice()' only works (has a value) due to return within the function not being empty.
    print(dice)               # This prints the number even if it is not 6.
    while dice != 6:          # Then, it loops 'dice = roll_dice()' call to get new values. And for every new value, it prints it. And, finally, it stops after the dice is 6.
        dice = roll_dice()
        print(dice)
else:                         # If at the very first try to dice is 6, the program prints it and stops.
    print(dice)


"""