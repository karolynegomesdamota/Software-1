numbers = []

number = input("Enter a number: ")
if number != "":
    number = float (number)
    numbers.append(number)

while number != "":
    number = input("Enter a number: ")
    if number != "":
        number = float (number)
        numbers.append(number)

numbers.sort(reverse=True)
five_greatest = numbers[:5]

print(f"The greatest numbers in descending order:")
for n in five_greatest:
    print(n)


"""
Notes for myself: Problems and findings during exercise.

# Empty space within numbers list:

My initial code did not have the if within while. This caused the last empty input "" to be registered within the numbers list because of the numbers.append(number).
I had to add a if so that empty spaces were not added to the list.

# Sorting

At first I typed in VSCode "sort" and sorted came out. I used it as sorted(numbers, reverse=True).
It was working as expected, but it was not the format required by Moodle.
Then I researched and found another format that was numbers.sort(reverse=True) and it matched what Moodle required.
After investigating sorted(numbers, reverse=True) only works within a print. If I print numbers separately after this code, it will not be sorted.
While numbers.sort(reverse=True) reorganizes the number from that point on. So if I print only the numbers after this code, it will be already sorted.

# Printing the five results:

At first I did not know how to create a single logic to print the 5 first numbers.

While trying to figure it out I discovered {list[:4]} or {list[4:]}, which might be useful in the future.
This prints each item of the list and the [:4] sets it to up to the fourth item. Or, [4:] from the fourth item onwards.
In the end, this did not help me because it did not match the result expected by Moodle, since this prints a list [a, b, c, d] and not separate items.

Then, I tried adding separate prints as print(five_greatest[0]), print(five_greatest[1]), etc. up to five_greatest[4].
This initially worked, but when I entered less than 5 numbers, which was giving some error since those items did not exist.

So, finally I realized that I needed to create a for to loop for the numbers of times corresponding to the number of items within the five_greatest list.
Then, I added for n in five_greatest: print(n).
This means that I have this action to happen the X of times (five_greatest - the number of items inside of it).
On the other hand, (n) is each item within the list that is being looped in that specific round.
SO: during the first loop n was the first item, during the second loop n was the second item, etc.

Finally, everything was working as intended, but only printing 4 numbers, so I changed numbers[:4] to numbers[:5].
So, it's important to note that list[:4] stops BEFORE index 4 and list[4:] starts INCLUDING index 4.
"""