#!/usr/bin/env python

import sys

def mult(n,s):
    return(n-len(s)+1)

def p_base(base,GC):
    if base == "G" or base == "C":
        p = GC*0.5
    else:
        p = (1-GC)*0.5
    return(p)

def exp_num(n,subseq,GC):
    p = mult(n,subseq)
    for base in subseq:
        p *= p_base(base,GC)
    return(p)


# import data
with open(sys.argv[1],"r") as data:
    n,s,A = [line.rstrip() for line in data]

n = int(n)
A = [float(x) for x in A.split()]

# calculate probabilities
B = [round(exp_num(n,s,x),4) for x in A]
print(*B, sep = " ")
