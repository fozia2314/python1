import mysql.connector
# %%
# Establish a connection


def get_airports_by_country(country_code):
    query = f"select count(*) from airport WHERE iso_country = '{country_code}' GROUP BY type ORDER BY type DESC"
    cursor = connection. cursor ()
    cursor.execute(query)
    result = cursor. fetchall()
    print(
         f"Airports in {country_code}: \n{result[0][0]} small_airport airports\n{result[1][0]} medium_airport airports\n{result[2][0]} heliport airports\n{result[3][0]} large_airport airports")
    return result
connection = mysql.connector.connect(
user="root",
password="Frezie350",
host="localhost",
database="flight_game",
autocommit=True
)
def run_country():
    country_code = input("Enter the country code(e.g.,FI for Finland):")
    get_airports_by_country(country_code)
#%%
run_country()