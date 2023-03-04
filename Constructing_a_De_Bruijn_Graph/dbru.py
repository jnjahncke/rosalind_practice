#!/usr/bin/env python

import sys

def revcomp(seq):
    seq = seq.lower()
    rev = seq.replace("a","T").replace("t","A").replace("g","C").replace("c","G")
    return rev[::-1]

# import k-mers
kmers = []
with open(sys.argv[1],"r") as raw:
    for line in raw:
        line = line.rstrip()
        if line not in kmers:
            kmers.append(line)

# add reverse complements to kmers
for k in kmers:
    r = revcomp(k)
    if r not in kmers:
        kmers.append(r)

# make adjacency list
L = []
k = len(kmers[0])-1
for kmer in kmers:
    edge = (kmer[:k],kmer[1:])
    if edge not in L:
        L.append(edge)
L = sorted(L)

for edge in L:
    print(f"({edge[0]}, {edge[1]})")
