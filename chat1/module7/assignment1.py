month_number = int(input("Enter the number of a month (1-12): "))


def get_season(month_number):
    if month_number in range(9, 11):
        print(f"You entered: {month_number}\nThe season is autumn.")
        return
    if month_number in range(3, 6):
        print(f"You entered: {month_number}\nThe season is spring.")
        return
    if month_number in range(6, 8):
        print(f"You entered: {month_number}\nThe season is summer.")
        return
    if month_number > 12 or month_number <= 0:
        print(f"You entered: {month_number}\nPlease enter a number between 1 and 12.")
    else:
        print(f"You entered: {month_number}\nThe season is winter.")


get_season(month_number)