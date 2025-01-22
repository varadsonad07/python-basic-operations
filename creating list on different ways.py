""" CREATING LIST ON DIFFERENT WAYS """

# Creating an empty list
empty_list = []
print("Empty List:", empty_list)

# List with elements
element_list = [1, 2, 3, 4, 5]
print("List with elements:", element_list)

# Mixed list with different data types
mixed_list = [1, 2, 3, 'varad', 4.5]
print("Mixed List:", mixed_list)

# List with repeated elements
repeated_list = [1, 2] * 4
print("Repeated List:", repeated_list)

# Operations on a list
sample_list = [1, 2, 3, 4, 2, 5, 1]
print("\nOriginal List:", sample_list)

# Length of the list
print("Length of the list:", len(sample_list))

# Count occurrences of an element
print("Count of 2:", sample_list.count(2))

# Append an element to the list
sample_list.append(10)
print("After appending 10:", sample_list)

# Insert an element at a specific index
sample_list.insert(7, 14)
print("After inserting 14 at index 7:", sample_list)

# Find the index of an element
print("Index of 4:", sample_list.index(4))

# Extend the list with another list
sample_list.extend([90, 80])
print("After extending with [90, 80]:", sample_list)

# Remove an element by value
sample_list.remove(80)
print("After removing 80:", sample_list)

# Pop an element by index
popped_item = sample_list.pop(3)
print("After popping index 3:", sample_list)
print("Popped item:", popped_item)

# Reverse the list
sample_list.reverse()
print("Reversed List:", sample_list)

# Sort the list
sample_list.sort()
print("Sorted List:", sample_list)

# Copy the list
copied_list = sample_list.copy()
print("Copied List:", copied_list)

# Clear the list
sample_list.clear()
print("Cleared List:", sample_list)

# Slicing a list
num_list = [10, 20, 30, 40]
print("\nOriginal List:", num_list)
print("Sliced [1:5]:", num_list[1:5])
print("Sliced [:3]:", num_list[:3])
print("Sliced [::3]:", num_list[::3])

# List comprehension examples
# Create a list of squares
squares = [x * 2 for x in range(5)]
print("\nSquares (list comprehension):", squares)

# Filter even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even_numbers = [x for x in numbers if x % 2 == 0]
print("Even Numbers (list comprehension):", even_numbers)
