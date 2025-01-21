# Python Program Demonstrating Various List Operations

# Experiment 4A: Basic List Operations

# Creating a list
my_list = [1, 2, 3, 4, 5, 6]

# Type of the list
print("Type of the list:", type(my_list))

# Modifying an element in the list
my_list[1] = 11
print("List after modifying the second element:", my_list)

# Adding an element to the end of the list
my_list.append(7)
print("List after appending 7:", my_list)

# Removing an element from the list
my_list.remove(5)
print("List after removing 5:", my_list)

# Inserting an element at a specific position
my_list.insert(3, 12)
print("List after inserting 12 at index 3:", my_list)

# Length of the list
print("Length of the list:", len(my_list))

# Checking if an element is present in the list
print("Is 5 in the list?", 5 in my_list)

# Experiment 4B: Slicing the List
print("\nExperiment 4B: Slicing the List")
print("Element at index 3:", my_list[3])
print("Elements from index 1 to 2:", my_list[1:3])
print("Elements from index 2 to 3:", my_list[2:4])

# Experiment 4C: Sorting the List
print("\nExperiment 4C: Sorting the List")
number_list = [50, 30, 10, 20, 40]

# Sorting in ascending order
number_list.sort()
print("List in ascending order:", number_list)

# Sorting in descending order
number_list.sort(reverse=True)
print("List in descending order:", number_list)

# Finding the largest and smallest numbers in a list
xyz_list = [50, 30, 10, 20, 40]
largest = max(xyz_list)
smallest = min(xyz_list)
print("Largest number in the list:", largest)
print("Smallest number in the list:", smallest)

# Experiment 4E: Reversing the List
print("\nExperiment 4E: Reversing the List")
abc_list = [77, 17, 29, 10]
abc_list.reverse()
print("Reversed list:", abc_list)

# Experiment 4F: Nested List Operations
print("\nExperiment 4F: Nested List Operations")
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Accessing elements in a nested list
print("Element at nested_list[1][2]:", nested_list[1][2])
print("Element at nested_list[0][1]:", nested_list[0][1])

# Modifying elements in a nested list
nested_list[0][2] = 10
print("Nested list after modifying an element:", nested_list)

# Appending elements to a nested list
nested_list[1].append(11)
print("Nested list after appending 11 to the second list:", nested_list)

# Adding a new sub-list
nested_list.append([15, 16, 17])
print("Nested list after appending a new sub-list:", nested_list)

# Looping through each row and column in a nested list
print("\nElements of the nested list:")
for row in nested_list:
    for element in row:
        print(element, end=" ")
    print()  # New line after each row
