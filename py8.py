# Function to find minimum element in the list
def minimum_element(rotated_sorted_list):
    for i in range(1, len(rotated_sorted_list)):
        if rotated_sorted_list[i] < rotated_sorted_list[i - 1]:
            return rotated_sorted_list[i]

    # If the loop completes, the minimum element is the first element
    return rotated_sorted_list[0]

# Example usage
sorted_rotated_list = [4, 5, 6, 7, 8, 9, 1, 2, 3]
minimum_element = minimum_element(sorted_rotated_list)
print("Minimum element:", minimum_element)
