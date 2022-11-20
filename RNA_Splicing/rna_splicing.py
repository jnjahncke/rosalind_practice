#!/usr/bin/env python

import sys
import re

inputfile = sys.argv[1]

def translate(sequence):
    if len(re.findall(r"[^ATCG]",sequence)) > 0:
        return
    translation = ""
    for found in re.finditer(r"([ATGC]{3})", sequence):
        AA = codon_dict[found.group(1)]
        if AA == "Stop":
            break
        else:
            translation += AA
    return(translation)

# make translation dictionary
codon_dict = {}
with open("DNA_codon_table.txt","r") as table:
    for line in table:
        line = line.rstrip()
        for found in re.finditer(r"([GCAT]{3})\s(\w+)",line):
            codon_dict[found.group(1)] = found.group(2)

# read in sequences
introns = {}
with open(inputfile,"r") as raw:
    i = 0
    seq = ""
    for line in raw:
        line = line.rstrip()
        if line[0] == ">":
            i += 1
        if i == 1 and line[0] != ">":
            seq += line
        if i >= 2 and line[0] == ">":
            current = line
            introns[current] = ""
        if i >= 2 and line[0] != ">":
            introns[current] += line

# remove introns
for intron in introns:
    start = seq.find(introns[intron])
    end = start + len(introns[intron])
    seq = seq[:start] + seq[end:]

print(translate(seq))
