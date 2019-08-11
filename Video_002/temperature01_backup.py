"""
Program to ask the name, temperature, and rainfall of a place and print it.
"""

# This is a variable to save the place
place = input("Enter the name of the place:")

# Rainfall variable
rainfall = input("Enter the rainfall recorded today in mm:")

# Temperature variable
temperature = float(input("Enter the temperature recorded today in Celsius:"))

# Print statement
print("In ", place, " today it rained ", rainfall, " mm  and the temperature is", temperature, " degree celsius")
