"""

Program to do basic arithmetic operations in python

Addition
Subtraction
Multiplication
Division
Modulus
Exponent

Fstring : Python 3.6+
"""

a = 2.0
b = 5.0

a1 = 7
b1 = 5

# Addition
c = a + b
# print("a = ", a, "and b = ", b, "and a + b = ", c)
print(f"a = {a}, and b = {b} and a + b = {c}")

# Subtraction
c = a - b
print(f"a = {a}, and b = {b} and a - b = {c}")

# Multiplication
c = a * b
print(f"a = {a}, and b = {b} and a * b = {c}")

# Division
c = a / b
print(f"a = {a}, and b = {b} and a / b = {c}")

# Integer Division
c1 = a1 // b1
print(f"a = {a1}, and b = {b1} and a / b = {c1}")

# Integer Modulus
r = a1 % b1
print(f"a = {a1}, and b = {b1} and a % b = {r}")

# Float Modulus
r = a % b
print(f"a = {a}, and b = {b} and a % b = {r}")

# Exponent 2^5 = 32
e = a**b
print(f"a = {a}, and b = {b} and a ^ b = {e}")