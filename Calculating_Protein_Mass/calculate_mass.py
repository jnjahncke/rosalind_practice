#!/usr/bin/env python

import sys

inputfile = sys.argv[1]

# get protein sequence
with open(inputfile,"r") as i:
    protein = i.readline().rstrip()

# parse mass table
masses = {}
with open("monoisotopic_mass_table.txt","r") as mt:
    for line in mt:
        line = line.rstrip().split()
        masses[line[0]] = float(line[1])

# calculate mass of protein sequence
mass = 0
for AA in protein:
    mass += masses[AA]
print(round(mass,3))
