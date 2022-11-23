#!/usr/bin/env python

import sys
import re

inputfile = sys.argv[1]

def find_overlap(seq1,seq2):
    length = len(min([seq1,seq2], key = len))

    # does the start of seq1 = end of seq2?
    # does the start of seq2 = end of seq1?
    seq12 = ""
    seq21 = ""
    for i in range(length)[::-1]:
        if bool(re.findall(seq1[:i] + r"$", seq2)):
            seq12 = seq1[:i]
            break
        if bool(re.findall(seq2[:i] + r"$", seq1)):
            seq21 = seq2[:i]
            break

    if bool(seq12) == True and len(seq12) >= (length//2):
        return(combine_seqs(seq2, seq1, seq12))
    if bool(seq21) == True and len(seq21) >= (length//2):
        return(combine_seqs(seq1, seq2, seq21))
    else:
        return(False)

def combine_seqs(first, second, overlap):
    first_loc = first.find(overlap)
    first = first[:first_loc]
    combined = first + second
    return(combined)

def find_combos(seq_list, consensus = ""):
    
    if len(seq_list) == 0:
        return(consensus)

    elif len(consensus) == 0:
        consensus = seq_list.pop(0)
        return(seq_list, consensus)

    else:
        for i in seq_list:
            test = find_overlap(i, consensus)
            if bool(test) == True:
                consensus = test 
                seq_list.remove(i)
        return(seq_list, consensus)

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
superstring = find_combos(seqs)
while len(superstring[0]) > 0:
    superstring = find_combos(superstring[0], superstring[1])
print(superstring[1])
