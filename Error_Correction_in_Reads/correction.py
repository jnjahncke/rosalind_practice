#!/usr/bin/env python

import sys

def reverse_complement(sequence):
    seq = sequence.lower()
    seq = seq.replace("a","T").replace("t","A").replace("g","C").replace("c","G")
    return(seq[::-1])

def hamming_distance(seq1, seq2):
    length = max([len(seq1),len(seq2)])
    dh = 0
    for i in range(length):
        if seq1[i] != seq2[i]:
            dh += 1
    return(dh)

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

# find correct vs erroneous sequences
flipped_dict = {}
for k,v in seq_dict.items():
    rev = reverse_complement(v)
    if v not in flipped_dict and rev not in flipped_dict:
        flipped_dict[v] = [k]
    elif v in flipped_dict:
        flipped_dict[v].append(k)
    elif rev in flipped_dict:
        flipped_dict[rev].append(k)

# make list of correct vs erroneous sequences
errors = []
correct = []
for k,v in flipped_dict.items():
    if len(v) == 1:
        errors.append(k)
    else:
        correct.append(k)

# check for hamming distance of 1
for seq1 in errors:
    for seq2 in correct:
        hd_fwd = hamming_distance(seq1,seq2)
        if hd_fwd == 1:
            print(f"{seq1}->{seq2}")
            continue
        rev = reverse_complement(seq2)
        hd_rev = hamming_distance(seq1,rev)
        if hd_rev == 1:
            print(f"{seq1}->{rev}")
