'''

Sets in Python

'''

# Set
numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# print(numbers)
# print(type(numbers))

list1 = [2, 4, 6, 8, 10]
tuple1 = (1, 3, 5, 7, 9)

# List and tuple to set conversion!
even = set(list1)
odd = set(tuple1)

# print(even)
# print(numbers[4]) # will throw an error

# check if an entry is in a set
# print(7 in numbers)
# print(12 in numbers)

numbers1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 3, 5]
unique_numbers = set(numbers1)
# print(numbers1, unique_numbers)


## Adding entries to a set
numbers.add(11)
print(numbers)

numbers.update([12, 13, 14, 15])
print(numbers)

## Remove data
numbers.remove(15)
numbers.discard(13)
print(numbers)

v = numbers.pop()
print(numbers, v)

odd.clear()
print(odd)
del even
print(even)

