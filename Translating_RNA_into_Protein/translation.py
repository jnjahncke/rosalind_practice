#!/usr/bin/env python

import re
import sys

codon_dict = {}
# make translation dictionary
with open("RNA_codon_table.txt","r") as table:
    for line in table:
        line = line.rstrip()
        for found in re.finditer(r"([GCAU]{3})\s(\w+)",line):
            codon_dict[found.group(1)] = found.group(2)

# import sequence
inputfile = sys.argv[1]
with open(inputfile,"r") as inputfile:
    sequence = str(inputfile.readlines())

# translate sequence
translation = ""
for found in re.finditer(r"([AUGC]{3})", sequence):
    AA = codon_dict[found.group(1)]
    if AA == "Stop":
        break
    else:
        translation += AA

print(translation)
