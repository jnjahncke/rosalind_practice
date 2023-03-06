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
peptides = []

def longest_peptide(ion, index=0, peptide = ""):
    for i in range(index, len(spec)):
        attempt = lookup(spec[i]-ion)
        if attempt != False:
            peptide += attempt
            longest_peptide(spec[i], i+1, peptide)
    peptides.append(peptide)

longest_peptide(spec[0])

print(sorted(peptides, key = len, reverse = True)[0])
