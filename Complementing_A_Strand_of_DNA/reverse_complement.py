#!/usr/bin/env python

import sys

# get file name from command line
inputfile = sys.argv[1]

# get sequence from file
s = ""
with open(inputfile,"r") as inputfile:
    for line in inputfile:
        line = line.rstrip()
        s += line

# lowercase and reverse s
sc = s.lower()[::-1]

# swap nucleotides
sc = sc.replace("a","T").replace("t","A").replace("g","C").replace("c","G")

# print reverse complement to standard out
print(sc)
