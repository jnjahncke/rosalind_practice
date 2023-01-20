#!/usr/bin/env python

import sys
from itertools import combinations 

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

# do all possible combinations of reversals
# return reversal with fewest breakpoints
def rev_combos(k,seq):
    bps = breakpoints(k,seq)
    if len(bps) > 0:
        combos = combinations(bps,2)
        seq_list = []
        bp_list = []
        for start,stop in combos:
            rev = reversal(seq,start,stop+1)
            seq_list.append(rev)
            bp_list.append(len(breakpoints(k,rev)))
        min_bp = bp_list.index(min(bp_list))
        return(seq_list[min_bp])
    else:
        return(seq)

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
    change = 0
    if k == g:
        result.append(change)
    else:
        rev = rev_combos(k,g)
        print(rev)
        change += 1
        while rev != k:
            rev = rev_combos(k,rev)
            print(rev)
            change += 1
        result.append(change)
print(*result)
