# Author: Bojan G. Kalicanin
# Date: 13-Oct-2016
# Write a function called square that takes a parameter named t, which
# is a turtle. It should use the turtle to draw a square. Write a
# function call that passes bob as an argument to square, and then run
# the program again.

import TurtleWorld as tw
import math

def square(t, length):
    """Write square with a turtle."""

    for i in range(4):
        tw.fd(t, length)
        tw.lt(t)

def polyline(t, n, length, angle):
    for i in range(n):
        tw.fd(t, length)
        tw.lt(t, angle)

def polygon(t, length, n):
    """Write polzgon of n sides, where each side is n in length."""
    angle = 360 / n

    polyline(t, n, length, angle)

def circle(t, r):
    """Write a circle with an radius r."""
    arc(t, r, 360)

def arc(t, r, angle):
    """
    Write part of the circle, with radius r and part which is
    distinguished by the angle in degrees.
    """ 
    arc_length = 2 * math.pi * r * angle / 360
    n = int(arc_length / 3) + 1
    step_length = arc_length / n
    step_angle = angle / n
    polyline(t, n, step_length, step_angle)


world = tw.TurtleWorld()
bob = tw.Turtle()
bob.delay = 0.01
arc(bob, 50, 60)

tw.wait_for_user()