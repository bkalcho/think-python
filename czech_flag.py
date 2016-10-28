# Author: Bojan G. Kalicanin
# Date: 28-Oct-2016
# Write a program that draws the national flag of the Czech Republic.
# Hint: you can draw a polygon like this:
#       points = [[-150,-100], [150, 100], [150, -100]]
#       canvas.polygon(points, fill='blue')

from swampy.World import World

world = World()
canvas = world.ca(width=500, height=500, background='white')
points1 = [[-150,-100], [-150, 100], [0, 0]]
canvas.polygon(points1, fill='MidnightBlue')
points2 = [[0, 0], [-150, 100], [200, 100], [200, 0]]
canvas.polygon(points2, fill='white')
points3 = [[0, 0], [-150, -100], [200, -100], [200, 0]]
canvas.polygon(points3, fill='red')

world.mainloop()