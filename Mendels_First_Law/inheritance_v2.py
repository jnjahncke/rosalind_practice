#!/usr/bin/env python

import sys

# import k, m, and n
with open(sys.argv[1],"r") as i:
    k,m,n = [int(x) for x in i.read().split()]

# write a function to return heritability prop
def heritability(parentA, parentB):
    hit = 0
    for a in parentA:
        for b in parentB:
            if "A" in a+b:
                hit += 1
    return(hit/4)
                   
geno = ["AA","Aa","aa"]
KMN = [k, m, n]

total = k + m + n
total1 = total - 1
prob = 0
for parentA, A in zip(geno, KMN):
    for parentB, B in zip(geno, KMN):
        h = heritability(parentA, parentB)
        if parentA == parentB:
            prob += (A/total) * ((B-1)/total1) * h
        else:
            prob += (A/total) * (B/total1) * h

print(round(prob,6))
