def gallons_to_liters(gallons):
    return gallons * 3.785


# Main program
while True:
    gallons_input = float(input("Enter a volume in American gallons (negative value to quit): "))

    if gallons_input < 0:
        print("Program finished.")
        break

    liters_output = gallons_to_liters(gallons_input)
    print(f"{gallons_input:.1f} American gallons is {liters_output:.2f} liters.")
else:
    print("Invalid input.")