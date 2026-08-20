first = -9
second = 12_456_123_180 # We can use underscore to make big numbers more clear. But it will be printed without it.
third = 4973 # This is called float because it's a number with decimals. Remeber to always use (.) instead of comma.
fourth = -4 + 2j

print(first)
print(second)
print(third)
print(fourth)
print(fourth.real)
print(fourth.imag)

#Moodle 2.

radius = input ("Enter the radius of the circle: ")
print (radius * 2)
# This shouldn't work because it multiplies the string. Basically repeats the text.
# We need to convert the text into number with int () or float (with decimals)
radius = input ("Enter the radius of the circle: ")
print (int(radius) * 2)
print (float(radius) * 2)

# To complete the task then we need do this:

import math
# We need to import math to make pi work.

radius = input ("Enter the radius of the circle: ")
area = float(radius) ** 2 * math.pi
print ("The area of the circle is" + str(area))
# It was giving error the number, so it should be a string so we use str
# Input is always string. This is a exam question.

import math

radius = input("Enter the radius of the circle: ")

radius = float(radius)
# We use this to covert the text we receive into number

area = radius ** 2 * math.pi
# This is simply the formula 

print("The area of the circle is " + str(area))
# Here we convert the number back to string using str because Moodle itself was giving error and the code was asking for a text.

# on top the result of exercese 2


