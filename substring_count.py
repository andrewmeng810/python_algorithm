#!/usr/bin/env python 3

# For this function: we are tring to find the count for the substring
# of the given string

# For example,
# string = 'AASBSKSBS'
# substring = 'SBS'

# the function should return count of substring, which is 2


# solution 1:
# while statement:
#
def substring_count(string, substring):
    start, end, counter, s_len = 0, 0 , 0, len(substring)
    while end <= len(string):
        if substring == string[start: end]:
            counter += 1
        start += 1
        end = start + s_len
    return counter


# test
# string = 'AASBSKSBS'
# substring = 'SBS'
# print(substring_count(string, substring))


# solution 2:

# list statement

print(sum([ 1 for i in range(len(string) - len(substring) + 1) if substring == string[i: i + len(substring)]]))

# test
# string = 'AASBSKSBS'
# substring = 'SBS'
# print(sum([ 1 for i in range(len(string) - len(substring) + 1) if substring == string[i: i + len(substring)]]))
