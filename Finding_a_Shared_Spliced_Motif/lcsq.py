#!/usr/bin/env python

import sys
from itertools import combinations

def is_subseq(seq, pattern):
    for NT in pattern:
        loc = seq.find(NT)
        if loc >= 0:
            seq = seq[loc+1:]
        else:
            return False
    return True

# import fasta
seq_dict = {}
with open(sys.argv[1],"r") as fasta:
    for line in fasta:
        line = line.rstrip()
        if line[0] == ">":
            seq_name = line[1:]
            seq_dict[seq_name] = ""
        else:
            seq_dict[seq_name] += line
seq1, seq2 = seq_dict.values()

# find all possible subsequences of seq1
seq1_sub = []
for length in range(len(seq1),0,-1):
    temp = [x for x in combinations(seq1, length)]
    for x in temp:
        x = "".join(x)
        if x not in seq1_sub:
            seq1_sub.append(x)
            if is_subseq(seq2, x) == True:
                print(x)
                exit()
