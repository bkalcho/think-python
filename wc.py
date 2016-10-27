# Author: Bojan G. Kalicanin
# Date: 27-Oct-2016
# Type this example into a file named wc.py and run it as a script. Then
# run the Python interpreter and import wc. What is the value of
# __name__ when the module is being imported?
# Warning: If you import a module that has already been imported, Python
# does nothing. It does not re-read the file, even if it has changed.
# If you want to reload a module, you can use the built-in function
# reload, but it can be tricky, so the safest thing to do is restart the
# interpreter and then import the module again.


def linecount(filename):
    count = 0
    for line in open(filename):
        count += 1
    return count

print(__name__)
if __name__ == '__main__':
    print(linecount('wc.py'))