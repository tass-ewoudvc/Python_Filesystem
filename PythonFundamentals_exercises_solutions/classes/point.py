#!/usr/bin/env python3

'''
Tass PythonFundamentals course
Solution to: Point class
'''

class Point:
    '''Class representing an x,y point'''

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "Point({},{})".format(self.x, self.y)

    def distance(self, other):
        '''Calculates the distance between 2 points'''
        print("Distance: {},{}".format(self.x-other.x, self.y-other.y))


p1 = Point(10,10)
p2 = Point(0,0)
print(p1)
print(p2)

p1.distance(p2)


