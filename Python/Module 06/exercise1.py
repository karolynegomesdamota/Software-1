import random

roll = int(input("How many dice to roll: "))

results = []

for i in range(roll):
    results.append(random.randint(1,6))

print (f"Sum of the dice: {sum(results)}")

# Note for myself: Still pending to completely understand what i is in for. Ask in class.