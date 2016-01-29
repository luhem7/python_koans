#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.


# triangle(a, b, c) analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    #Raises TriangleError if the given side lengths are invalid

    if (a <= 0 or b <= 0 or c <= 0) or ( a > (b+c) or b > (a+c) or c > (a+b) ) : #one of the sides is greater than the sum of the lengths of the other two sides
        raise TriangleError
    
    mySetLength = len({a,b,c})
    if mySetLength == 3: return 'scalene'
    elif mySetLength == 2: return 'isosceles'
    else : return 'equilateral'


# Error class used in part 2.  No need to change this code.
class TriangleError(StandardError):
    pass
