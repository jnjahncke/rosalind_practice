#!/usr/bin/env python

import sys
from math import factorial

fasta = sys.argv[1]

# import sequence
with open(fasta,"r") as fasta:
    seq = ""
    for line in fasta:
        if line[0] == ">":
            continue
        else:
            seq += line

# count As, count Gs
A = seq.count("A")
G = seq.count("G")

print(factorial(A) * factorial(G))
