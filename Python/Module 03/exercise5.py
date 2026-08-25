talents = float(input ("Enter talents: "))
pounds = float(input ("Enter pounds: "))
lots = float(input ("Enter lots: "))

talent = 20 * 32 * 13.3 * talents
pound = 32 * 13.3 * pounds
lot = 13.3 * lots

total_grams= lot + pound + talent
kilograms= total_grams / 1000
remaining_grams= (kilograms - int(kilograms)) * 1000

print ("The weight in modern units:")
print (str(int(kilograms)) + f" kilograms and {remaining_grams:.2f} grams.")

# Note to myself: Remember input will always be a string so you must convert it to make calculations. And then, when printing, if mixed with strings, you must convert it back.
# Note to myself: The output formatting does not work directly if you try to apply it to a str(remaining_grams), you must add it within a string and {remaining_grams:.2f}. But this works: print (f"{remaining_grams:.2f}")