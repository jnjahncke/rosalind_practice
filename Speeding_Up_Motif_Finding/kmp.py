#!/usr/bin/env python

import sys

# import sequence
seq = ""
with open(sys.argv[1],"r") as fasta:
    for line in fasta:
        line = line.rstrip()
        if line[0] != ">":
            seq += line

array = [0] * len(seq)
k = 0
for i in range(2, len(seq) + 1):
    while k > 0 and seq[k] != seq[i-1]:
        k = array[k-1]
    if seq[k] == seq[i-1]:
        k += 1
    array[i-1] = k

print(*array, sep = " ")
