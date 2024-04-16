#!/usr/bin/env python

import sys
import numpy as np

# create fasta dictionary
seqs = {}
with open(sys.argv[1],"r") as i:
    for line in i:
        line = line.rstrip()
        if line[0] == ">":
            seqname = line[1:]
            seqs[seqname] = ""
        else:
            seqs[seqname] += line

# load sequences into array
seqs = np.array([[y for y in x] for x in seqs.values()])

# build profile
bps = ["A","C","G","T"]
profileACGT = np.array([(seqs == bp).sum(axis=0) for bp in bps])

# find consensus
consensus_map = np.array(profileACGT.argmax(axis = 0))
consensus = np.array(bps)[consensus_map]

# print results
print(*consensus, sep = "")
for n,bp in enumerate(bps):
    print(f'{bp}: {" ".join(map(str,profileACGT[n]))}', sep = "")
