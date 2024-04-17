#!/usr/bin/env python

import sys

# import protein string
AA = ""
with open(sys.argv[1],"r") as i:
    for line in i:
        AA += line.rstrip()

# import mass table
with open("monoisotopic_mass_table.txt","r") as i:
    table = i.read().split()
table = dict(zip(table[0::2], [float(x) for x in table[1::2]]))

# calculate mass
mass = sum([table[a] for a in AA])
print(round(mass,3))
