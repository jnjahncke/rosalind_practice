#!/usr/bin/env python

import sys
import re

inputfile = sys.argv[1]

with open(inputfile,"r") as inputfile:
    sequence, pattern = [line.rstrip() for line in inputfile]

# Find pattern locations
locations = []
for found in re.finditer(r"(?=(" + pattern + "))",sequence):
    locations.append(found.start(1)+1)

print(*locations, sep = " ")
