# %%
import mysql.connector
from geopy import distance
# %
# Establish a connection

def get_airport_coordinates(icao_code):
    query = f"select latitude_deg, longitude_deg FROM airport where ident = '{icao_code}'"
    cursor = connection. cursor()
    cursor. execute(query)
    result = cursor.fetchall()
    return result
connection = mysql. connector .connect(
    user="root",
    password="Frezie350",
    port=3306,
    host="localhost",
    database="flight_game",
    autocommit=True
)
# %%
def run_airport_distance():
    first_icao_code = input( "Enter the ICAO code of the first airport: ")
    first_location = get_airport_coordinates(first_icao_code)
    second_icao_code = input("Enter the ICAO code of the second airport: ")
    second_location = get_airport_coordinates(second_icao_code)
    first_coordinate = (first_location[0][0], first_location[0][1])
    second_coordinate = (second_location[0][0], second_location[0][1])
    result = distance.distance(first_coordinate, second_coordinate).km
    print(f"Distance between {first_icao_code} and {second_icao_code}: (result) kilometers")