#!/usr/bin/env python

import sys
from itertools import product 
import re

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

# find meirs, build array
array = []
for kmer in kmers:
    temp = [found.group(1) for found in re.finditer(r"(?=(" + kmer + "))", seq)]
    array.append(len(temp))
print(*array, sep = " ")
