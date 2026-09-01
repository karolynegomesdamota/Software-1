cities = []

city = input ("Enter the name of a city: ")
cities.append(city)

for ask in range(1,5):
    city = input ("Enter the name of a city: ")
    cities.append(city)

print ("\n\nThe cities you entered: ")
for i in cities:
    print (i)


"""
Note for myself: At first Moodle was giving me error, even though my result was correct.
Only after a while I noticed it required the 'question loop' to be a for/in and I had initially added while.

I had previously created a count and added a while that added counts in order to stop.

Now, however, I added:

for ask in range(1,5): # Loops 5 times and there's no need for a count.
    city = input ("Enter the name of a city: ")
    cities.append(city)

Finally, needed to add 2 breaks within the print because Moodle was giving me errors due to spaces.
"""