#!/usr/bin/env python

import sys

# import sequences
seq_dict = {}
with open(sys.argv[1],"r") as fasta:
    for line in fasta:
        line = line.rstrip()
        if line[0] == ">":
            seqname = line[1:]
            seq_dict[seqname] = ""
        else:
            seq_dict[seqname] += line
seqlist = list(seq_dict.values())

# create distance function
def distance(s1,s2):
    count = 0
    for n in range(len(s1)):
        if s1[n] != s2[n]:
            count += 1
    return(count/len(s1))

# create distance matrix
D = []
for i in range(len(seqlist)):
    D.insert(i,[])
    for j in range(len(seqlist)):
        D[i].append(distance(seqlist[i],seqlist[j]))

# print matrix with correct formatting
[print(*x) for x in D]
