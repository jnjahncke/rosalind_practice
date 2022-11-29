#!/usr/bin/env python

import sys

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

# calculate As next to Us and Gs next to Cs
AU = 0
GC = 0
for i in range(len(seq)-1):
    if seq[i] == "G" and seq[i+1] == "C":
        GC += 1
    elif seq[i] == "C" and seq[i+1] == "G":
        GC += 1
    elif seq[i] == "A" and seq[i+1] == "U":
        AU += 1
    elif seq[i] == "U" and seq[i+1] == "A":
        AU += 1

# calculate matches
matchAU = 1
x = 1
term = (2*A) - x
while term > 1:
    term = (2*A) - x
    matchAU = matchAU * term
    x = x+2

matchGC = 1
x = 1
term = (2*G) - x
while term > 1:
    term = (2*G) - x
    matchGC = matchGC * term
    x = x+2

print(matchAU + matchGC - (2*AU) - (2*GC))
