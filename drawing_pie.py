import math

try:
    from swampy.TurtleWorld import *
except ImportError:
    from TurtleWorld import *

def draw_pie(t, n, r):
    polypie(t, n, r)
    pu(t)
    fd(t, r*2 + 10)
    pd(t)

    
def polypie(t, n, r):
    angle = 360 / n
    for i in range(n):
        isosceles(t, r, angle/2)
        lt(t, angle)


def isosceles(t, r, angle):
    y = r * math.sin(angle * math.pi / 180)

    rt(t, angle)
    fd(t, r)
    lt(t, 90+angle)
    fd(t, 2*y)
    lt(t, 90+angle)
    fd(t, r)
    lt(t, 180-angle)


# create the world and bob
world = TurtleWorld()
bob = Turtle()
bob.delay = 0
pu(bob)
bk(bob, 130)
pd(bob)

# draw polypies with various number of sides
size = 40
draw_pie(bob, 5, size)
draw_pie(bob, 6, size)
draw_pie(bob, 7, size)
draw_pie(bob, 8, size)
die(bob)

wait_for_user()