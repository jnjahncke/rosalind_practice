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

def reverse_complement(seq):
    seq = seq.lower()
    comp = seq.replace("g","C").replace("c","G").replace("a","T").replace("t","A")
    rev_comp = comp[::-1]
    return(rev_comp)

# make translation dictionary
codon_dict = {}
with open("DNA_codon_table.txt","r") as table:
    for line in table:
        line = line.rstrip()
        for found in re.finditer(r"([GCAT]{3})\s(\w+)",line):
            codon_dict[found.group(1)] = found.group(2)

# read in sequence
frames = {}
with open(inputfile,"r") as i:
    for line in i:
        line = line.rstrip()
        if line[0] == ">":
            frames[1] = ""
        else:
            frames[1] += line

# make reading frames
frames[2] = frames[1][1:]
frames[3] = frames[2][1:]
frames[4] = reverse_complement(frames[1])
frames[5] = frames[4][1:]
frames[6] = frames[5][1:]

# translate all frames
proteins = []
for frame in frames:
    # Start codon: ATG
    # Stop codons: TAA, TAG, TGA
    # Need overlapping matches in case two start codons exist before a stop
    for found in re.finditer(r"(?=(ATG([GCAT]{3})+)(TAA|TAG|TGA))",frames[frame]):
        s = found.group(1)
        if s != None and len(s) >= 3:
            proteins.append(translate(s))
proteins = list(set(proteins)) # eliminate duplicates from list
for protein in proteins:
    print(protein)
