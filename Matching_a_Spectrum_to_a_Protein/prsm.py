#!/usr/bin/env python

import sys
from itertools import combinations

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

# find all possible differences between ions in spectrum
diff = []
for i,j in combinations(spec,2):
    diff.append(round(abs(i-j),5))
spec += diff

# find all possible differences between ions in peptides
#temp = []
#for p in peptides:
#    for i,j in combinations(ion_dict[p],2):
#        temp.append(round(abs(i-j),5))
#    ion_dict[p] += temp

# calculate multiplicities
mult = {}
for p in peptides:
    mult[p] = 0
    for ion in diff:
        if round(ion,5) in ion_dict[p]:
            mult[p] += 1

max_mult = {"x":0}
for p in mult:
    if mult[p] > list(max_mult.values())[0]:
        max_mult = {p:mult[p]}

for k,v in max_mult.items():
    print(v)
    print(k)
