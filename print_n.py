# Author: Bojan G. Kalicanin
# Date: 15-Oct-2016
# Print something n times

def print_n(text, n):
    """Print some text n times."""
    while n > 0:
        print(text)
        n -= 1


if __name__ == '__main__':
    print_n("example", 7)