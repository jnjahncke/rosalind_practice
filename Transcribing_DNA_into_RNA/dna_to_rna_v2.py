#!/usr/bin/env python

import sys

dna = ""
with open(sys.argv[1],"r") as i:
    for line in i:
        dna += line.rstrip()
dna = dna.upper()

rna = dna.replace("T","U")

print(rna)
