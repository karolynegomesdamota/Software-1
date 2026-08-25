year = int(input("Enter a year: "))

year_divisible_4 = (year % 4)
year_divisible_100 = (year % 100)
year_divisible_400 = (year % 400)

if year_divisible_4 == 0 and year_divisible_100 == 0 and year_divisible_400 != 0:
    print(str(year) + " is not a leap year.")
elif year_divisible_4 == 0:
    print(str(year) + " is a leap year.")
else:
    print(str(year) + " is not a leap year.")

# Note to myself: remainder = dividend % divisor (modulo operator)