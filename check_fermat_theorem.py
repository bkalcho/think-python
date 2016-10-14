# Author: Bojan G. Kalicanin
# Date: 14-Oct-2016
# Check if Fermat's Last Theorem holds

def check_fermat(a, b, c, n):
    """
    Function that checks if the Last Fermat Theorem holds.
    That means there are no positive integers a, b, c, such that
    a^n + b^n = c^n, for any values of n greater that 2.
    """
    if (n > 2) and (a**n + b**n == c**n):
        print("Holy smokes, Fermat was wrong!")
    elif not n > 2:
        print("Value of n must be integer greater than 2!")
    else:
        print("No, that doesn't work")

def prompt_user():
    """
    Prompt user to input values for a, b, c and n, and convert them
    to integers, and uses check_fermat to check whether they violate
    Fermat's theorem"""
    string = input("Input a, b, c, n? ")
    values = list(map(int, string.split()))
    check_fermat(values[0], values[1], values[2], values[3])


prompt_user()