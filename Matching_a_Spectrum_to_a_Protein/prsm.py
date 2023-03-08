#!/usr/bin/env python

import sys

# parse mass table
AAs = {}
with open("monoisotopic_mass_table.txt","r") as mt:
    for line in mt:
        line = line.rstrip().split()
        AAs[line[0]] = round(float(line[1]),5)

# import data 
with open(sys.argv[1],"r") as i:
    raw = i.readlines()

n = int(raw.pop(0))
peptides = []
for i in range(n):
    peptides.append(raw.pop(0).strip())
spec = sorted([float(x) for x in raw])

# find b- and y-ions for all given peptides
ion_dict = {}
for p in peptides:
    ion_dict[p] = []
    for i in range(len(p)):
        b, b_mass = p[:i],0
        y, y_mass = p[i:], 0
        for AA in b:
            b_mass += AAs[AA]
        for AA in y:
            y_mass += AAs[AA]
        if b_mass > 0:
            ion_dict[p].append(round(b_mass,5))
        if y_mass > 0:
            ion_dict[p].append(round(y_mass,5))

# calculate multiplicities
# for each b- and y-ion, calculate the minkowski distance:
#   the distance between the ion on the spectrum
#   and the b/y-ion
# keep count of the number of times each minowski distance appears.
# the max number of appearances is the maximum multiplicity.
# do this for each peptide.
mult = {}
max_mult = {}
for p in peptides:
    mult[p] = {}
    for ion in spec:
        for j in ion_dict[p]:
            distance = round(ion - j,4)
            if distance not in mult[p]:
                mult[p][distance] = 1
            else:
                mult[p][distance] += 1
    max_mult[p] = max(mult[p].values())

# report the peptide with the maximum multiplicity out of all peptides
answer_m = 0
answer_p = ""
for p in max_mult:
    if max_mult[p] > answer_m:
        answer_m = max_mult[p]
        answer_p = p

print(answer_m)
print(answer_p)
