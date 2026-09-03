def get_season (month):
    if month in range(1, 13):
        season = seasons_of_the_year[month-1]
        print(f"You entered: {month}")
        print(f"The season is {season}.")
    else:
        print(f"You entered: {month}")
        print("Please enter a number between 1 and 12.")
        season = "not"

    return season

seasons_of_the_year = ("winter", "winter", "spring", "spring", "spring", "summer", "summer", "summer", "autumn", "autumn", "autumn", "winter")

month = int(input("Enter the number of a month (1-12): "))

season = get_season(month)


"""
Note for myself:

The code works, but seasons_of_the_year is horrendous (every season written one by one).
I need to figure out how to fix it.

I also wonder how the function works without passing seasons_of_the_year as a parameter. Ask teacher.

# Explanation of seasons_of_the_year[month-1]

'seasons_of_the_year' is referencing the tuple with all the seasons.
'seasons_of_the_year[0]' is referencing a specific index within that tuple (in this case 0 - the first one).
'seasons_of_the_year[month]' is referencing the the specific index within the tuple that corresponds to whatever number the user enters. In this case, the months are restricted to be 1-12, therefore we would always miss the index 0.
'seasons_of_the_year[month-1]'is referencing the specific index within is referencing the the specific index within the tuple that corresponds to whatever number the user enters minus 1, therefore solving the previous issue of always missing the index 0.
"""