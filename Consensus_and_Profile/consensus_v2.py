#!/usr/bin/env python

import sys

# create fasta dictionary
seqs = {}
with open(sys.argv[1],"r") as i:
    for line in i:
        line = line.rstrip()
        if line[0] == ">":
            seqname = line[1:]
            seqs[seqname] = ""
        else:
            seqs[seqname] += line


# build profile
seqlen = len(seqs[seqname])
profile = {"A": [0] * seqlen,
        "C": [0] * seqlen,
        "G": [0] * seqlen,
        "T": [0] * seqlen} 

for seq in seqs.values():
    for n,bp in enumerate(seq):
        profile[bp][n] += 1

# find consensus
consensus = ""
for n in range(seqlen):
    max_NT, max_num = "", 0
    for NT in profile:
        if profile[NT][n] > max_num:
            max_NT, max_num = NT, profile[NT][n]
    consensus += max_NT

# print results
print(consensus)
print("A:", *profile["A"], sep = " ")
print("C:", *profile["C"], sep = " ")
print("G:", *profile["G"], sep = " ")
print("T:", *profile["T"], sep = " ")
