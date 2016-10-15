# Author: Bojan G. Kalicanin
# Date: 15-Oct-2016
# Estimate pi by using Ramanujan's infinite series formula

import math
def estimate_pi():
    k = 0
    s = 0
    t = 1
    while t > 1e-15:
        a = (math.factorial(4*k) * (1103 + 26390*k))
        b = (math.factorial(k))**4 * 396**(4*k)
        t = a/b
        s += t
        k += 1
    m = 2 * math.sqrt(2) / 9801
    approx = 1 / (m * s)
    return approx
    
pi_approx = estimate_pi()
print("Approximation of pi: " + str(pi_approx))
delta = pi_approx - math.pi
print("Absolute difference: " + str(delta))