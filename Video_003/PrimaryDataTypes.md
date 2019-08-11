# Introduction to Scientific Computation Using Python

by [Arun Prasaad Gunasekaran](https://arunprasaad2711.github.io)

Video 3 : Primary Data Types in Python

## Table of Contents
<!-- TOC -->

- [Introduction to Scientific Computation Using Python](#introduction-to-scientific-computation-using-python)
  - [Table of Contents](#table-of-contents)
  - [What is a data type?](#what-is-a-data-type)
  - [Primary Data Types](#primary-data-types)
  - [String Data type](#string-data-type)
  - [Program to Test out different types of variables.](#program-to-test-out-different-types-of-variables)
    - [Code](#code)
    - [Output](#output)
  - [Some simple data-functions](#some-simple-data-functions)

<!-- /TOC -->

## What is a data type?
Simply put, it is the nature of the information.

## Primary Data Types

These are the primary data types available in python

```python
i = 1 # Integer. Stores integers
r = 5.78 # Floats. Stores numbers with decimal parts.
c = 'h' # Characters. Stores single characters. It is a string in python!
s = 'Strings' # Strings. Stores a series of characters
l = True/False # Logical. Stores binary values
cm = 6.0+5.6j  # Complex. Stores complex values
```

## String Data type

Strings are long chain of letters, numbers, symbols, and special characters. You can use both single and double quotes, but must end accordingly. Use slash to place quotes if needed.

In python, there is no equivalent for ``char`` type.

```python
"Hello", 
'Hello', 
'My name is Arun', 
"I asked, 'what is for lunch?'"
'I exclaimed, "This tree is big!"'
"I used slash \" to type a double quote symbol"
```

## Program to Test out different types of variables.

### Code

```python
a = 1.5     # Float/Real
print(a, id(a), type(a))
a = "hello" # String/Character
print(a, id(a), type(a))
a = 5       # Integer
print(a, id(a), type(a))
a = True    # Logical
print(a, id(a), type(a))
a = 6.0+7.8j    # Complex
print(a, id(a), type(a))
a = [7, 8.9, 10] # List
print(a, id(a), type(a))
a = (5.2, 4, 12) # Tuple
print(a, id(a), type(a))
a = {'v1': 6, 'v2' : 10} # Dictionary
print(a, id(a), type(a))
# Get the ASCII/unicode value of a character
print(ord('z'))
# Get the character for the ASCII/unicode
print(chr(98))
print(chr(32250))
```

### Output

```
1.5 140048331680624 <class 'float'>
hello 140048284573232 <class 'str'>
5 140048501217856 <class 'int'>
True 140048500811040 <class 'bool'>
(6+7.8j) 140048284294832 <class 'complex'>
[7, 8.9, 10] 140048284073544 <class 'list'>
(5.2, 4, 12) 140048284133416 <class 'tuple'>
{'v1': 6, 'v2': 10} 140048284066872 <class 'dict'>
122
b
緺
```

## Some simple data-functions

* ``id()`` : returns the memory location ID of the variable.
* ``type()`` - returns the datatype of the variable.
* ``ord()`` - returns the ASCII/Unicode value of the symbol.
* ``chr()`` - returns the symbol of the ASCII/Unicode value.
