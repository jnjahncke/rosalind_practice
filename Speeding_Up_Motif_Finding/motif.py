#!/usr/bin/env python

import sys

def motif(seq, subseq):
    result = seq.find(subseq)
    if result == 0:
        return True
    else:
        return False

# import sequence
seq = ""
with open(sys.argv[1],"r") as fasta:
    for line in fasta:
        line = line.rstrip()
        if line[0] != ">":
            seq += line

# build failure array
array = [0]
for i in range(1,len(seq)):
    longest = 0
    for j in reversed(range(i+1)):
        newseq = seq[:i]
        subseq = seq[i-j:i+1]
        length = len(subseq) 
        if length < longest:
            break
        elif subseq[0] == seq[0]:
            find = motif(newseq, subseq)
            if find == True and length > longest:
                longest = length
    array.append(longest)
print(*array, sep = " ")
