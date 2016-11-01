# Author: Bojan G. Kalicanin
# Date: 01-Oct-2016
# This exercise is a cautionary tale about one of the most common, and
# difficult to find, errors in Python. Write a definition for a class
# named Kangaroo with the following methods:
# 1. An __init__ method that initializes an attribute named
#    pouch_contents to an empty list.
# 2. A method named put_in_pouch that takes an object of any type and
#    adds it to pouch_contents.
# 3. A __str__ method that returns a string representation of the
#    Kangaroo object and the contents of the pouch.
# Test your code by creating two Kangaroo objects, assigning them to
# variables named kanga and roo, and then adding roo to the contents of
# kanga's pouch.

class Kangaroo(object):
    """Example class named Kangaroo."""
    def __init__(self, contents=None):
        """Initialize class attributes."""
        if contents == None:
            contents = []
        self.pouch_contents = contents

    def put_in_pouch(self, t):
        self.pouch_contents.append(t)

    def __str__(self):
        t =[object.__str__(self) + ' with pouch contents:']
        for obj in self.pouch_contents:
            s = '   ' + object.__str__(obj)
            t.append(s)
        return '\n'.join(t)


if __name__ == '__main__':
    kanga = Kangaroo()
    roo = Kangaroo()
    kanga.put_in_pouch('wallet')
    kanga.put_in_pouch('car keys')
    kanga.put_in_pouch(roo)
    print(kanga)
    print(roo)