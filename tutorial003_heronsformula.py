"""

Program to calculate the area of a triangle using Heron's formula.

"""

# Sides of the triangle
a = float(input("Enter the side 'a' of the triangle:"))
b = float(input('Enter the side "b" of the triangle:'))
c = float(input('Enter the side \'c\' of the triangle:'))

# Perimeter of the triangle
peri = a + b + c

# Semi-perimeter
s = peri / 2

# Area
Area = (s*(s-a)*(s-b)*(s-c))**0.5

print(f"The perimeter and area of the triangle with sides {a}, {b}, and {c} units are: {peri}, {Area} respectively")