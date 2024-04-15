#!/usr/bin/env python

import sys

# write a function that calculates gc content of a sequence
def gc_content(dna):
    dna = dna.upper()
    gc_sum = dna.count("G") + dna.count("C")
    dna_len = len(dna)
    return(100*gc_sum/dna_len)

# build dictionary of dna sequences
dna_dict = {}
with open(sys.argv[1],"r") as i:
    for line in i:
        if line[0] == ">":
            seqname = line.rstrip()[1:]
            dna_dict[seqname] = ""
        else:
            dna_dict[seqname] += line.rstrip()

# calculate gc content for all sequences
# keep track of highest gc content sequence
best_gc = 0
best_seq = ""
for seq in dna_dict:
    gc = gc_content(dna_dict[seq])
    if gc > best_gc:
        best_gc = gc
        best_seq = seq

print(best_seq)
print(round(best_gc,6))
