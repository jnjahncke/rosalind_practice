#!/usr/bin/env python

import sys
import re

# build codon dictionary
codon_dict = {}
with open("RNA_codon_table.txt","r") as d:
    for line in d:
        line = line.rstrip()
        for found in re.finditer(r"([GCAU]{3})\s(\w+)", line):
            codon_dict[found.group(1)] = found.group(2)

# import rna sequence
rna = ""
with open(sys.argv[1],"r") as i:
    for line in i:
        line = line.rstrip()
        rna += line

# build function that translates rna  -> protein
def rna2AA(rna):
    AA = ""
    while len(rna) > 3:
        if codon_dict[rna[0:3]] == "Stop":
            break
        else:
            AA += codon_dict[rna[0:3]]
            rna = rna[3:]
    return(AA)

print(rna2AA(rna))
