def gallons_to_liters (gallons):
    while gallons >= 0:
        if gallons >= 0:
            l = gallons * 3.785
            print (f"{gallons} American gallons is {l:.2f} liters.")
            gallons = float(input("Enter a volume in American gallons (negative value to quit): "))
        else:
            print("Program finished.")
    print("Program finished.")

gallons = float(input("Enter a volume in American gallons (negative value to quit): "))

gallons_to_liters(gallons)

"""
Note for myself:

# Logic behind building this
1. Create the function with its own logic
2. Create the input that will be inserted in it as a parameter.
3. Add that input within a variable to the parameter and insert it where necessary.
4. Call the function.
    Note: In case you would have to use what the function returns, create a new variable and equal it to the function call.

# Reminder:

I was having issues formatting litters {l:.2f} because I forgot to add the f.
"""
