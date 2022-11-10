#!/usr/bin/env python

import sys

inputfile = sys.argv[1]

# read in sequences
seq_dict = {}
with open(inputfile,"r") as inputfile:
    for line in inputfile:
        line = line.rstrip()
        if line[0] == ">":
            sequence = line[1:]
            seq_dict[sequence] = ""
        else:
            seq_dict[sequence] += line

# build profile
length = len(seq_dict[sequence])
A = [0] * length
C = [0] * length
G = [0] * length
T = [0] * length

for seq in seq_dict:
    for i in range(length):
        NT = seq_dict[seq][i]
        if NT == "A":
            A[i] += 1
        elif NT == "C":
            C[i] += 1
        elif NT == "G":
            G[i] += 1
        elif NT == "T":
            T[i] += 1
profile_dict = {"A":A, "C":C, "G":G, "T":T}

# find consensus sequence
consensus = []
for i in range(length):
    max_NT = ""
    max_num = 0
    for NT in profile_dict:
        if profile_dict[NT][i] > max_num:
            max_NT = NT
            max_num = profile_dict[NT][i]
    consensus.append(max_NT)

# format output
print("".join(consensus))
for NT in profile_dict:
    line = NT + ": "
    for i in range(length):
        line += str(profile_dict[NT][i]) + " "
    print(line)
