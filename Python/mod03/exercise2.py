import math

radius = input("Enter the radius of the circle: ")

radius = float(radius)

area = radius ** 2 * math.pi

print("The area of the circle is " + str(area))




#- The program should prompt the user with "Enter the length of the rectangle: "
#- The program should prompt the user with "Enter the width of the rectangle: "
# The program should calculate the perimeter and area
#- The program should output the perimeter in the form "The perimeter of the rectangle is [perimeter]"
#- The program should output the area in the form "The area of the rectangle is [area]"
#- Store the length in a variable called 'length'
#- Store the width in a variable called 'width'
#- Store the perimeter in a variable called 'perimeter'
#- Store the area in a variable called 'area'

length = float(input("Enter the length of the rectangle: "))

width = float(input("Enter the width of the rectangle: "))
width = float(width)

perimeter = 2 * (length + width)
area = length * width
# Why set this to 0 and not going straight to the formula? To check if there are errors. Later we set the formula, before it was = to 0.2


print ("The perimeter of the rectangle is " + str(perimeter))
print ("The area of the rectangle is " + str(area))
