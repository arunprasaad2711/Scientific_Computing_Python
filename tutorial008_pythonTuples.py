'''

Tuples in python

'''

list1 = ["My Hero Academia", "Dr Stone", "Death Note"]

# Representing tuples
tuple1 = ("My Hero Academia", "Dr Stone", "Death Note")
tuple2 = "My Hero Academia", "Dr Stone", "Death Note"

# List to tuple conversion
fav_anime = tuple(list1)

# print(tuple1)
# print(tuple2)
# print(fav_anime)

# Can't add entries to a tuple
# tuple2.append("Full Metal Alchemist")

# Concatenation of two tuples!
cities1 = ("Paris", "Goettingen", "Kiruna")
cities2 = ("Madrid", "Athens", "Rome")

cities = cities1 + cities2

# print(cities)

# Multiply elements in a tuple
message = ("I will not come to school late anymore",)*100

# print(message)

# Accessing entries of a tuple
print(cities)
print(cities[3], cities[-3])

# deleting entries in a tuples
# Can't delete entries
# del cities[-1]

# can delete entire tuple
del cities
print(cities)











