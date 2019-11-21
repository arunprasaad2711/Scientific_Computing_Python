'''

List: Values, Indexing, and Methods

'''

# List
l1 = [7, 6, 8, 4, 5, 9, 1]
# print(l1)

# Appending - add entry in the end
l1.append(10)
# print(l1)


# Insert - add entry on the given index
l1.insert(6, 22)
# print(l1)

# Extending list
l2 = ["John", "Bruce,", "Diana", "Hal", "Barry"]
l1.extend(l2)
# print(l1)

# Copy
# l3 = l2
# print(l3)
# print(id(l3), id(l2))
# l3.append("Clarke")
# print(l2)
# print(id(l3), id(l2))

l4 = l2.copy()
# print(id(l2), id(l4))

# Clear
# print(l4)
# l4.clear()
# print(l4)

# Count
l5 = [1, 3, 4, 1, 4, 5, 1, 2, 2, 2, 1]
# print(l5.count(2))

# Sort
print(l5)
l5.sort()
print(l5)

# index
l6 = [1, 3, 4, 1, 4, 5, 1, 2, 2, 11, 2, 1]
print(l6.index(11))

# Pop
print(l6)
last = l6.pop()
print(last, l6)

# Remove
print(l6)
l6.remove(2)
print(l6)

# del
print(l6)
del l6[5]
print(l6)

# Reverse
print(l6)
l6.reverse()
print(l6)


# len, max, min
print(len(l6), max(l6), min(l6))

















