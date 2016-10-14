# Author: Bojan G. Kalicanin
# Date: 14-Oct-2016
# Fibonacci array

def fibonacci(n):
    """Function that calculates Fibonacci array."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
        
        
if __name__ == '__main__':
    # Test fibonacci function for some example n.
    a = fibonacci(1)
    b = fibonacci(20)
    print(a, b)