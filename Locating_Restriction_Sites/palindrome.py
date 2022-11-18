#!/usr/bin/env python

import sys
import re

def reverse_complement(sequence):
    sequence = sequence.lower()
    rev = sequence.replace("a","T").replace("t","A").replace("c","G").replace("g","C")[::-1]
    return(rev)

inputfile = sys.argv[1]

# import sequence
sequence = ""
with open(inputfile,"r") as inputfile:
    for line in inputfile:
        line = line.rstrip()
        if line[0] != ">":
            sequence += line

# scan through sequence looking for reverse palindromes
palindromes = []
for j in range(4,13):
    for found in re.finditer(r"(?=([ATCG]{" + str(j) + r"}))", sequence):
        s = found.group(1)
        if reverse_complement(s) == s:
            palindromes.append((found.start(1)+1, len(s))) # location, length

# sort by location and print to standard out
palindromes = sorted(palindromes)
for item in palindromes:
    print(item[0],item[1])
