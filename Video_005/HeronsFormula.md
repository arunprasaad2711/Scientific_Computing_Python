# Introduction to Scientific Computation Using Python

by [Arun Prasaad Gunasekaran](https://arunprasaad2711.github.io)

Video 5 : Area of a Triangle using Heron Formula.

## Table of Contents
<!-- TOC -->

- [Introduction to Scientific Computation Using Python](#introduction-to-scientific-computation-using-python)
  - [Table of Contents](#table-of-contents)
  - [Area of a Triangle](#area-of-a-triangle)
  - [Interactive animation using Geogebra](#interactive-animation-using-geogebra)
  - [Program](#program)
  - [Output](#output)

<!-- /TOC -->

## Area of a Triangle

A triangle has many formulae to find its area. One formulae that involves only the sides of the triangle is the Heron's formula or the Hero's formula.

If $a$, $b$, and $c$ are the sides of a triangle ABC, then the area of the triangle $\Delta$ is given by

$$\Delta = \sqrt{s(s-a)(s-b)(s-c)}$$

where $s = \displaystyle{\frac{a + b + c}{2}}$ is the semi-perimeter of the triangle.

## Interactive animation using Geogebra

<iframe scrolling="no" title="TaylorSeries_Demo" src="https://www.geogebra.org/material/iframe/id/n4pxcth2/width/1366/height/687/border/888888/sfsb/true/smb/false/stb/false/stbh/false/ai/false/asb/false/sri/false/rc/false/ld/false/sdz/false/ctl/false" width="100%" height="400px" style="border:0px;"> </iframe>

## Program

```python
'''
Program to calculate the area of a triangle using Heron's formulae
'''

# Get inputs
a = float(input("Enter the side 'a' of the triangle:"))
b = float(input("Enter the side 'b' of the triangle:"))
c = float(input("Enter the side 'c' of the triangle:"))

# Calculate the semi-perimeter
s = (a + b + c)*0.5

# Find the Area
Area = (s*(s-a)*(s-b)*(s-c))**0.5

# Print the result
print("The area of the triangle with sides a = {}, b = {}, and c = {} is {}".format(a, b, c, Area))
```

## Output
```
Enter the side 'a' of the triangle:3
Enter the side 'b' of the triangle:4
Enter the side 'c' of the triangle:5
The area of the triangle with sides a = 3.0, b = 4.0, and c = 5.0 is 6.0
```