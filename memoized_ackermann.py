# Author: Bojan G. Kalicanin
# Date: 17-Oct-2016
# Memoize the Ackermann function from Exercise 6.5 and see if
# memoization makes it possible to evaluate the function with bigger
# arguments.

cache = {}
def memoized_ackermann(m, n):
    if m == 0:
        return n + 1
    if n == 0:
        return ack(m - 1, 1)
    try:
        return cache[m, n]
    except KeyError:
        cache[m, n] = ack(m - 1, ack(m, n - 1))
        return cache[m, n]