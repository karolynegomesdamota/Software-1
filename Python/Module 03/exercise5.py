talents = input ("Enter talents: ")
pounds = input ("Enter pounds: ")
lots = input ("Enter lots: ")

talent = 20 * 32 * 13.3 * float(talents)
pound = 32 * 13.3 * float(pounds)
lot = 13.3 * float(lots)

total_grams= lot + pound + talent
kilograms= total_grams / 1000
remaining_grams= (kilograms - int(kilograms)) * 1000

print ("The weight in modern units:")
print (str(int(kilograms)) + f" kilograms and {remaining_grams:.2f} grams.")

# Note to myself: Remember input will always be a string so you must convert it to make calculations. And then, when printing, if mixed with strings, you must covert it back.
# ASK IN CLASS ANYWAY - Note to myself: The output formatting does not work directly if you try to apply it to a str(remaining_grams), you must add it within a string and {remaining_grams:.2f}.
# print (f"{remaining_grams:.2f}") works