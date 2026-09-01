digits = []

integer = int(input("Enter an integer: "))

integer = str(integer)

for i in integer:
    i = int (i)
    digits.append(i)

sum = (sum(digits))

integer = int (integer)

if (integer % 2 == 0 and integer != 2) or (integer % 5 == 0 and integer != 5) or (sum % 3 == 0) or (integer ==1):
    print (f"{integer} is not a prime number.")
else:
    print (f"{integer} is a prime number.")


"""
Note for myself:

# How I started:

I had to research how to manually figure out if a number is prime:

If it is divisible by 2, except 2: Not prime.
If it is divisible by 5, except 5: Not prime.
If the sum of the digits is divisible by 3: Not prime.
If the number is 1: Not prime

First: (integer % 2 == 0 and integer != 2) - Meaning: The remainder of the division by 2 is 0 and the number is not 2.
Second: (integer % 5 == 0 and integer != 5) - Meaning: The remainder of the division by 5 is 0 and the number is not 5.

Third:

I needed to figure out how to separate the digits and then calculate the sum.
Note that the exercise forced me to receive the input as an integer.
If I want to iterate a string (process it digit by digit), I need to convert it into a string.
So I added integer = str(integer)
Then I added a for to iterate (process the string in repeat) in order to produce a separate digits.

for i in integer: # Meaning: Inside integer, take each (i) item at a time and apply what follows.
     i = int (i) # This to convert it back to integer so the sum calculation can be done.
    digits.append(i) # This to add each item to the list digits

Forth: (integer == 1) - Meaning if the number is 1.

Then, we need to sum each digit that we have saved inside the list digits.

sum(digits) - I added it to a variable to be able to use it more clearly in the upcoming if sum = (sum(digits))

Then, in order to make the conditions of the upcoming 'if' to work, I need to convert the integer back to integer.

And finally, I add the if with the corresponding printings.

# Finding along the way:

While I was coding, I was having problems with strings and integers.
I was struggling to know if something was string or integers.
I then discovered type() which helps me to know what it is.
"""
