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
positions = []
start = 0
for NT in subseq:
    loc = seq.find(NT)
    positions.append(loc + start + 1)
    seq = seq[loc+1:]
    start += loc + 1

print(*positions, sep = " ")
