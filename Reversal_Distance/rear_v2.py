#!/usr/bin/env python

import sys
from itertools import combinations 

# finding breakpoints
def breakpoints(k,g):
    breakpoints = []
    l = len(k)-1
    # compare sequences
    for n in range(l):
        k1 = k[n]
        k2 = k[n+1]
        if abs(g.index(k1) - g.index(k2)) != 1: 
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
        if len(bps) > 0:
            combos = combinations(bps,2)
            for start,stop in combos:
                rev = reversal(seq,start,stop)
                new_seq_list.append(rev)
                bp_list.append(len(breakpoints(k,rev)))
                print(f"Key: {k}\nSeq: {seq}\nBPs: {bps}\nStart: {start}\tEnd: {stop}\nRev: {rev}\nNew BPs: {breakpoints(k,rev)}")
        else:
            return([seq])
    print(f"New seq list: {new_seq_list}")
    print(f"BP list: {bp_list}")
    if len(bp_list) > 0:
        min_bp = min(bp_list)
        w_min_bp = [x for x in new_seq_list if len(breakpoints(k,x)) == min_bp]
    else:
        w_min_bp = new_seq_list
    print(f"With min bps: {w_min_bp}")
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
    k.insert(0,"a")
    k.append("b")
    g.insert(0,"a")
    g.append("b")
    change = 0
    rev = [g]
    while k not in rev:
        rev = rev_combos(k,rev)
        change += 1
        print(f"Change: {change}")
    result.append(change)
print(*result)
