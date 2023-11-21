# Function to find Prime Numbers in the given List

#Using if Condition to find prime numbers
def prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

list = [10, 501, 22, 37, 100, 999, 87, 351]

prime_numbers = [num for num in list if prime(num)]

print("List:", list)
print("Prime numbers:", prime_numbers)
