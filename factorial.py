# Author: Bojan G. Kalicanin
# Date: 14-Oct-2016
# Factorial

def factorial(n):
    """Function that computes factorial of n."""
    if not isinstance(n, int):
        print("Factorial is only defined for integers.")
        return None
    elif n < 0:
        print("Factorial is not defined for negative integers")
        return None
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)
        
        
if __name__ == '__main__':
    # Test for some values
    a = factorial(20)
    b = factorial(0)
    print(a, b)