import random
num_dice =int(input("How many dice to roll: Sum of the dice:"))
total_sum = 0
for _ in range(num_dice):
    roll = random.randint(1,6)
    total_sum +=roll
print(f"Sum of the dice: {total_sum}")