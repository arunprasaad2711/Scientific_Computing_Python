# Introduction to Scientific Computation Using Python

by [Arun Prasaad Gunasekaran](https://arunprasaad2711.github.io)

Video 2 : Meta Information and Basics

## Table of Contents
<!-- TOC -->

- [Introduction to Scientific Computation Using Python](#introduction-to-scientific-computation-using-python)
  - [Table of Contents](#table-of-contents)
  - [Benefits of these Videos](#benefits-of-these-videos)
  - [Why Python? - Funny Note](#why-python---funny-note)
  - [Why Python? - Serious note](#why-python---serious-note)
  - [Is Python absolutely advantageous?](#is-python-absolutely-advantageous)
  - [Different Versions of Python](#different-versions-of-python)
    - [Python 2 - Legacy](#python-2---legacy)
    - [Python 3 - Future](#python-3---future)
  - [So, what to look for in any programming language?](#so-what-to-look-for-in-any-programming-language)
  - [Program to ask the name, temperature, and rainfall of a place and print it](#program-to-ask-the-name-temperature-and-rainfall-of-a-place-and-print-it)
  - [Comments and Docstrings](#comments-and-docstrings)
  - [Input Command](#input-command)

<!-- /TOC -->

## Benefits of these Videos

* **Short term benefits:**
    * Useful for Assignments
    * Learning programming in a simpler way
    * Serves as an Icebreak to smoothen the class-to-research/application transition
    * Gaining comfort and confidence
    * Have a tool to solve simple and complex problems
* **Long term benefits:**
    * Skills are directly applicable in research
    * Helpful to cut-down pre-research timing (Finding fixes, looking for solutions etc.,)
    * You have a solid foundation to proceed further
    * You can almost all the fundamental tools
    
All the examples here are chosen carefully so that you all get a broad exposure to a variety of programming tools and useful functions and libraries.

## Why Python? - Funny Note

<img src="images/python.png" height="300" width="300">

Source: http://xkcd.com/353/

## Why Python? - Serious note

* Free, open source, cross platform
* __Object Oriented__, __modern__, **interpreted** Programming Language
* Very flexible and has a wide variety of features
* Little overhead and pre-requisite
* Easy access to work with Unix/Linux Shells
* One great choice to learn programming from scratch to advanced levels
* Very friendly, **intuitive** and **humane**
* Can combine this with other programming languages
* Plotting and visualization tools (1D, 2D, 3D) are great
* Can be used for making GUI apps, OS, web frame works etc.,
* Most importantly, you get to avoid **Software Piracy Issues**

## Is Python absolutely advantageous?
**No!**
Beacuse no programming language is perfect.
Then why to choose Python?,

* You love programming in general and want to explore a lot,
* You like the language,
* You want to do a variety of programming with a single main language,
    * eg: Webcrawling, Machine Learning, Data Analysis, Software development, Web development etc.,
* Not many licensing restrictions,
* Work demands,

Bottom line : Python is good, but not undisputed.

Other programming languages that are good : R, Julia, Sage, Mathematica, Maple, Matlab, Fortran, C, C++, IDL, Java, JavaScript, etc,

## Different Versions of Python

As of 2019, there are two versions of the Python Language: The Legacy 2.x series and the future 3.x series. Python 3.x came to existence because the founder of Python, Guido van Rossum wanted to add more features to the language. The problem was that adding those features meant dismantling the major framework of Python 2.x and rewrite a significant portion of the language. Consequently, to make sure that the already exisiting programs work well and to make sure the new features get implemented, the old version of python, namely 2.x remained as it is for backward compatibility, while the newer version of python namely 3.x has the new features added to it.

The result of this decision is the exisitence of 2 distinct versions of python with a lot of similarities on the top, with many differences underneath.

### Python 2 - Legacy

* Old version of Python
* Legacy Codes built on it
* No new version anymore
* Library Migration going on

### Python 3 - Future

* Newer version of Python
* The future of Python
* Revamped internal architecture - supports future technological implementations
* (Almost all) libraries are translated

We are in the **transition** period wherein we have access to use both the versions of Python. In the future, Python 2 will be obsolete, and in this transition period, almost all the libraries are being converted from Python 2 to Python 3. Infact, new libraries are being made in Python 3 extensively.

Consequently, as of 2019, Python 2.x series is stopping all major releases and releasing only sub releases for maintenance purposes. Other than that, the most active development is focussed on Python 3. The support and maintenance is only for people to transition from python 2.x to 3.x soon.

## So, what to look for in any programming language?

This is a (personal) checklist to keep in mind to pick a programing language for scientific computation.

- Basic data types, data conversions,
- Machine Scalability,
- Inter-operatability with other programming languages,
- Variables, constants, sizes, precisions
- Operators,
- Input/Output statements,
- Data formatting
- Loops and decision making statements,
- Advanced data types like arrays, pointers, derived data types,
- Functions, Subroutines,
- Handling data files,
- Objects, classes,
- External libraries/packages/modules
- Executing multiple files simultaneously
- Plotting and visualization facility,

 ## Let's write our first program

Open up a Text Editor and save a file with the extension ``.py``

## Program to ask the name, temperature, and rainfall of a place and print it

```python
"""
Program to ask the name, temperature, and rainfall of a place and print it.
"""

# This is a variable to save the place
place = input("Enter the name of the place:")

# Rainfall variable
rainfall = input("Enter the rainfall recorded today in mm:")

# Temperature variable
temperature = float(input("Enter the temperature recorded today in Celsius:"))

# Print statement
print("In ", place, " today it rained ", rainfall, " mm  and the temperature is", temperature, " degree celsius")
```
## Comments and Docstrings

Comment - Lines that are ignored when the program is run. Used for excluding codes and for including messages.
```python

# This is a single line comment
# Comment begins with a hash # symbol

```
Docstrings - Document strings. Multi-line comments. But more useful for including help/direction messages that appear when help utilities are called. In libraries, this is used as a documentation/help message for functions and classes.

```python
"""
    This is a Docstring. It starts and ends with 
    triple " or triple ' quotes. Mix and match does not work!
"""

'''
    This is also a DocString
'''
```

## Input Command

Input command - Used for getting input from user to a variable.
```python
n = input('Enter the value for n') # Dynamic input
n = float(input('Enter the value for n')) # Type casted input
```

* Dynamic input - that is, the function analyzes the data and assumes data type automatically.
* Explicit type casting (manually changing the data type) is used to control data types.