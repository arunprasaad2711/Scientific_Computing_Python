'''

Fibonacci Series

1, 1, 2, 3, 5, 8, ...
0, 1, ...

'''

# Input from user
n = int(input("Enter the number of terms in the series:"))

# Method 1: Make a list and use loops in a classical style
fib1 = [1, 1]

for i in range(2, n+1, 1):
	new_term = fib1[i-1] + fib1[i-2]
	fib1.append(new_term)

print(f"The fibonacci series upto {n} terms is:")
print(fib1)

# Method 2: Be more pythonic
a = 1
b = 1

fib2 = [a, b]

for i in range(2, n+1, 1):
	a, b = b, a+b  # Swap and Unpack
	fib2.append(b)

print(f"The fibonacci series upto {n} terms is:")
print(fib2)

