#!/usr/bin/env python

import sys
from scipy.special import comb
from math import log

# read in data
with open(sys.argv[1],"r") as raw:
    N = int(raw.readline().strip())

# probability of AT LEAST k shared chromosomes
# (out of 2N total chromosomes)
p = 0.5
n = 2*N
A = []
for i in range(1,n+1):
    Pr = 0
    for k in range(i,n+1):
        Pr += comb(n,k) * p**k * (1-p)**(n-k)
    logPr = round(log(Pr,10),4)
    A.append(logPr)

print(*A, sep = " ")
