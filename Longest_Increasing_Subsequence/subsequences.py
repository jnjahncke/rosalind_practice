#!/usr/bin/env python

import sys

inputfile = sys.argv[1]

with open(inputfile,"r") as raw:
    n = int(raw.readline())
    perm = raw.readline().split()

# find all increasing subsequences
increasing = []
for i in range(len(perm)):
    current = [perm[i]]
    for j in range(i,len(perm)):
        sub = perm[j:]
        if len(sub) > 0 and perm[j] == min(sub) and perm[j] > current[-1]:
                current.append(perm[j])
    increasing.append(current)
max_inc = max(increasing, key = len)

# check last digit
max_inc = max_inc[:-1]
pos = perm.index(max_inc[-1])
for i in range(pos,len(perm)):
    if perm[i] > max_inc[-1]:
        max_inc.append(perm[i])
print(*max_inc, sep = " ")

# find all decreasing subsequences
decreasing = []
for i in range(len(perm)):
    current = [perm[i]]
    for j in range(i,len(perm)):
        sub = perm[j:]
        if len(sub) > 0 and perm[j] == max(sub) and perm[j] < current[-1]:
                current.append(perm[j])
    decreasing.append(current)
max_dec = max(decreasing, key = len)

# check last digit
max_dec = max_dec[:-1]
pos = perm.index(max_dec[-1])
for i in range(pos,len(perm)):
    if perm[i] < max_dec[-1]:
        max_dec.append(perm[i])
print(*max_dec, sep = " ")
