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
palindromes = {} # location : sequence
for i in range(len(sequence)):
    for j in range(4,13):
        for found in re.finditer(r"(?=([ATCG]{" + str(j) + r"}))", sequence[i:]):
            s = found.group(1)
            if reverse_complement(s) == s:
                if found.start(1)+i+1 not in palindromes:
                    palindromes[found.start(1)+i+1] = s
                elif found.start(1)+i+1 in palindromes and len(s) > len(palindromes[found.start(1)+i+1]):
                    palindromes[found.start(1)+i+1] = s

#for j in range(4,13):
#    for found in re.finditer(r"(?=([ATCG]{" + str(j) + r"}))", sequence):
#        s = found.group(1)
#        if reverse_complement(s) == s:
#            if found.start(1)+1 not in palindromes:
#                palindromes[found.start(1)+1] = s
#            elif found.start(1)+1 in palindromes and len(s) > len(palindromes[found.start(1)+1]):
#                palindromes[found.start(1)+1] = s

# sort items by start location
palindromes = {k: v for k, v in sorted(palindromes.items(), key=lambda item: item[0])}
# print palindromes
for k,v in palindromes.items():
    print(f"{k} {len(v)}")
