airports = {} # Dictionary to store airport data (ICAO: Name)

while True:
    print("\nAirport Data Management")
    print("1. Enter a new airport")
    print("2. Fetch airport information")
    print("3. Quit")
    choice = input("Please choose an option (1-3): ")

    if choice == '1':
        icao_code = input("Enter the ICAO code: ").upper()
        airport_name = input("Enter the airport name: ")
        airports[icao_code] = airport_name
        print(f"Airport {airport_name} with ICAO code {icao_code} has been added.")
    elif choice == '2':
        icao_to_fetch = input("Enter the ICAO code: ").upper()
        if icao_to_fetch in airports:
            print(f"The airport with ICAO code {icao_to_fetch} is {airports[icao_to_fetch]}.")
        else:
            print(f"No airport found with ICAO code {icao_to_fetch}.")
    elif choice == '3':
        print("Thank you for using the Airport Data Management system. Goodbye!")
        break
    else:
        print("Invalid option. Please choose 1, 2, or 3.")