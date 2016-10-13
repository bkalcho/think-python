# Author: Bojan G. Kalicanin
# Date: 13-Oct-2016
# Set of functions for drawing flowers

try:
    from swampy.TurtleWorld import *
except ImportError:
    from TurtleWorld import *

from drawing_basic_shapes import *

def flower_petal(t, r, angle):
    for i in range(2):
        arc(t, r, angle)
        lt(t, 180 - angle)

def flower(t, r, angle, n):
    for i in range(n):
        flower_petal(t, r, angle)
        lt(t, 360 / n)

def move(t, length):
    """Move t forward length without leaving a trail"""
    pu(t)
    fd(t, length)
    pd(t)

world = TurtleWorld()
bob = Turtle()
bob.delay = 0.01

move(bob, -100)
flower(bob, 30, 60, 7)

move(bob, 100)
flower(bob, 30, 60, 10)

move(bob, 100)
flower(bob, 30, 60, 20)

die(bob)


wait_for_user()