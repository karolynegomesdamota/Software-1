# Module 03

print ("'Hi' was said by Karo")
# I can use different quotation marks within the other to make them visible in the output.

print ('"I\'m Karo"')
# If I add a back slash I can quote and use apostrophe.

print ("Good")
print ("morning")
print ("everyone")
print ("Good \n morning \n everyone")
# If I add back slash + n within a single print, it breaks the line and it works as separate prints in different lines.

input ("Name: ")
print("Ok, you entered a name")
# After you run this, you need to go to Terminal and enter a name to continue runing the rest of the code.

# A variable is a storage of information in our machine. The name of it should be descriptive and not include spaces. If you want to simulate a space, you can use underscore (_).

name = input ("Name: ")
print(name)
print("My name is " + name + "!")
# We can use that variable to make to create a dynamic result.

name = input ("Give name: ")
greeting = "Hello, " + name + "!"
print(greeting)
# Moodle exercise. We created a variable within a variable and then printed it.

points = 10
print (points)
points= 50
print (points)
# You can change a variable by simply writing it again. It updates on the go as the code runs.

print ("There's a hidden print under this message.")
# print ("I will make this disappear by commeting it.")
print ("There's a hidden print on top of this message.")
# We can use this to test code and leave notes.