#!/usr/bin/env python

import sys

dna = ""
with open(sys.argv[1], "r") as i:
    for line in i:
        dna += line.rstrip()
dna = dna.upper()

print(dna.count("A"), dna.count("C"), dna.count("G"), dna.count("T"))
