# Author: Bojan G. Kalicanin
# Date: 27-Oct-2016
# Solution to the exercises 15.1 to 15.3

import copy
import math

class Point(object):
    """Represent a point in 2-D space."""
    
    def __init__(self, x, y):
        """Initializing attributes of the class Point."""
        self.x = x
        self.y = y
        
class Rectangle(object):
    """Represent a rectangle.
    
    attributes: width, height, corner.
    """
    def __init__(self, width, height, corner):
        """Initializing attributes of the class Rectangle."""
        self.width = width
        self.height = height
        self.corner = Point(corner.x, corner.y)

def distance_between_points(p1, p2):
    """Calculates distance between two points."""
    d = math.sqrt((p2.x - p1.x)**2 + (p2.y-p1.y)**2)
    return d
    
def find_center(rect):
    """Calculate the center of the rectangle."""
    x = rect.corner.x + rect.width/2.0
    y = rect.corner.y + rect.height/2.0
    p = Point(x, y)
    return p

def grow_rectangle(rect, dwidth, dheight):
    rect.width += dwidth
    rect.height += dheight
    
def move_rectangle(rect, dx, dy):
    rect.corner.x += dx
    rect.corner.y += dy
    
def move_rectangle_ver2(rect, dx, dy):
    rect2 = copy.deepcopy(rect)
    rect2.corner.x += dx
    rect2.corner.y += dy


point1 = Point(3.0, 4.2)
point2 = Point(8.4, 2.3)
dist = distance_between_points(point1, point2)
print("{0:.3g}".format(dist))

point3 = Point(0.0, 0.0)
box = Rectangle(100.0, 200.0, point3)
print(box.corner.x, box.corner.y, box.width, box.height)
center = find_center(box)
print(center.x, center.y)

move_rectangle(box, 2.1, 4.1)
print(box.corner.x, box.corner.y, box.width, box.height)