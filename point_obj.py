# Author: Bojan G. Kalicanin
# Date: 29-Oct-2016
# 1. Write an init method for the Point class that takes x and y as
# optional parameters and assigns them to the corresponding attributes.
# 2. Write a str method for the Point class. Create a Point object and 
# print it.
# 3. Write an add method for the Point class.
# 4. Write an add method for Points that works with either a Point
# object or a tuple.

class Point(object):
    """Represents a point in a 2-D world."""
    
    def __init__(self, x=0, y=0):
        """Initialization of the class attributes at instantiation."""
        self.x = x
        self.y = y
        
    def __str__(self):
        """String representation of the object, used when printing."""
        return "({0:.2f}, {1:.2f})".format(self.x, self.y)
        
    def __add__(self, other):
        """Addition operator overloading."""
        if isinstance(other, Point):
            return self.adding_points(other)
        else:
            return self.adding_tuple(other)
    
    def __radd__(self, other):
        """Right side addition."""
        return self.__add__(other)
            
    def adding_points(self, other):
        """Method for adding two points."""
        sum = Point()
        sum.x = self.x + other.x
        sum.y = self.y + other.y
        return sum
        
    def adding_tuple(self, other):
        """Adding point to the point represented by tuple."""
        sum = Point()
        sum.x = self.x + other[0]
        sum.y = self.y + other[1]
        return sum
    
        
point = Point(2.3456, 3.48793)
print(point)