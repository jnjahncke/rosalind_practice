#!/usr/bin/env python

import sys

inputfile = sys.argv[1]

with open(inputfile,"r") as inputfile:
    sequence, pattern = [line.rstrip() for line in inputfile]

# Find pattern locations
locations = []
start = 0
while sequence.find(pattern) > 0:
    loc = sequence.find(pattern)
    locations.append(loc + start + 1)
    start += loc+1
    sequence = sequence[loc+1:]
output = ""
for x in locations:
    output += str(x) + " "
print(output)
