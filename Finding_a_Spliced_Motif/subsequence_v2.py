#!/usr/bin/env python

import sys

# read in file
seq = ""
subseq = ""
i = 0
with open(sys.argv[1],"r") as fasta:
    for line in fasta:
        line = line.rstrip()
        if line[0] == ">":
            i += 1
        if i == 1 and line[0] != ">":
            seq += line
        if i == 2 and line[0] != ">":
            subseq += line

# find subsequence locations
i = 0
for NT in subseq:
    i = i + seq[i:].index(NT) + 1
    print(i, end = " ")
