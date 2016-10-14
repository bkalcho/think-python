# Author: Bojan G. Kalicanin
# Date: 14-Oct-2016
# Ackermann function

def ack(m, n):
    """Function that realize Ackermann function."""
    if m == 0:
        return n + 1
    elif (m > 0) and (n == 0):
        return ack(m - 1, 1)
    elif (m > 0) and (n > 0):
        return ack(m - 1, ack(m, n - 1))
        
        
if __name__ == '__main__':
    # Tests ack function for some example values
    a = ack(3, 4)
    print(a)