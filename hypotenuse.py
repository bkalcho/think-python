# Author: Bojan G. Kalicanin
# Date: 14-Oct-2016
# Return the length of the hypotenuse of the right triangle if the
# lengths of the legs are already known.

import math

def hypotenuse(a, b):
    """Returns the length of the hypotenuse of the right triangle."""
    c = math.sqrt(a**2 + b**2)
    return c