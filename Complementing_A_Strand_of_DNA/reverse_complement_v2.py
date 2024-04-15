#!/usr/bin/env python

import sys

dna = ""
with open(sys.argv[1],"r") as i:
    for line in i:
        dna += line.rstrip()
dna = dna.lower()[::-1]

rc = dna.replace("a","T").replace("t","A").replace("g","C").replace("c","G")

print(rc)
