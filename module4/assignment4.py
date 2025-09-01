import random

randomr = random.randint(1, 10)
value = int(input("Enter guess:"))
while value != randomr:
    if value < randomr:
        print("Too low")

    elif value > randomr:
        print("Too high")
    value = int(input("Enter guess:"))
else:
    print("correct")
