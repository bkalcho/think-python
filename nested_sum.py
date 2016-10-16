# Author: Bojan G. Kalicanin
# Date: 16-Oct-2016
# Add up the elements from all nested lists

def nested_sum(numbers):
    """Add up all the elements from nested lists."""
    total = 0
    for number in numbers:
        total += sum(number)
    print(total)
    

if __name__ =='__main__':
    a = [[1, 2, 3], [78, 109], [123, 453, 12, 100]]
    nested_sum(a)