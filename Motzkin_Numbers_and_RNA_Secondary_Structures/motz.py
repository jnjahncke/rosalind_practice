#!/usr/bin/env python

import sys

MOD = 1000000

def count_noncrossing_matchings(rna):
    n = len(rna)
    # Initialize the Motzkin numbers
    m = [1, 1] + [0] * (n - 1)
    # Compute the Motzkin numbers using the recurrence relation
    for i in range(2, n + 1):
        s = 0
        for k in range(1, i):
            if (rna[k-1], rna[i-1]) in [('A', 'U'), ('U', 'A'), ('C', 'G'), ('G', 'C')]:
                s = (s + m[k-1] * m[i-k-1])
        m[i] = (m[i-1] + s)
    return m[n]


# Read the input RNA string from a file
rna = ""
with open(sys.argv[1],"r") as fasta:
    for line in fasta:
        line = line.rstrip()
        if line[0] != ">":
            rna += line

# Count the noncrossing matchings and print the result modulo 1,000,000
print(count_noncrossing_matchings(rna) % MOD)
