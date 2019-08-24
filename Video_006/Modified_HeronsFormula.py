'''
Program to calculate the area of a triangle using Heron's formula
'''

# Get inputs
a = float(input("Enter the side 'a' of the triangle:"))
b = float(input("Enter the side 'b' of the triangle:"))
c = float(input("Enter the side 'c' of the triangle:"))

# Properties of a triangle:
# Triangle has 3 sides greater than zero.
# Sum of any two sides is greater than the third side.

if(a <= 0.0 or b <= 0.0 or c <= 0.0):
	print("Sides of a triangle can't be zero or negative!")
elif( a >= b+c or b >= c+a or c >= a+b ):
	print("The values violate triangle inequality!")
else:
	# Calculate the semi-perimeter
	s = (a + b + c)*0.5
	
	# Find the Area
	Area = (s*(s-a)*(s-b)*(s-c))**0.5
	
	# Print the result
	print("The area of the triangle with sides a = {}, b = {}, and c = {} is {}".format(a, b, c, Area))