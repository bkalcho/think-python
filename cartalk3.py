# Author: Bojan G. Kalicanin
# Date: 16-Oct-2016
# "Recently I had a visit with my mom and we realized that the two
# digits that make up my age when reversed resulted in her age.
# For example, if she's 73, I'm 37. We wondered how often this has
# happened over the years but we got sidetracked with other topics and
# we never came up with an answer.
# "When I got home I figured out that the digits of our ages have been
# reversible six times so far. I also figured out that if we're lucky it
# would happen again in a few years, and if we're really lucky it would
# happen one more time after that. In other words, it would have
# happened 8 times over all. So the question is, how old am I now?"

def str_fill(i, len):
    """Return the integer of the length of at least len digits"""
    return str(i).zfill(len)


def are_reversed(i, j):
    """
    Return True if the integers i and j, when written as strings,
    are the reverse of each other
    """
    return str_fill(i,2) == str_fill(j,2)[::-1]


def num_instances(diff, flag=False):
    """
    Returns the number of times the mother and daughter have
    pallindromic ages in their lives, given the difference in age.
    If flag==True, prints the details.
    """
    daughter = 0
    count = 0
    while True:
        mother = daughter + diff
        if are_reversed(daughter, mother) or are_reversed(daughter, mother+1):
            count += 1
            if flag:
                print(daughter, mother)
        if mother > 120:
            break
        daughter = daughter + 1
    return count


def check_diffs():
    """
    Enumerate the possible differences in age between mother
    and daughter, and for each difference, count the number of times
    over their lives they will have ages that are the reverse of
    each other.
    """
    diff = 10
    while diff < 70:
        n = num_instances(diff)
        if n > 0:
            print(diff, n)
        diff = diff + 1
        
check_diffs()
num_instances(18, True)