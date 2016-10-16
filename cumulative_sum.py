# Author: Bojan G. Kalicanin
# Date: 16-Oct-2016
# Return the cumulative sum of the elements.

def cumulative_sum(t):
    """Take a list and return the cumulative sum."""
    res = []
    total = 0
    for i in range(len(t)):
        res.append(sum(t[:i + 1]))
    return res
        
        
if __name__ == '__main__':
    a = [1, 2, 3]
    print(cumulative_sum(a))