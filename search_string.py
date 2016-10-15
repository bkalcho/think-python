# Author: Bojan G. Kalicanin
# Date: 15-Oct-2016
# Search for a letter through the string

def find(word, letter, s):
    """Search for a letter in the string, starting from index s."""
    index = s
    while index < len(word):
        if word[index] == letter:
            return index
        index += 1
    return -1