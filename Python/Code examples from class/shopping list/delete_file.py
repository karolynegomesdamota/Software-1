import os

give_file_name = input("Enter the name of the file you want to delete: ")
while not os.path.exists(give_file_name):
    try:
        with open(give_file_name, "r") as file:
            file_data = file.read()
        print(file_data)
    except FileNotFoundError:
        print("File not found!")
        give_file_name = input("Enter the name of the file you want to delete: ")
    except IOError:
        print("Other error")

if os.path.exists(give_file_name):
            os.remove(give_file_name)