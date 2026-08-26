"""
EXERCISE
Create a calculator program.
The calculator should allow the user to make calculations until they decide to quit
The calculator should print a menu, from which the user can choose a calculation. The available calculations are add, minus, and multiplication.
The calculator should then ask the user for two numbers
Finally, the calculator prints the result of teh calculation

Then, the calculator should print hte menu again, and allow the user to choose a new calculation and input new numbers.
"""

calculation_type = input ("The available calculations are '+' for additions, '-' for subtraction, and '*' for multiplications. If, otherwise, you want to stop the calculator enter 'stop'. ")
while calculation_type == "+" or "-" or "*" or "stop":
    if calculation_type == "+":
        num1 = (input ("Enter here the first value. If, otherwise, you want to stop the calculator enter 'stop'. "))
        if num1 == "stop":
            break
        num2 = (input ("Enter here the second value: "))
        addition = float(num1) + float(num2)
        print (addition)
        calculation_type = input ("The available calculations are '+' for additions, '-' for subtraction, and '*' for multiplications. If, otherwise, you want to stop the calculator enter 'stop'. ")
    elif calculation_type == "-":
        num1 = (input ("Enter here the first value. If, otherwise, you want to stop the calculator enter 'stop'. "))
        if num1 == "stop":
            break
        num2 = (input ("Enter here the second value: "))
        subtraction = float(num1) - float(num2)
        print (subtraction)
        calculation_type = input ("The available calculations are '+' for additions, '-' for subtraction, and '*' for multiplications. If, otherwise, you want to stop the calculator enter 'stop'. ")
    elif calculation_type == "*":
        num1 = (input ("Enter here the first value. If, otherwise, you want to stop the calculator enter 'stop'. "))
        if num1 == "stop":
            break
        num2 = (input ("Enter here the second value: "))
        multiplication = float(num1) * float(num2)
        print (multiplication)
        calculation_type = input ("The available calculations are '+' for additions, '-' for subtraction, and '*' for multiplications. If, otherwise, you want to stop the calculator enter 'stop'. ")
    elif calculation_type == "stop":
            break