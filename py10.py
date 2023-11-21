# Function to find sub-list in the list
def sub_list(nums):
    # Iterate through all possible sub-list
    for i in range(len(nums)):
        current_sum = 0
        for j in range(i, len(nums)):
            # Add elements to the current sum
            current_sum += nums[j]

            # If the current sum is zero, there is a sub-list with sum 0
            if current_sum == 0:
                return True

    # If no sub-list with sum 0 is found
    return False

my_list = [4, 2, -3, 1, 6]
result = sub_list(my_list)

if result:
    print("There is a sub-list with sum 0.")
else:
    print("No sub-list with sum 0 found.")
