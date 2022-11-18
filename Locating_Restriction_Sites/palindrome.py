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
for j in range(4,13):
    for found in re.finditer(r"(?=([ATCG]{" + str(j) + r"}))", sequence):
        s = found.group(1)
        if reverse_complement(s) == s:
            print(f"{found.start(1)+1} {len(s)}")
