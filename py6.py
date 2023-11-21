# Function to find duplicates in the list
def duplicates(list1, list2, list3):
    # Find common elements between list1 and list2
    common_elements_1_2 = set(list1) & set(list2)

    # Find common elements between list2 and list3
    common_elements_2_3 = set(list2) & set(list3)

    # Find common elements among all three lists
    common_elements_all = common_elements_1_2 & common_elements_2_3

    # Convert the result back to a list if needed
    duplicates = list(common_elements_all)

    return duplicates


list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
list3 = [5, 6, 7, 8, 9]

result = duplicates(list1, list2, list3)
print("Duplicates:", result)
