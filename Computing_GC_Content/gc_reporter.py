#!/usr/bin/env python

import sys
import re

inputfile = sys.argv[1]

def gc_content(sequence):
    sequence = sequence.upper()
    seq_len = len(sequence)
    gc_num = sequence.count("G") + sequence.count("C")
    gc_pct = gc_num * 100 / seq_len
    return(gc_pct)


seq_dict = {}
gc_max = 0
seq_max = ""

with open(inputfile,"r") as inputfile:
    for line in inputfile:
        line = line.rstrip()
        if line[0] == ">":
            sequence = ""
            seq_name = re.findall(r">(Rosalind_[0-9]{4})",line)[0]
            seq_dict[seq_name] = {"seq":"","gc":0}
        else:
            seq_dict[seq_name]["seq"] += line
   
for sequence in seq_dict:
    seq_dict[sequence]["gc"] += gc_content(seq_dict[sequence]["seq"])
    if seq_dict[sequence]["gc"] > gc_max:
        gc_max = seq_dict[sequence]["gc"]
        seq_max = sequence

print(seq_max)
print(round(gc_max,6))
