"""
EXERCISE
Create a calculator program.
The calculator should allow the user to make calculations until they decide to quit
The calculator should print a menu, from which the user can choose a calculation. The available calculations are add, minus, and multiplication.
The calculator should then ask the user for two numbers
Finally, the calculator prints the result of the calculation

Then, the calculator should print hte menu again, and allow the user to choose a new calculation and input new numbers.
"""

calculation_type = input("Select \n1. Addition \n2. Subtraction \n3. Multiplication \n4. Exit\n")

while calculation_type == "1" or "2" or "3":
    if calculation_type == "1":
        num1 = (input ("Enter the first value or 'stop' to exit.\n"))
        if num1 == "stop":
            break
        num2 = (input ("Enter the second value or 'stop' to exit.\n"))
        if num2 == "stop":
            break
        addition = float(num1) + float(num2)
        print (addition)
        calculation_type = input ("Select \n1. Addition \n2. Subtraction \n3. Multiplication \n4. Exit\n")
    elif calculation_type == "2":
        num1 = (input ("Enter the first value or 'stop' to exit.\n"))
        if num1 == "stop":
            break
        num2 = (input ("Enter the second value or 'stop' to exit.\n"))
        if num2 == "stop":
            break
        subtraction = float(num1) - float(num2)
        print (subtraction)
        calculation_type = input ("Select \n1. Addition \n2. Subtraction \n3. Multiplication \n4. Exit\n")
    elif calculation_type == "3":
        num1 = (input ("Enter the first value or 'stop' to exit.\n"))
        if num1 == "stop":
            break
        num2 = (input ("Enter the second value or 'stop' to exit.\n"))
        if num2 == "stop":
            break
        multiplication = float(num1) * float(num2)
        print (multiplication)
        calculation_type = input ("Select \n1. Addition \n2. Subtraction \n3. Multiplication \n4. Exit\n")


# For the initial selection, the exit should be created following a conditional logic and not simply break. So I removed the elif for 4 and removed it from the while. So now when I choose 4, it simply stops.
# I also rearranged and cleaned up inputs.
