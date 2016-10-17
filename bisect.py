# Author: Bojan G. Kalicanin
# Date: 17-Oct-2016
# To check whether a word is in the word list, you could use the in
# operator, but it would be slow because it searches through the words
# in order.
# Because the words are in alphabetical order, we can speed things up
# with a bisection search (also known as binary search), which is
# similar to what you do when you look a word up in the dictionary. You
# start in the middle and check to see whether the word you are looking
# for comes before the word in the middle of the list. If so, then you
# search the first half of the list the same way. Otherwise you search
# the second half.
# Either way, you cut the remaining search space in half. If the word
# list has 113,809 words, it will take about 17 steps to find the word
# or conclude that it's not there.
# Write a function called bisect that takes a sorted list and a target
# value and returns the index of the value in the list, if its there, or
# None if it's not.

def bisect(t, word):
    """
    Function that takes a sorted list (t) and a target value (word) and
    returns the index of the value in the list, if its there, or None if
    it's not.
    """
    lower = 0
    upper = len(t) - 1
    middle = (lower + upper) // 2
    while word != t[middle] and lower <= upper:
        if word < t[middle]:
            upper = middle - 1
        else:
            lower = middle + 1
        middle = (upper + lower) // 2
    if word == t[middle]:
        return middle
    return None


# Test function if called from main program, if imported do not execute
# test
if __name__ == '__main__':
    t = []
    f_obj = open('words.txt')
    for line in f_obj:
        w = line.strip()
        t.append(w)
    f_obj.close()
    result = bisect(t, 'aba')
    if result:
        print("The index of the matched value '" + t[result] + \
            "' is: " + str(result))
    else:
        print("Targeted word is not in the list!")