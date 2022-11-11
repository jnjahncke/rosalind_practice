#!/usr/bin/env python

import sys

inputfile = sys.argv[1]

# import sequences
seq_dict = {}
with open(inputfile,"r") as inputfile:
    for line in inputfile:
        line = line.rstrip()
        if line[0] == ">":
            seq_name = line[1:]
            seq_dict[seq_name] = ""
        else:
            seq_dict[seq_name] += line

# find overlaps
overlaps = []
for i in seq_dict:
    for j in seq_dict:
        if i == j:
            continue
        suffixi = seq_dict[i][-3:]
        prefixj = seq_dict[j][:3]
        suffixj = seq_dict[j][-3:]
        prefixi = seq_dict[i][:3]
        # order matters: suffix to prefix
        if suffixi == prefixj:
            overlaps.append(str(i) + " " + str(j))
        elif suffixj == prefixi:
            overlaps.append(str(j) + " " + str(i))

# print overlaps to standard out
# make sure there are no duplicates
for overlap in set(overlaps):
    print(overlap)
