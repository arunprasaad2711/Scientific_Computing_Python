'''

Set methods

'''

n = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
p = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

n1 = {1, 2, 3, 4, 5}
n2 = {1, 2, 4, 8}
n7 = {3, 5, 7, 9}

# Set unions
# n3 = n1.union(n2)
n3 = n1 | n2
# print(n3)

# Set intersection
# n4 = n1.intersection(n2)
n4 = n1 & n2
# print(n4)

# Disjoint set
# print(n7.isdisjoint(n2))

# Superset
# print(n.issuperset(n1))
# print(n1.issuperset(n))

# Subset
print(n.issubset(n1))
print(n1.issubset(n))

# frozenset
frozen_p = frozenset(p)
print(frozen_p, type(p))

fp = frozen_p.union({14, 15})
print(fp)