# Introduction to Scientific Computation Using Python

by [Arun Prasaad Gunasekaran](https://arunprasaad2711.github.io)

Video 4 : Operations Part 1

## Table of Contents
<!-- TOC -->

- [Introduction to Scientific Computation Using Python](#introduction-to-scientific-computation-using-python)
  - [Table of Contents](#table-of-contents)
  - [Basic Arithmetic Operations in Python](#basic-arithmetic-operations-in-python)
  - [Program to test all Basic Operations](#program-to-test-all-basic-operations)
  - [Output](#output)

<!-- /TOC -->

## Basic Arithmetic Operations in Python

| Operator 	|      Name      	|  Operation 	| Example 	| Result 	|               Remark              	|
|:--------:	|:--------------:	|:----------:	|:-------:	|:------:	|:---------------------------------:	|
|     +    	|    Addition    	|  ``a + b`` 	|  5 + 6  	|   11   	|          Normal Addition          	|
|     -    	|   Subtraction  	|  ``a - b`` 	|  5 - 6  	|   -1   	|         Normal Subtraction        	|
|     *    	| Multiplication 	|  ``a * b`` 	|  5 * 6  	|   30   	|       Normal Multiplication       	|
|     /    	|    Division    	|  ``a / b`` 	|  6 / 4  	|   1.5  	|          Normal Division          	|
|    //    	| Floor Division 	| ``a // b`` 	|  15 // 4 	|    3   	|  Division + removes decimal part  	|
|     %    	|     Modulus    	|  ``a % b`` 	|  22 % 4 	|    2   	| Returns the Remainder of Division 	|
|    **    	| Exponentiation 	| ``a ** b`` 	|  2 ** 4 	|   16   	|     Same as ``2*2*2*2``. Exponent     	|

## Program to test all Basic Operations

```python

a = 11
b = 2

print("a = ", a, " and b = ", b)

# Addition
print("a + b = ", a + b)
# Subtraction
print("a - b = ", a - b)
# Multiplication
print("a * b = ", a * b)
# Division
print("a / b = ", a / b)
# Floor Division
print("a // b = ", a // b)
# Modulus
print("a % b = ", a % b)
# Exponentiation
print("a ** b = ", a ** b)

```

## Output

```
a =  11  and b =  2
a + b =  13
a - b =  9
a * b =  22
a / b =  5.5
a // b =  5
a % b =  1
a ** b =  121
```