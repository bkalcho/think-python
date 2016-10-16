# Author: Bojan G. Kalicanin
# Date: 16-Oct-2016
# Write a function called middle that takes a list and returns a new
# list that contains all but the first and last elements. So
# middle([1,2,3,4]) should return [2,3].

def middle(t):
    """
    Take a list and return a new list that contains all but the first
    and last elements.
    """
    return t[1:-1]
    
# Execute next tests only if it is called from the main program, not
# when imported as a module.
if __name__ == '__main__':
    a = [1, 2, 3, 4]
    print(middle(a))