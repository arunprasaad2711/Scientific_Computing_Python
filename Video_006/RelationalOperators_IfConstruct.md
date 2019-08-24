# Introduction to Scientific Computation Using Python

by [Arun Prasaad Gunasekaran](https://arunprasaad2711.github.io)

Video 6 : Relational Operators and If construct

## Table of Contents

<!-- TOC -->

- [Introduction to Scientific Computation Using Python](#introduction-to-scientific-computation-using-python)
  - [Table of Contents](#table-of-contents)
  - [Basic Relational Operators in Python](#basic-relational-operators-in-python)
  - [Basic Logical Operators in Python](#basic-logical-operators-in-python)
  - [If-else construct](#if-else-construct)
    - [Note](#note)
  - [Updated Heron's Formula](#updated-herons-formula)

<!-- /TOC -->

## Basic Relational Operators in Python

| Operator 	|           Name           	|  Operation 	|                                    Remark                                    	|
|:--------:	|:------------------------:	|:----------:	|:----------------------------------------------------------------------------:	|
|     <    	|         Less than        	|  ``a < b`` 	|         Returns ``True`` if a is less than b. Else returns ``False``.        	|
|    <=    	|   Less than or Equal to  	| ``a <= b`` 	|   Returns ``True`` if a is less than or equal to b. Else returns ``False``.  	|
|     >    	|       Greater than       	|  ``a > b`` 	|       Returns ``True`` if a is greater than b. Else returns ``False``.       	|
|    >=    	| Greater than or equal to 	| ``a >= b`` 	| Returns ``True`` if a is greater than or equal to b. Else returns ``False``. 	|
|    ==    	|         Equal to         	| ``a == b`` 	|         Returns ``True`` if a is equal to b. Else returns ``False``.         	|
|    !=    	|       Not Equal to       	| ``a != b`` 	|       Returns ``True`` if a is not equal to b. Else returns ``False``.       	|

## Basic Logical Operators in Python

| Operator 	|     Name    	|     Operation     	|                                        Remark                                        	|
|:--------:	|:-----------:	|:-----------------:	|:------------------------------------------------------------------------------------:	|
|    or    	|  Boolean Or 	|  ``con1 or con2`` 	| Returns ``True`` if either ``con1`` or ``con2`` is ``True``. Else returns ``False``. 	|
|    and   	| Boolean And 	| ``con1 and con2`` 	| Returns ``True`` if both ``con1`` and ``con2`` are ``True``. Else returns ``False``. 	|
|    not   	| Boolean Not 	|    ``not con1``   	|                       Returns ``True`` if ``con1`` is ``False``                      	|

## If-else construct

```python
if (condition1):
    # statements to execute if the condition1 is true
elif (condition2):
    # statements to execute if the condition2 is true
elif (condition3):
    # statements to execute if the condition3 is true
...
elif (conditionN):
    # statements to execute if the conditionN is true
else:
    # statements to execute if all the N conditions fail
```

### Note
The <key>Tabs</key> here are necessary! The tab indicates that the indended statements are a part of the construct.

## Updated Heron's Formula

Check if the inputs actually make a valid triangle.

```python
'''
Program to calculate the area of a triangle using Heron's formulae
'''

# Get inputs
a = float(input("Enter the side 'a' of the triangle:"))
b = float(input("Enter the side 'b' of the triangle:"))
c = float(input("Enter the side 'c' of the triangle:"))

if (a <= 0.0 or b <= 0.0 or c <= 0.0):
    print("Sides of a triangle can't be zero or negative!")
elif ( c >= a+b or b >= a+c or a >= b+c):
    print("The values violate triangle inequality!")
else:
    print("All conditions are valid!")
    # Calculate the semi-perimeter
    s = (a + b + c)*0.5

    # Find the Area
    Area = (s*(s-a)*(s-b)*(s-c))**0.5

    # Print the result
    print("The area of the triangle with sides a = {}, b = {}, and c = {} is {}".format(a, b, c, Area))
```