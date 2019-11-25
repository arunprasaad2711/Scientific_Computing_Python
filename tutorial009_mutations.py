'''

Mutations in python

Remedies to avoid mutation
* use tuples instead
* do reassignments

'''


x = ["Boyle", "Lavoisier", "Pascal", "Charles"]

y = x
y.append("Thompson")

# print(x)
# print(y)
#
# print(id(x), id(y))

y1 = x.copy()
# print(id(x), id(y1))

y1.append("Rutherford")
# print(x)
# print(y1)


x1 = [1, 2, 3]
print(f"Initial id of x1 is {id(x1)}")
y1 = x1
print(f"Initial id of y1 is {id(x1)}")
x1 = [4, 5, 6]
print(f"Final id of x1 is {id(x1)}")
print(f"Final id of y1 is {id(y1)}")
print(x1, y1)

