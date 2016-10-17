# Author: Bojan G. Kalicanin
# Date: 17-Oct-2016
# Run this version of fibonacci and the original with a range of
# parameters and compare their run times.

import time
import fibonacci as fb

known = {0:0, 1:1}

def fibonacci(n):
    if n in known:
        return known[n]
    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res

n = [1, 3, 10, 25, 30, 35]
for i in n:
    start_time = time.time()
    f = fb.fibonacci(i)
    end_time = time.time() - start_time
    print(f, end_time)

for i in n:
    start_time = time.time()
    f = fibonacci(i)
    end_time = time.time() - start_time
    print(f, end_time)