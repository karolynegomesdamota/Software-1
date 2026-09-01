import random

roll = int(input("How many dice to roll: "))

results = []

for i in range(roll):
    results.append(random.randint(1,6))

print (f"Sum of the dice: {sum(results)}")

"""
Note for myself:
At the beginning, the meaning of i was not very clear to me.
The teacher said to "translate" it into i = variable[index].

For example here:

for i in variable: # i means the index within a previous created variable called "variable"
    print (i)

This will run through all the index values of "variable" and, in this specific case, it will print separately each one (for each loop round) and stop when there's nothing else.

So it's basically:

print (variable[0])
print (variable[1])
print (variable[2])
print (variable[3])

A good way to clearly see this: Name the 'i' the singular name of the plural variable name.
For example: The variable is called 'names' and the i is 'name'.
"""