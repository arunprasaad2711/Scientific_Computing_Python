'''

Factorial of a positive integer.

n = 5,
5! = 5x4x3x2x1
25! = 25x24x...x1
0! = 1

'''

n1 = int(input("Enter the value of n:"))

if n1 < 0:
	print("Factorial of a negative integer(s) do not exist!")
	exit
else:
	for n in range(0, n1 + 1, 1):
		if n is (0 or 1):
			fact = 1
		else:
			fact = 1
			for i in range(2, n+1, 1):
				fact = fact * i
		print(f"The value of {n}! is {fact}")