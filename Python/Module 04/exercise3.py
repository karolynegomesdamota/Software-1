biological_gender = input ("Enter biological gender (male/female): ")

biological_gender_lowercase = biological_gender.lower()

hemoglobin = float(input ("Enter hemoglobin value (g/l): "))

if biological_gender_lowercase == "female" and hemoglobin < 117:
    print("Your hemoglobin is low.")
elif biological_gender_lowercase == "female" and (hemoglobin >= 117 and hemoglobin <= 155):
    print("Your hemoglobin is normal.")
elif biological_gender_lowercase == "female" and hemoglobin > 155:
    print("Your hemoglobin is high.")
elif biological_gender_lowercase == "male" and hemoglobin < 134:
    print("Your hemoglobin is low.")
elif biological_gender_lowercase == "male" and (hemoglobin >= 134 and hemoglobin <= 167):
    print("Your hemoglobin is normal.")
elif biological_gender_lowercase == "male" and hemoglobin > 167:
    print("Your hemoglobin is high.")
else:
    print ("Invalid gender.")

# Note to myself: To apply the lower case feature, you must first create the variable and then a new one and apply it to the first.