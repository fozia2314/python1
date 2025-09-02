numbers =[]
while True:
    user_input =input("Enter a number: ")
    if user_input =="":
        break
    if numbers.append(float(user_input)):
        print("Invalid input. Please enter a number or press enter to quit.")
numbers.sort(reverse=True)
print("The greatest numbers in descending order: ")
for i in range(min(5, len(numbers))):
    print(numbers[i])