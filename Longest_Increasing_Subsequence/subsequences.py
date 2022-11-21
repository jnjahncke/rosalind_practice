#!/usr/bin/env python

import sys

inputfile = sys.argv[1]

with open(inputfile,"r") as raw:
    n = int(raw.readline())
    perm = raw.readline().split()

# find all increasing and decreasing subsequences
increasing = []
decreasing = []
for i in range(n):
    current_inc = [perm[i]]
    current_dec = [perm[i]]
    for j in range(i,n):
        sub = perm[j:]
        if len(sub) > 0 and perm[j] == min(sub) and perm[j] > current_inc[-1]:
            current_inc.append(perm[j])
        if len(sub) > 0 and perm[j] == max(sub) and perm[j] < current_dec[-1]:
            current_dec.append(perm[j])
    increasing.append(current_inc)
    decreasing.append(current_dec)

max_inc = max(increasing, key = len)
max_dec = max(decreasing, key = len)

# check last digit increasing
max_inc = max_inc[:-1]
pos = perm.index(max_inc[-1])
for i in range(pos,n):
    if perm[i] > max_inc[-1]:
        max_inc.append(perm[i])
print(*max_inc, sep = " ")

# check last digit decreasing
max_dec = max_dec[:-1]
pos = perm.index(max_dec[-1])
for i in range(pos,n):
    if perm[i] < max_dec[-1]:
        max_dec.append(perm[i])
print(*max_dec, sep = " ")
