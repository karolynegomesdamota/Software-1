user_name = "python"
user_password = "rules"

typed_name = input("Enter username: ")
typed_password = input("Enter password: ")

counts = 0

while counts <4:
    if typed_name == user_name and typed_password == user_password:
        print("Welcome")
        break
    elif typed_name != user_name or typed_password != user_password:
        print("Incorrect username or password. Please try again.")
        typed_name = input("Enter username: ")
        typed_password = input("Enter password: ")
        counts = counts + 1

if typed_name != user_name and typed_password != user_password:
    print("Access denied")