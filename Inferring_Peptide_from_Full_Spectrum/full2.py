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

# read data
spec = []
with open(sys.argv[1],"r") as i:
    for line in i:
        line = float(line.rstrip())
        spec.append(line)
parent = spec[0]
n = int((len(spec)-3)/2)
spec.pop(0)


# determine ions
ions = []
while len(spec) > 0:
    for i in spec:
        for j in spec:
            if round(i+j,5) == round(parent,5):
                ions.append([i,j])
                spec.remove(i)
                spec.remove(j)


# determine peptide sequence
peptide = ""
ions = sorted(ions)
while len(peptide) < n:
    attempt = lookup(ions[1][0]-ions[0][0])
    if attempt != False:
        peptide += attempt
        ions.remove(ions[0])
    else:
        flip = ions.pop(1)
        ions.append(flip[::-1])
        ions = sorted(ions)

print(peptide)
