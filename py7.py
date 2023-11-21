# Function to find first non repeating element in the list
def non_repeating_element(nums):
    # Create a dictionary to store the frequency of each element
    frequency_dict = {}

    # Iterate through the list to count the frequency of each element
    for num in nums:
        if num in frequency_dict:
            frequency_dict[num] += 1
        else:
            frequency_dict[num] = 1

    # Iterate through the list again to find the first non-repeating element
    for num in nums:
        if frequency_dict[num] == 1:
            return num

    # If no non-repeating element is found, return None
    return None


numbers = [2, 3, 4, 2, 3, 5, 4, 6]
result = non_repeating_element(numbers)

if result is not None:
    print(f"The first non-repeating element is: {result}")
else:
    print("No non-repeating element found in the list.")
