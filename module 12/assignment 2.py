import requests

API_KEY = "a5a42f5d67a3ee3a0d0482d2b7be1052"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

municipality_name = input("Enter municipality name: ")

full_url = f"{BASE_URL}?q={municipality_name}&appid={API_KEY}&units=metric"

try:
    response = requests.get(full_url)


    data = response.json()

    # Extract weather description and temperature
    weather_description = data["weather"][0]["description"]
    temperature = data["main"]["temp"]

    # Print the results in the specified format
    print(f"Weather: {weather_description}")
    print(f"Temperature: {temperature} Celsius")

except requests.exceptions.HTTPError as err:
    print(f"HTTP Error: {err}")
    print("Could not retrieve weather data. Please check the municipality name and your API key.")
except requests.exceptions.RequestException as err:
    print(f"An error occurred: {err}")
except KeyError:
    print("Could not find weather data for the specified municipality.")