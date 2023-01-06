#!/usr/bin/env python

import sys
from math import factorial

# import sequence
seq = ""
with open(sys.argv[1],"r") as fasta:
    for line in fasta:
        line = line.rstrip()
        if line[0] != ">":
            seq += line

# count NTs
A = seq.count("A")
U = seq.count("U")
G = seq.count("G")
C = seq.count("C")

AU = [A, U]
GC = [G, C]

# calculate matchings
term1 = factorial(max(AU)) // factorial(max(AU) - min(AU))
term2 = factorial(max(GC)) // factorial(max(GC) - min(GC))

print(int(term1 * term2))
