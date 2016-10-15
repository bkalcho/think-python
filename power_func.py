# Author: Bojan G. Kalicanin
# Date: 15-Oct-2016
# Power function

def is_power(a, b):
    """Function that checks if a is power of b."""
    if a == b:
        return True
    elif a % b != 0:
        return False
    return is_power(a/b, b)
    

# Run only if a module is called from main program. If it is imported
# do not run test cases
if __name__ == '__main__':
    # Test cases for is_power function
    a = is_power(8, 2)
    b = is_power(7, 3)
    c = is_power(11, 11)
    print(a, b, c)