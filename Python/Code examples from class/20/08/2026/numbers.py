first = -9
second = 12_456_123_180 # We can use underscore to make big numbers more clear. But it will be printed without it.
third = 4973 # This is called float because it's a number with decimals. Remember to always use (.) instead of comma.
fourth = -4 + 2j

print(first)
print(second)
print(third)
print(fourth)
print(fourth.real)
print(fourth.imag)
# The real part of a complex number is the one without j. Th imaginary part is the one with j.

# Exercise 2 of MOD03 - Step by step logic until we ge to the final result

radius = input ("Enter the radius of the circle: ")
print (radius * 2)
# This does not produce the result we look for because it multiplies the string. Basically repeats the text.
# We need to convert the text into number with int (whole number) or float (number with decimals)

# To solve the previous issue:

radius = input ("Enter the radius of the circle: ")
print (int(radius) * 2)
print (float(radius) * 2)
# We can use any option, depending on which kind of result we want (whole number or with decimals)

# To complete the task correctly we need to do this:

import math
# We need to import math to make pi work. This gives you access to built-in mathematical functions and constants.

radius = input ("Enter the radius of the circle: ")
area = float(radius) ** 2 * math.pi
print ("The area of the circle is" + str(area))
# This format was giving error the number, so we broke it down as coded below.

import math

radius = input("Enter the radius of the circle: ")
# Input is always string, so we need to convert it into number. This is a exam question.

radius = float(radius)
# We use this to covert the text we receive into number

area = radius ** 2 * math.pi
# This is simply the formula

print("The area of the circle is " + str(area))
# Here we convert the number back to string using str because Moodle itself was giving error and the code was asking for a text.