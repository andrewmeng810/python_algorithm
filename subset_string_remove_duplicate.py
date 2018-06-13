#! usr/bin/env python 3


# For this function, we are subsetting strings (S) based on desired length (k).
# Given S and k, print n/k lines where each line i which unique stringsself.

# Sample input:
# 'AABCAAADA'

# Sample output:
# AB
# CA
# AD

# Solution 1
# if functions


def merge_the_tools(string, k):
    """ Evenly subseting string based on the subset length"""
    part_count = round(len(string) / k)
    div = len(string) % k
    # if function to determine if string length can be evenly divided by k
    if div == 0:
        part_list = [string[i * k: k(1 + i)] for i in range(part_count)]
        # initiate a set to remove duplicates and sorted by original index
        print('\n'.join(''.join(sorted(set(i), key= i.index)) for i in part_list))

    else:
        last_part = string[- div:]
        part_list = [string[i * k: i * k(1 + i)] for i in range(part_count)]
        part_list.append(last_part)

        print('\n'.join(''.join(sorted(set(i), key= i.index)) for i in part_list))

# merge_the_tools('AABCAAADA', 3)



# Soloution 2
# zip and iter function


def merge_the_tools(string, k):
    for part in zip(*[iter(string)] * k):
        d = dict()
        print(''.join([ d.setdefault(c, c) for c in part if c not in d ]))

# test
# merge_the_tools('AABCAAADA', 3)
