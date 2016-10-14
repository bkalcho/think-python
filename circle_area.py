# Author: Bojan G. Kalicanin
# Date: 14-Oct-2016
# Compute the radius and area of the circle

import math as m
import points_distance as pd
import hypotenuse as h

def area(radius):
    area = m.pi() * radius**2
    return area

def circle_area(xc, yc, xp, yp):
    """Computes circle area."""
    radius = pd.distance(xc, yc, xp, yp)
    result = area(radius)
    return result