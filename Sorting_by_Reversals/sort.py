#!/usr/bin/env python

import sys
from itertools import combinations 

# turn list to string
def l2s(l):
    s = ""
    for x in l:
        s += str(x)
    return s

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
def rev_combos(k,seq_dict):
    new_seq_dict = {}
    bp_list = []
    for seq in seq_dict:
        seq_dict[seq]["change"] += 1
        bps = breakpoints(k,seq_dict[seq]["seq"])
        combos = combinations(bps,2)
        for start,stop in combos:
            rev = reversal(seq_dict[seq]["seq"],start,stop)
            new_seq_dict[l2s(rev)] = {"seq":rev, "change":seq_dict[seq]["change"], "reversals":[(start,stop-1)] + seq_dict[seq]["reversals"]}
            bp_list.append(len(breakpoints(k,rev)))
    min_bp = min(bp_list)
    
    seq_dict_out = {}
    for rev in new_seq_dict:
        if len(breakpoints(k,new_seq_dict[rev]["seq"])) == min_bp:
            seq_dict_out[rev] = {"seq":new_seq_dict[rev]["seq"], 
                    "change":new_seq_dict[rev]["change"], 
                    "reversals":new_seq_dict[rev]["reversals"]}

    return seq_dict_out

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

    seq_dict = {}
    seq_dict[l2s(g)] = {"seq":g, "change":0, "reversals":[]}
    while l2s(k) not in seq_dict.keys():
        seq_dict = rev_combos(k,seq_dict)

for seq in seq_dict:
    print(seq_dict[seq]["change"])
    revs = seq_dict[seq]["reversals"]
    for rev in revs:
        print(*rev, sep = " ")
