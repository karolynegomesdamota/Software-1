import random

three_digit_code = str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9))
four_digit_code = str(random.randint(1, 6)) + str(random.randint(1, 6)) + str(random.randint(1, 6)) + str(random.randint(1, 6))

print ("3-digit code: " + three_digit_code)
print ("4-digit code: " + four_digit_code)