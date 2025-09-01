username = "python"
password = "rules"
i = 1

while i <= 5:
    entered_username = input("Enter username: ")
    entered_password = input("Enter password: ")

    if i == 5:
        print("Access denied")
    if entered_username == username and entered_password == password:
        print("Welcome")
        break

    if entered_username != username and entered_password != password and i != 5:
        print("Incorrect username or password. Please try again.")
    i += 1  # increase attempt count
