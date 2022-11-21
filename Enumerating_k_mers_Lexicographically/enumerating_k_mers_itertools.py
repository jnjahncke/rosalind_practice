#!/usr/bin/env python

import sys
from itertools import product

inputfile = sys.argv[1]

with open(inputfile,"r") as raw:
    alphabet, n = raw.readlines()

alphabet = alphabet.rstrip().split()
n = int(n)

for p in product(alphabet, repeat = n):
    print("".join(p))
