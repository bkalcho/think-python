# Author: Bojan G. Kalicanin
# Date: 14-Oct-2016
# Palindrome

def first(word):
    return word[0]
    
def last(word):
    return word[-1]
    
def middle(word):
    return word[1:-1]
    
def is_palindrome(word):
    if word == word[::-1]:
        return True
    else:
        return False
    #if len(word) <= 1:
    #    return True
    #elif first(word) != last(word):
    #    return False
    #return is_palindrome(middle(word))
    
if __name__ == '__main__':
    # test previous functions
    print(first('example'))
    print(last('example'))
    print(middle('tw'))
    print(middle('t'))
    print(middle(''))
    print(is_palindrome('example'))
    print(is_palindrome('noon'))
    print(is_palindrome('redivider'))