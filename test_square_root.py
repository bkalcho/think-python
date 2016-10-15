# Author: Bojan G. Kalicanin
# Date: 15-Oct-2016
# Program that test Newton's method of calculation of square root.

import square_roots as sr
import math

def test_square_root(n):
    """Function that tests square root calculation by Newton's method"""
    a = 1.0
    while a < n:
        b = sr.newton_root(a)
        b = round(b, 11)
        c = math.sqrt(a)
        c = round(c, 11)
        string = "{0:.1f} {1:.11f} {2:.11f} {3:.11e}"
        print(string.format(a, b, c, b - c))
        a += 1.0
        
test_square_root(10)