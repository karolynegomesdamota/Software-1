import random

random_computer = random.randint(1, 10)

user_guess = int(input("Enter here your guess: "))

while random_computer != user_guess:
    if (user_guess < random_computer):
        print("Too low")
        user_guess = int(input ("Enter here your guess: "))
    elif (user_guess > random_computer):
        print("Too high")
        user_guess = int(input ("Enter here your guess: "))

print ("Correct")

# Note to myself: I need to provide some range within random.randint() for it to work.