#!/usr/bin/env python

import sys

def trans_type(NT1,NT2):
    if NT1 == "A" and NT2 == "G":
        return("transition")
    elif NT1 == "G" and NT2 == "A":
        return("transition")
    elif NT1 == "C" and NT2 == "T":
        return("transition")
    elif NT1 == "T" and NT2 == "C":
        return("transition")
    elif NT1 == NT2:
        return("same")
    else:
        return("transversion")

# import sequences
seqs = {}
with open(sys.argv[1],"r") as fasta:
    for line in fasta:
        line = line.rstrip()
        if line[0] == ">":
            seq_name = line[1:]
            seqs[seq_name] = ""
        else:
            seqs[seq_name] += line

# compare sequences
seq1, seq2 = list(seqs.values())
transitions = 0
transversions = 0
for i in range(len(seq1)):
    trans = trans_type(seq1[i],seq2[i])
    if trans == "transition":
        transitions += 1
    elif trans == "transversion":
        transversions += 1
print(transitions/transversions)
