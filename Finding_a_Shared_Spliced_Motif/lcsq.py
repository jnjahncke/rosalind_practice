#!/usr/bin/env python

import sys
from itertools import combinations

def is_subseq(seq, pattern):
    i = 0
    for NT in pattern:
        try:
            i = i + seq[i:].index(NT) + 1
        except:
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

# use combinations to find all subsequences of seq1
# starting from longest, subsequences, 
# see if they are also subsequences of seq2
# break at first match
seq1_sub = []
for length in range(len(seq1),0,-1):
    for x in ["".join(x) for x in combinations(seq1, length)]:
        if x not in seq1_sub:
            seq1_sub.append(x)
            if is_subseq(seq2, x) == True:
                print(x)
                exit()
