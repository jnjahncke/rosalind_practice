#!/usr/bin/env python

import sys

# take text file from user input
inputfile = sys.argv[1]

# read file, extract sequence
s = ""
with open(inputfile, "r") as inputfile:
    for line in inputfile:
        line = line.rstrip()
        s += line

# make sure all nucleotides are uppercase
s = s.upper()

# count nucleotides
A = s.count("A")
C = s.count("C")
G = s.count("G")
T = s.count("T")

# print counts to standard out
print(A, C, G, T)
