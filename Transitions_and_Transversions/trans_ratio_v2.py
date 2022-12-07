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
# a for transition
# b for translation
mut = ["a" if trans_type(NT1,NT2) == "transition" else "b" for NT1,NT2 in zip(seq1,seq2) if NT1 is not NT2]
print(mut.count("a")/mut.count("b"))
