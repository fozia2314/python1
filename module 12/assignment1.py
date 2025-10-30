import requests


def get_chuck_norris_joke():
    api_url = "https://api.chucknorris.io/jokes/random"

    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            joke_data = response.json()
            print(joke_data["value"])
        else:
            print(f"Error: Unable to fetch joke. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:

        print(f"An error occurred: {e}")


get_chuck_norris_joke()