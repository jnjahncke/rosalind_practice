#!/usr/bin/env python

import sys

def lookup(weight):
    w = round(weight,4)
    if w in masses:
        return(masses[w])
    else:
        return(False)

# parse mass table
masses = {}
with open("monoisotopic_mass_table.txt","r") as mt:
    for line in mt:
        line = line.rstrip().split()
        masses[round(float(line[1]),4)] = line[0]

# import spectrum
spec = []
with open(sys.argv[1],"r") as i:
    for line in i:
        line = float(line.rstrip())
        spec.append(line)

# determine peptide sequence
spec = sorted(spec)
peptide = ""

while len(spec) > 1:
    attempt = lookup(spec[1]-spec[0])
    if attempt != False:
        peptide += attempt
        spec.pop(0)
    else:
        spec.pop(1)

print(peptide)
