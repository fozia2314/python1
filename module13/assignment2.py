from example import Flask, jsonify
import sqlite3

app = Flask(__name__)

DATABASE = "airports.db"  # Path to your local SQLite database


def get_airport_by_icao(icao_code):
    """Fetch airport details from the database by ICAO code."""
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT ident, name, municipality FROM airports WHERE ident = ?",
        (icao_code.upper(),)
    )
    row = cursor.fetchone()
    conn.close()
    return row


@app.route('/airport/<icao_code>', methods=['GET'])
def get_airport(icao_code):
    """Return airport name and location for a given ICAO code."""
    airport = get_airport_by_icao(icao_code)

    if airport:
        result = {
            "ICAO": airport[0],
            "Name": airport[1],
            "Location": airport[2]
        }
    else:
        result = {
            "error": f"No airport found for ICAO code '{icao_code.upper()}'"
        }

    return jsonify(result)


if __name__ == '__main__':
    app.run(debug=True)
