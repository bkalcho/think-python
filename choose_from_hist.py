# Author: Bojan G. Kalicanin
# Date: 19-Oct-2016
# Write a function named choose_from_hist that takes a histogram as
# defined in Section 11.1 and returns a random value from the histogram,
# chosen with probability in proportion to frequency.

import random
import histogram

def choose_from_hist(h):
    """
    Take histogram and return a random value from histogram, choosen
    with probability in proportion to frequency.
    """
    r = random.uniform(0, 1)
    s = 0
    for v in h.values():
        s += v
    d = {}
    for k, v in h.items():
        d[k] = v/s
    cumulative_probability = 0
    for k, v in d.items():
        cumulative_probability += v
        if r < cumulative_probability:
            break
    return k
            

s = 'banana'
h = histogram.histogram(s)
print(h)
r = choose_from_hist(h)
print(r)