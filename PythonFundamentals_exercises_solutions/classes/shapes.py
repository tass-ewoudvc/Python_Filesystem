#!/usr/bin/env python3
'''
Tass PythonFundamentals course
Solution to: Classic shapes
'''
import math

class Square:
    '''Class representation of a Square'''

    def __init__(self, side):
        '''Constructor for shape objects
        Takes a side as argument
        '''
        self.side = side

    def getSurfaceArea(self):
        '''Computes the surface are of the Square,
        based on the 'side' member
        '''
        return self.side**2

    def getType(self):
        '''Returns the type in a str object'''
        return 'Square'


class Circle:
    '''Class representation of a Circle'''

    def __init__(self, radius):
        '''Constructor for Circle objects
        Takes radius as argument
        '''
        self.radius = radius

    def getSurfaceArea(self):
        '''Computes the surface of the Circle,
        based on the 'radius' member
        '''
        return math.pi * self.radius**2

    def getType(self):
        '''Returns the type in str object'''
        return 'Circle'
        


def printSurfaceAreaOfObject(object):
    '''Print a line, regardless of the actual type of object'''
    print("Surface area of this {} is {}".format(object.getType(), object.getSurfaceArea()))


s1 = Square(10)
s2 = Square(7)

c1 = Circle(10)
c2 = Circle(7)

printSurfaceAreaOfObject(s1)
printSurfaceAreaOfObject(s2)
printSurfaceAreaOfObject(c1)
printSurfaceAreaOfObject(c2)
