# Python program to demonstrate various operations on strings

# Initialize the string
string = "hello mamdam"

# Accessing by indexing (positive and negative)
print("Accessing by indexing (positive and negative):")
print(string[0])    # Positive indexing: First character
print(string[4])    # Positive indexing: Fifth character
print(string[-1])   # Negative indexing: Last character
print(string[-4])   # Negative indexing: Fourth character from the end

# Accessing by slicing (positive and negative)
print("\nAccessing by slicing (positive and negative):")
print(string[0:4])    # Positive slicing: First 4 characters
print(string[-6:])    # Negative slicing: Last 6 characters
print(string[::2])    # Slicing with step: Every second character

# String functions and operations
print("\nString functions and operations:")
print(len(string))                      # 1. Length of the string
print(string.find("hello"))             # 2. Find the index of the substring "hello"
print(string.count("m"))                # 3. Count the occurrences of the character 'm'
print(string.replace("mamdam", "varad")) # 4. Replace "mamdam" with "varad"
print(string.upper())                   # 5. Convert the string to uppercase
print(string.lower())                   # 6. Convert the string to lowercase
print(string.capitalize())              # 7. Capitalize the first letter of the string
print(string.startswith("hello"))       # 8. Check if the string starts with "hello"
print(string.endswith("madam"))         # 9. Check if the string ends with "madam"
