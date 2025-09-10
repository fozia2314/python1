#Establish a connection
import mysql.connector
connection = mysql.connector.connect(
    user="root",
    password="Frezie350",
    host="localhost",
    database="flight_game",
    autocommit=True,

)
cursor = connection.cursor()
# %%
prompt = input("Enter the ICAO code of an airport: ")
query = f"select name, municipality from airport where ident = '{prompt}'"
cursor. execute(query)
result = cursor.fetchall()
print(f"Airport name: {result[0][0]}\nLocation: {result[0][1]}")