from example import Flask, jsonify

app = Flask(__name__)
@app.route("/prime_number")
def is_prime(n: int) -> bool:

    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True



def prime_number(number):

    result = {
        "Number": number,
        "isPrime": is_prime(number)
    }
    return jsonify(result)


if __name__ == '__main__':
    app.run(use_reloader=True,host='127.0.0.1',port=5000)





