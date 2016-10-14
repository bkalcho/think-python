# Author: Bojan G. Kalicanin
# Date: 14-Oct-2016
# Calculate distance between two points

import math

def distance(x1, y1, x2, y2):
    """Calculate distance between points (x1, y1) and (x2, y2)."""
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)