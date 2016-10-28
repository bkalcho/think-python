# Author: Bojan G. Kalicanin
# Date: 28-Oct-2016
# Swampy (see Chapter 4) provides a module named World, which defines a
# userdefined type also called World. You can import it like this:
#       from swampy.World import World
# Or, depending on how you installed Swampy, like this:
#       from World import World
# The following code creates a World object and calls the mainloop
# method, which waits for the user.
#       world = World()
#       world.mainloop()
# A window should appear with a title bar and an empty square. We will
# use this window to draw Points, Rectangles and other shapes. Add the
# following lines before calling mainloop and run the program again.
# canvas = world.ca(width=500, height=500, background='white')
# bbox = [[-150,-100], [150, 100]]
# canvas.rectangle(bbox, outline='black', width=2, fill='green4')
# You should see a green rectangle with a black outline. The first line
# creates a Canvas, which appears in the window as a white square. The
# Canvas object provides methods like rectangle for drawing various
# shapes.
# bbox is a list of lists that represents the "bounding box" of the
# rectangle. The first pair of coordinates is the lower-left corner of
# the rectangle; the second pair is the upper-right corner.
# You can draw a circle like this:
#       canvas.circle([-25,0], 70, outline=None, fill='red')
# The first parameter is the coordinate pair for the center of the
# circle; the second parameter is the radius.
# If you add this line to the program, the result should resemble the
# national flag of Bangladesh (see
# http://en.wikipedia.org/wiki/Gallery_of_sovereign-state_flags).
#
# 1. Write a function called draw_rectangle that takes a Canvas and a
# Rectangle as arguments and draws a representation of the Rectangle on
# the Canvas.
# 2. Add an attribute named color to your Rectangle objects and modify
# draw_rectangle so that it uses the color attribute as the fill color.
# 3. Write a function called draw_point that takes a Canvas and a Point
# as arguments and draws a representation of the Point on the Canvas.
# 4. Define a new class called Circle with appropriate attributes and
# instantiate a few Circle objects. Write a function called draw_circle
# that draws circles on the canvas.
# 5. Write a program that draws the national flag of the Czech Republic.
# Hint: you can draw a polygon like this:
#       points = [[-150,-100], [150, 100], [150, -100]]
#       canvas.polygon(points, fill='blue')
# I have written a small program that lists the available colors; you
# can download it from http://thinkpython.com/code/color_list.py.

from swampy.World import World

class Rectangle(object):
    """Represents a rectangle."""
    def __init__(self, xl, yl, xu, yu, color):
        self.xl = xl
        self.yl = yl
        self.xu = xu
        self.yu = yu
        self.color = color

class Point(object):
    """Represents a point in 2-D space."""
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Circle(object):
    """Represent a circle in 2-D space."""
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

def draw_rectangle(can, rect):
    """Draw representation of the Rectangle on the Canvas."""
    canvas.rectangle([[rect.xl, rect.yl], [rect.xu, rect.yu]], outline='black',
        width=2, fill=rect.color)

def draw_point(can, p):
    """Draws representation of the Point on the canvas."""
    canvas.circle([p.x, p.y], r=0, outline='black', fill=None)

def draw_circle(can, c):
    """Draws representation of the Circle on the Canvas."""
    canvas.circle([c.x, c.y], c.r, outline='black', fill='red')

world = World()
canvas = world.ca(width=500, height=500, background='white')
#rectangle = Rectangle(-150, -100, 150, 100, 'green4')
#draw_rectangle(canvas, rectangle)

#p = Point(100, 100)
#draw_point(canvas, p)

c = Circle(20, 20, 25)
draw_circle(canvas, c)

world.mainloop()