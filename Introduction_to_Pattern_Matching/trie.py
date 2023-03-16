#!/usr/bin/env python

import sys

def best_match(string, d):
    best = ""
    best_n = 0
    for dna_str in d:
        n = 0
        align = zip(string, dna_str)
        for item in align:
            if item[0] == item[1]:
                n += 1
            else:
                break
        if n > best_n:
            best_n = n
            best = dna_str
    return([best, best_n])

def adj_list(string, d, x):
    best, best_n = best_match(string, d)
    d[string] = []
    if best_n == 0: # new branch off of 1
        for i,NT in enumerate(string):
            if i == 0:
                d[string].append([NT,(1,x+1)])
                x += 1
            else:
                d[string].append([NT,(x,x+1)])
                x += 1
    else: # builds off existing branch
        # find branch off point
        start = d[best][best_n-1][1][1]
        new_string = string[best_n:]
        for NT in string[:best_n]:
            d[string].append([0,0])
        for i,NT in enumerate(new_string):
            if i == 0:
                d[string].append([NT,(start,x+1)])
                x += 1
            else:
                d[string].append([NT,(x,x+1)])
                x += 1
    return(d, x)

# import data
with open(sys.argv[1],"r") as r:
    dna = r.read().strip().split("\n")


# build adjacency list
d = {}
# key = dna string
# values = list of NTs, tuples
x = 0
for string in dna:
    if len(d) == 0:
        d[string] = []
        for i,NT in enumerate(string):
            d[string].append([NT,(i+1,i+2)])
            x = i+2
    elif string in d:
        continue
    else:
        d, x = adj_list(string, d, x)

# print list to std out
for l in d.values():
    for edge,node in l:
        if node != 0:
            print(node[0],node[1],edge)
