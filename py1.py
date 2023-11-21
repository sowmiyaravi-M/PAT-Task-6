# Function to find EVEN and ODD numbers in the given list
list = [10, 501, 22, 37, 100, 999, 87, 351]

# List of even numbers
even_numbers = [num for num in list if num % 2 == 0]

# List of odd numbers
odd_numbers = [num for num in list if num % 2 != 0]

print("Original List:", list)
print("Even Numbers:", even_numbers)
print("Odd Numbers:", odd_numbers)