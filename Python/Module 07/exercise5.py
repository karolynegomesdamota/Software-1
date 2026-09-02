def filter_even_numbers (original_list):
    for i in original_list:
        if i % 2 != 0:
            original_list.remove(i)
    return original_list

original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Original list:", original_list)

filtered_list = filter_even_numbers(original_list)

print("List with even numbers only:", filtered_list)

"""
Note for myself:

def filter_even_numbers (original_list):
    for i in original_list:                  # Loop through the list and for each item:
        if i % 2 != 0:                       # Check if the remainder of the division is not 0. If not, it is uneven.
            original_list.remove(i)          # If it is uneven, remove it from the list.
    return original_list                     # Return the original list, from which the uneven numbers have already been removed.

original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Original list:", original_list)

filtered_list = filter_even_numbers(original_list) # I put this in the middle because if I put the 2 prints together at the end, the original list is printed already without the uneven numbers.

print("List with even numbers only:", filtered_list)
"""