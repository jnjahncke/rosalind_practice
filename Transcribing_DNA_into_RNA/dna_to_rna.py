#!/usr/bin/env python

import sys

# get file from command line
inputfile = sys.argv[1]

# get sequence from file
s = ""
with open(inputfile,"r") as inputfile:
    for line in inputfile:
        line = line.rstrip()
        s += line
# make sure all nucleotides are uppercase
s = s.upper()

# transcribe sequence to RNA
s = s.replace("T","U")

print(s)


