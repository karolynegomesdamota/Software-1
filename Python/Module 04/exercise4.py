year = int(input("Enter a year: "))

year_divisible_4 = (year / 4) - int( year / 4)
year_divisible_100 = (year / 100) - int( year / 100)
year_divisible_400 = (year / 400) - int( year / 400)

if year_divisible_4 == 0 and year_divisible_100 == 0 and year_divisible_400 != 0:
    print(str(year) + " is not a leap year.")
elif year_divisible_4 == 0:
    print(str(year) + " is a leap year.")
else:
    print(str(year) + " is not a leap year.")

# Result matches, but Moodle expects me to do it differently (using modulo operator (%)). Ask professor if it must be coded exactly how Moodle determines it or if doing it differently but getting the same result is valid.
