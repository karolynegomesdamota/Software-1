money = float(input ("Enter how much money you have here: "))

if money >= 10:
    print ("You can buy chocolate!")
else:
    print ("You are poor!")

# The else also works without "else" if I post it right below the if without indentation. Example:
#if money >= 10:
#    print ("You can buy chocolate!")
#print ("You are poor!")

# If I had set money as = 5, we call it hard code. If I add an input as I did, we have a "soft" code that is receiving the info externally.

# We can even make the code more "complex" and compare variables against another variables and add more ifs:

money = float(input ("Enter how much money you have here: "))

chocolate_price = 10
toast_price=3

if money <= toast_price :
    print ("You are broke!")
if money >= toast_price and money < toast_price + chocolate_price:
    print ("You can get a toast!")
if money >= toast_price + chocolate_price:
    print ("You can get a toast and chocolate!")

# And logical statement used here

receipt = input ("Do you want a receipt? ")

if receipt == "yes":
    print ("Here you have!")
elif receipt == "no" or "nope":
    print ("Ok!")
else:
    print ("No comment")

# Or logical statement used here. Also elif: If it's used if we want everything to run (for example, where we want to print many results if the input matches many). If we use elif, as soon as it runs a match, it stops.

# != Example

print ("If today is your birthday, you get a discount!")
birthday = input ("Enter your birthday: ")

if birthday == "25/08":
    print ("Yay! You get a discount!")
if birthday != "25/08":
    print ("Sad! No discount for you!")

# Not logical operator

being_class= input ("What are you? ")

if being_class != "student":
    print("You are not a student. Go to the lobby and ask for help. You are not allowed to enter this floor!")
if being_class == "student":
    print("You are a student. Please come in!")

"""""
Multiple
Lines
Quote
"""""