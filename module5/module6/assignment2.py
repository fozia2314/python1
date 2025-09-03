import random

def roll_dice(sides):

    return random.randint(1, sides)


num_sides = int(input("Enter the number of sides on the dice: "))
max_roll_to_stop = int(input(f"Enter the maximum roll (1-{num_sides}) that will stop the program: "))
while True:
    current_roll = roll_dice(num_sides)
    print(current_roll)
    if  current_roll  == max_roll_to_stop:
        break