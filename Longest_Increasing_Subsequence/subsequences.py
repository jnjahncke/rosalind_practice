#!/usr/bin/env python

import sys
from itertools import combinations, takewhile

def inc_dec(perm):
    status_inc = []
    status_dec = []
    for i in range(len(perm)-1):
        if perm[i] > perm[i+1]:
            status_dec.append(True)
            status_inc.append(False)
        elif perm[i] < perm[i+1]:
            status_dec.append(False)
            status_inc.append(True)
        else:
            status_dec.append(False)
            status_inc.append(False)
    if False not in status_inc:
        return("Increasing")
    elif False not in status_dec:
        return("Decreasing")


inputfile = sys.argv[1]

with open(inputfile,"r") as raw:
    n = int(raw.readline())
    perm = raw.readline().split()

increasing = []
decreasing = []
for i in range(n//2, (n//2) + 2):
    for c in combinations(perm, i):
        # if all decreasing
        if inc_dec(c) == "Decreasing":
            decreasing.append(c)
        # if all increasing
        elif inc_dec(c) == "Increasing":
            increasing.append(c)

max_inc = max(increasing, key = len)
print(*max_inc, sep = " ")

max_dec = max(decreasing, key = len)
print(*max_dec, sep = " ")
