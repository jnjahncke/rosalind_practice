#!/usr/bin/env python

import sys
import re

inputfile = sys.argv[1]
mod = 1000000

# read in codon table
codon_dict = {}
with open("RNA_codon_table.txt","r") as table:
    for line in table:
        line = line.rstrip()
        for found in re.finditer(r"([GCAU]{3})\s(\w+)",line):
            if found.group(2) not in codon_dict:
                codon_dict[found.group(2)] = 1
            else:
                codon_dict[found.group(2)] += 1

# import protein sequence
with open(inputfile,"r") as i:
    seq = ""
    for line in i:
        line = line.rstrip()
        seq += line

# scroll through protein sequence
prod = 1
for AA in seq:
    prod = prod * (codon_dict[AA]%mod)
prod = prod * (codon_dict["Stop"]%mod)
print(prod%mod)
