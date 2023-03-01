#!/usr/bin/env python

import sys

def lookup(weight):
    return(masses[weight])

# parse mass table
masses = {}
with open("monoisotopic_mass_table.txt","r") as mt:
    for line in mt:
        line = line.rstrip().split()
        masses[round(float(line[1]),4)] = line[0]

# read data
spec = []
with open(sys.argv[1],"r") as i:
    for line in i:
        line = float(line.rstrip())
        spec.append(line)

# determine protein sequence
prot = ""
for i in range(len(spec)-1):
    prot += lookup(round(spec[i+1]-spec[i],4))

print(prot)
