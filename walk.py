# Author: Bojan G. Kalicanin
# Date: 25-Oct-2016
# The os module provides a function called walk that is similar to this
# one but more versatile. Read the documentation and use it to print the
# names of the files in a given directory and its subdirectories.

import os

def walkdirs(dirname):
    """
    Print the names of all files in the dirname and its subdirectories.
    """
    for root, dirs, files in os.walk(dirname):
        for filename in files:
            print(os.path.join(root, filename))

if __name__ == '__main__':
    walkdirs('.')