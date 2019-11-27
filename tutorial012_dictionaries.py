'''

Dictionaries

A collection of unordered (key, value)

key:value,
'''

# Sample dictionary
Mercury = {
	'Mass': 0.0553,
	'Radius': 2439.7,
	'Density': 5.43,
	'Units': ['times mass of Earth', 'km', 'times 1000 kg/m3']
}

# print(Mercury)
# print(type(Mercury))

# Empty dictionary
PlanetX = {}

# print(PlanetX, type(PlanetX))
PlanetX['Mass'] = 1.5
# print(PlanetX, type(PlanetX))

Mercury['Units'] = ['X mass of Earth', 'km', 'X Density of Water']

# print(Mercury)
# print(Mercury['Radius'])
# print(Mercury['Units'][1])
# print(f"The radius of Mercury is {Mercury['Radius']} {Mercury['Units'][1]}")

Venus = dict({
	'Mass': 0.815,
	'Radius': 6051.8,
	'Density': 5.20,
	'Units': ['times mass of Earth', 'km', 'times 1000 kg/m3']
})

Jupiter = dict([
	('mass', 317.83),
	('Radius', 71492),
	('Density', 1.33),
	('Units', ['times mass of Earth', 'km', 'times 1000 kg/m3'])
])

#print(Jupiter)

# Mutated Copy
PlanetY = Jupiter
# print(id(PlanetY), id(Jupiter))

# Actual Copy - Shallow copy
PlanetZ = Jupiter.copy()
print(id(PlanetZ), id(Jupiter))

# Clear Dictionary
PlanetZ.clear()
print(PlanetZ)

# Delete dictionary
del PlanetZ
# print(PlanetZ)

planetKeys = Venus.keys()
print(planetKeys, type(planetKeys))

planetValues = Venus.values()
print(planetValues, type(planetValues))