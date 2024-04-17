#!/usr/bin/env python

import sys
import re

# create codon table such that AA = BP
with open("DNA_codon_table.txt","r") as table:
    table = table.read().split()
bps = table[0::2]
aas = table[1::2]
table = dict(zip(bps,aas))

# translate a sequence
def translate(seq):
    translation = ""
    for found in re.finditer(r"([ATCG]{3})",seq):
        AA = table[found.group(1)]
        if AA == "Stop":
            break
        else:
            translation += AA
    return(translation)

# create reverse complement
def rev_comp(seq):
    seq = seq.upper().lower()
    rev_comp = seq.replace("g","C").replace("c","G").replace("a","T").replace("t","A")[::-1]
    return(rev_comp)

# create open reading frames
def orfs(seq):
    orf_list = [seq, seq[1:], seq[2:], rev_comp(seq), rev_comp(seq)[1:], rev_comp(seq)[2:]]
    return(orf_list)

# import sequence
seq = ""
with open(sys.argv[1],"r") as i:
    for line in i:
        if line[0] != ">":
            seq += line.rstrip()

# translate all ORFs
#   start = ATG
#   stop  = TAA, TAG, TGA
translations = []
for orf in orfs(seq):
    for found in re.finditer(r"(?=(ATG((?:[ACTG]{3})+))(?:TAA|TAG|TGA))",orf):
        translations.append(translate(found.group(1)))

print(*set(translations), sep = "\n")
