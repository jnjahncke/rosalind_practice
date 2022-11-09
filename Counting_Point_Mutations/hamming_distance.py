#!/usr/bin/env python

import sys

inputfile = sys.argv[1]

with open(inputfile,"r") as inputfile:
    s,t = inputfile.readlines()

dh = 0
for i in range(0,len(s)):
    if s[i] != t[i]:
        dh += 1
print(dh)
