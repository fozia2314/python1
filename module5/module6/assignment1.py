import random

def roll_dice():
    """
    Returns a random dice roll between 1 and 6.
    """
    return random.randint(1, 6)

# Main program
roll_result = 0
while roll_result != 6:
    roll_result = roll_dice()
    print(roll_result)
