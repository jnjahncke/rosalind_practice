#!/usr/bin/env python

import sys

# import sequences
keys = []
given = []
with open(sys.argv[1],"r") as perms:
    linenum = 0
    for line in perms:
        line = line.rstrip()
        if line.rstrip() != "":
            linenum += 1
            if linenum%2 == 1: # odd
                line = [int(x) for x in line.split()]
                keys.append(line)
            if linenum%2 == 0: # even
                line = [int(x) for x in line.split()]
                given.append(line)

# make reversals until they match                
perms = zip(keys,given)
result = []
for k,g in perms:
    change = 0
    for n in range(len(k)-1):
        if k[n] != g[n]:
            f = g.index(k[n])
            rev = g[n:f+1]
            g = g[:n] + rev[::-1] + g[f+1:]
            change += 1
    result.append(change)
print(*result)
