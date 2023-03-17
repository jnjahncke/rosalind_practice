#!/usr/bin/env python

import sys

memo = {}
def motz(seq):
    if len(seq) == 0 or len(seq) == 1:
        return 1

    if seq in memo:
        return memo[seq]

    memo[seq] = motz(seq[1:])
    for i in range(1, len(seq)):
        if ((seq[0] == 'A' and seq[i] == 'U') or
            (seq[0] == 'U' and seq[i] == 'A') or
            (seq[0] == 'C' and seq[i] == 'G') or
            (seq[0] == 'G' and seq[i] == 'C')):
            memo[seq] += motz(seq[1:i]) * motz(seq[i+1:])
            memo[seq] %= 10**6
    return memo[seq]

# Read the input RNA string from a file
rna = ""
with open(sys.argv[1],"r") as fasta:
    for line in fasta:
        line = line.rstrip()
        if line[0] != ">":
            rna += line

# Count the noncrossing matchings and print the result modulo 1,000,000
print(motz(rna))
