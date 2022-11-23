#!/usr/bin/env python

import sys
from copy import deepcopy
import re

inputfile = sys.argv[1]

def find_overlap(seq1,seq2):
    length = len(min([seq1,seq2], key = len))

    # does the start of seq1 = end of seq2?
    # does the start of seq2 = end of seq1?
    seq12 = ""
    seq21 = ""
    for i in range(length//2,length):
        if bool(re.findall(seq1[:i] + r"$", seq2)):
            seq12 = seq1[:i]
        if bool(re.findall(seq2[:i] + r"$", seq1)):
            seq21 = seq2[:i]

    # check that they're long enough
    length = (length//2)-1
    if bool(seq12) == True and len(seq12) >= length:
        return(seq2, seq1, seq12)
    if bool(seq21) == True and len(seq21) >= length:
        return(seq1, seq2, seq21)
    else:
        return(False)
    

def combine_seqs(first, second, overlap):
    first_loc = first.find(overlap)
    first = first[:first_loc]
    combined = first + second
    return(combined)


def find_combos(seq_list):
    combos = []
    for i in seq_list:
        for j in seq_list:
            if i != j:
                test = find_overlap(i,j)
                print(test)
                if bool(test) != False:
                    first, second, overlap = test
                    combos.append(combine_seqs(first, second, overlap))
                    combos = list(set(combos))
    return(combos)

# import subsequences
sequences = {}
with open(inputfile,"r") as inputfile:
    for line in inputfile:
        line = line.rstrip()
        if line[0] == ">":
            seq = line[1:]
            sequences[seq] = ""
        else:
            sequences[seq] += line
seqs = list(sequences.values())

# join subsequences into supersequence
combos = find_combos(seqs)
print(combos)
exit()
while len(combos) > 1:
    combos = find_combos(combos)
print(combos[0])
