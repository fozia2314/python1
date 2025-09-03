def filter_even_numbers(input_list):
    """
    Filters a list of integers and returns a new list containing only the even numbers.
    """
    even_numbers = []
    for number in input_list:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers

# Main program for testing
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_list = filter_even_numbers(original_list)

print(f"Original list: {original_list}")
print(f"List with even numbers only: {filtered_list}")
