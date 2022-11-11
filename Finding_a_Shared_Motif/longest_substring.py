#!/usr/bin/env python

import sys

# checks if a certain substring is in all strings
def is_substr(substr, strings):
    for string in strings:
        if substr not in string:
            return(False)
    return(True)

# finds longest substring present in all strings
def long_substr(strings):
    substr = ""
    shortest = min(strings, key = len)
    sh_length = len(shortest)
    # loop through each NT of the shortest sequence
    for i in range(sh_length):
        # compare current NT to the following NTs,
        # build up subst as long as it is in all strings
        for j in range(sh_length-i+1):
            if j > len(substr) and is_substr(shortest[i:i+j], strings):
                substr = shortest[i:i+j]
    return(substr)

# read in strings
inputfile = sys.argv[1]
string_dict = {}
with open(inputfile,"r") as inputfile:
    for line in inputfile:
        line = line.rstrip()
        if line[0] == ">":
            seq_name = line[1:]
            string_dict[seq_name] = ""
        else:
            string_dict[seq_name] += line

strings = list(string_dict.values())
print(long_substr(strings))
