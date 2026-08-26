
rounds = 3
while rounds >= 0:
    print("Hi, this is round " + str(rounds))
    rounds = rounds - 1

# Normal loop

rounds = 5
finished_rounds = 0
while finished_rounds < rounds:
    print ("Greeting!")
    finished_rounds += 1

# Fixed amount of repetition
# finished_rounds += 1 means finished_rounds = finished_rounds + 1

command = input ("What do you want do to? Enter exit to stop. ")

while command != "exit":
    print (f"You want to do {command}")
    command = input ("What do you want to do? Enter exit to stop. ")

# User ends repetition with command.

counter = 1
while counter <= 3:
    print (counter)
    counter = counter + 1

# This is an example of exam question, where they ask what the result would be. Answer: 1,2,3.

counter = 0
while counter < 5:
    print (counter)
    counter = counter + 2

# This is an example of exam question, where they ask what the result would be. Answer: 0,2,4.

counter = 5
while counter >= 0:
    print (counter)
    counter = counter - 1

# This is an example of exam question, where they ask what the result would be. Answer: 3,2,1,0.

outer = 1

while outer <= 5:
    inner = 1
    while inner <= 5:
        product = outer * inner
        print(f"{outer} times {inner} is {product}")
        inner += 1
    outer += 1

# Nested loops. We run 1 time the outer and inside of it the inner one will run 5 times. When this is finished, we will add one to the outer and run again the loop.

command = input ("What do you want do to? ")

while command != "stop":
    if command =="help":
        break
    print (f"You want to do {command}")
    command = input ("What do you want to do? ")

# Break

# Problems:

# Remember to add "additions" to rounds to close the loop

# Remember to mention the same variable. After the run, if you need to add a new command, refer the first variable.

# Make sure the condition is not infinite. For example lower and equal than 10 or greater than 10.

# MOD05-EX1 DONE IN CLASS

# Two options:

# My initial attempt:

number = 1

while number <=1000:
    remainder_number_by_3 = (number % 3)
    if remainder_number_by_3 == 0:
        print(number)
    number += 1

# Note to myself: This was not working at first because I had added the remainder_number_by_3 was outside of the while. So it was printing all the numbers.

# Cleaner option:

number = 1

while number <=1000:
    if number % 3 == 0:
        print(number)
    number += 1