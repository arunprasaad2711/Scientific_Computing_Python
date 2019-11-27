"""

For Loop

"""

# p = range(0, 10)
# 0, 3, 6, 9

# range(start, stop+increment, increment)
# for i in range(0, 11):
# 	print(i)

# Iterating over lists

l1 = ["Mercury", "Venus", "Earth"]
t1 = ("Mars", "Jupiter", "Saturn")
s1 = {"Uranus", "Neptune", "Pluto"}

for planet in s1:
	print(planet)
	
d1 = {"Planet": "Mercury", "Position": 1, "Temp": 400.0}

for key, value in d1.items():
	print(key, value)