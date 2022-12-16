#!/usr/bin/env python

import sys
from itertools import product 
from re import finditer

# import sequence
with open(sys.argv[1],"r") as fasta:
    for line in fasta:
        line = line.rstrip()
        if line[0] == ">":
            seq = ""
        else:
            seq += line

# make all possible 4-mers
kmers = ["".join(x) for x in product("ACGT", repeat=4)]

# find mers, build array
array = []
for kmer in kmers:
    array.append([found.group(1) for found in finditer(r"(?=(" + kmer + "))", seq)])
print(*[len(x) for x in array], sep = " ")
