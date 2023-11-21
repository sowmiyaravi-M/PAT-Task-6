# Function to count Happy Numbers in the given List
def happy_number(n):
    function = set()
    while n != 1 and n not in function:
        function.add(n)
        n = sum(int(digit) ** 2 for digit in str(n))
    return n == 1

def count_happy_numbers(numbers):
    count = 0
    for num in numbers:
        if happy_number(num):
            count += 1
    return count

# Given List
list = [10, 501, 22, 37, 100, 999, 87, 351]

# Count happy numbers in the list
happy_count = count_happy_numbers(list)

print(f"There are {happy_count} happy numbers in the list.")
