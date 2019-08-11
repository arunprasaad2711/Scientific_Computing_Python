"""
Primary Data Types
"""

# id() - returns the memory location ID of the variable
# type() - returns the datatype of the variable
a = 1.5     # Float/Real
print(a, id(a), type(a))

a = "hello" # String/Character
print(a, id(a), type(a))

a = 5       # Integer
print(a, id(a), type(a))

a = True    # Logical
print(a, id(a), type(a))

a = 6.0+7.8j    # Complex
print(a, id(a), type(a))

a = [7, 8.9, 10] # List
print(a, id(a), type(a))

a = (5.2, 4, 12) # Tuple
print(a, id(a), type(a))

a = {'v1': 6, 'v2' : 10} # Dictionary
print(a, id(a), type(a))

# Get the ASCII/unicode value of a character
print(ord('Z'))
# Get the character for the ASCII/unicode
print(chr(98))
print(chr(15896))
