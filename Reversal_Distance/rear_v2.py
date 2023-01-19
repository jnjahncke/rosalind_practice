#!/usr/bin/env python

import sys

# finding breakpoints
def breakpoints(k,g):
    breakpoints = []
    l = len(k)-1
    # compare sequences
    for n in range(l):
        g1 = g.index(k[n])
        g2 = g.index(k[n+1])
        if g1+1 != g2:
            breakpoints.append(g1+1)
    return(sorted(breakpoints))

# perform reversal
def reversal(seq, start, end):
    prefix = seq[:start]
    rev = seq[start:end][::-1]
    suffix = seq[end:]
    return(prefix + rev + suffix)

# find minimum number of reversals


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
    k.insert(0,"a")
    k.append("b")
    g.insert(0,"a")
    g.append("b")
    print(breakpoints(k,g))
