# Author: Bojan G. Kalicanin
# Date: 14-Oct-2016
# If any of the three lengths is greater than the sum of the other two,
# then you cannot form a triangle. Otherwise, you can. (If the sum of
# two lengths equals the third, they form what is called a “degenerate”
# triangle.)

def is_triangle(a, b, c):
    """"
    Take three integer arguments, and check whether they can form
    triangle or not.
    """
    if (a > b + c) or (b > a + c) or (c > a + b):
        print("No")
    else:
        print("Yes")

def prompt_user():
    """
    Prompts user to enter stick lengths, and check if they can form
    a triangle.
    """
    str_values = input("Enter lengths of the stics, a, b, c: ")
    values = list(map(int, str_values.split()))
    is_triangle(values[0], values[1], values[2])


prompt_user()