# Author: Bojan G. Kalicanin
# Date: 16-Oct-2016
# Two words are anagrams if you can rearrange the letters from one to
# spell the other. Write a function called is_anagram that takes two
# strings and returns True if they are anagrams.

def is_anagram(t, s):
    """Take two strings and check if they are anagrams."""
    t_list = list(t)
    s_list = list(s)
    for i in t_list:
        if i not in s_list:
            return False
        else:
            s_list.remove(i)
    return True
    
    
if __name__ == '__main__':
    print(is_anagram('cinema', 'iceman'))
    print(is_anagram('man', 'arm'))