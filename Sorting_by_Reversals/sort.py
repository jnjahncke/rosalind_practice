#!/usr/bin/env python

import sys
from itertools import combinations 

# finding breakpoints
def breakpoints(k,g):
    breakpoints = []
    l = len(k)-1
    # compare sequences
    for n in range(l):
        g1 = g[n]
        g2 = g[n+1]
        if abs(k.index(g1) - k.index(g2)) != 1: 
            breakpoints.append(n+1)
    return(sorted(breakpoints))

# perform reversal
def reversal(seq, start, end):
    prefix = seq[:start]
    rev = seq[start:end][::-1]
    suffix = seq[end:]
    return(prefix + rev + suffix)

# do all possible combinations of reversals
# return reversal with fewest breakpoints
def rev_combos(k,seq_list):
    new_seq_list = []
    bp_list = []
    for seq in seq_list:
        bps = breakpoints(k,seq)
        combos = combinations(bps,2)
        for start,stop in combos:
            rev = reversal(seq,start,stop)
            new_seq_list.append(rev)
            bp_list.append(len(breakpoints(k,rev)))
    min_bp = min(bp_list)
    w_min_bp = [x for x in new_seq_list if len(breakpoints(k,x)) == min_bp]
    return(w_min_bp)

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
    k = ["a"] + k + ["b"]
    g = ["a"] + g + ["b"]
    change = 0
    rev = [g]
    while k not in rev:
        rev = rev_combos(k,rev)
        change += 1
    result.append(change)
print(*result)
