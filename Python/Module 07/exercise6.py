import math

def calculate_unit_price (diameter, price):
    unit_price_per_square_meter = price / ((math.pi * ((diameter/2))**2 / 10000))
    return unit_price_per_square_meter

diameter = int(input("Enter the diameter of the first pizza (cm): "))
price = int(input("Enter the price of the first pizza (euros): "))
pizza_1 = calculate_unit_price(diameter, price)

diameter = int(input("Enter the diameter of the second pizza (cm): "))
price = int(input("Enter the price of the second pizza (euros): "))
pizza_2 = calculate_unit_price(diameter, price)

print(f"Unit price of the first pizza: {pizza_1:.2f} euros/m²")
print(f"Unit price of the second pizza: {pizza_2:.2f} euros/m²")

if pizza_1 < pizza_2:
    print("The first pizza provides better value for money.")
else:
    print("The second pizza provides better value for money.")


"""
Note for myself:

# Calculations

Circle area: π*r^2. In this case, we have diameter (which is 2r).
The formula then should be: π*(d/2)^2. Plus, divide this by 10000 to pass from square cm to square meters.
Once we have the area, we use it to divide the price to get what a meter costs.

# Keep in mind:

I tried to loop the input questions, but it was making the code overly complicated.
import math

I also had initially issues because the calculation was not going through because the numbers were strings.
I fixed it by adding int.
"""