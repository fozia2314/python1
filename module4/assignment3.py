number = float(input("Enter a number (or press Enter to quit): "))
Smallest_number = number
Largest_number = number
while True:
    number_str = input("Enter a number (or press Enter to quit): ")
    if number_str == "":
        break
    number = float(number_str)

    if number < Smallest_number:
        Smallest_number = number
    if number > Largest_number:
        Largest_number = number

print("Smallest number:", Smallest_number)
print("Largest number:", Largest_number)
