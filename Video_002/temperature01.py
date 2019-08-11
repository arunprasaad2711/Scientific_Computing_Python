"""
Program to ask the name, temperature, and rainfall of a place and print it
"""

# This is a variable to save the name of the place
place = input("Enter the name of the place:")

# This is a variable to save the temperature of the place
temperature = float(input("Enter the temperature recorded today in Celsius:"))

# This is a variable to save the name of the place
rainfall = float(input("Enter the rainfall recorded today in mm per day:"))

# Print statement
print("In", place, "today it rained", rainfall, "mm  and the temperature is", temperature, "degree celsius")
