# Function to find the sum of First and Last digit in an integer
def sum_of_first_and_last_digit(number):
    # Convert the number to a string to easily extract digits
    number_str = str(number)

    # Extract the first and last digits
    first_digit = int(number_str[0])
    last_digit = int(number_str[-1])

    # Calculate the sum of the first and last digits
    sum_result = first_digit + last_digit

    return sum_result

# Get user input for an integer
user_input = int(input("Enter an integer: "))

# Call the function and display the result
result = sum_of_first_and_last_digit(user_input)
print(f"The sum of the first and last digits of {user_input} is: {result}")

