# Function to find triplet in the list
def triplet(nums, target_sum):
    n = len(nums)

    # Iterate over each triplet combination
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if nums[i] + nums[j] + nums[k] == target_sum:
                    # Triplet found
                    return [nums[i], nums[j], nums[k]]

    # No triplet found
    return None

nums = [10, 20, 30, 9]
target_sum = 59
result = triplet(nums, target_sum)

if result:
    print(f'Triplet with sum {target_sum}: {result}')
else:
    print('No triplet found with the given sum.')
