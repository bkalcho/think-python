# Author: Bojan G. Kalicanin
# Date: 26-Oct-2016
# Greatest Common Divisor (GCD)

def gcd(a, b):
    """Function that calculates GCD (Greatest Common Divisor)"""
    r = a % b
    if b == 1:
        return 1
    elif r == 0:
        return b
    return gcd(b, r)
    
    
if __name__ == '__main__':
    # Test cases for gcd function
    a = gcd(24, 16)
    b = gcd(128, 32)
    c = gcd(100, 13)
    print(a, b, c)