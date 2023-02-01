#!/usr/bin/env python

import sys
from scipy.special import comb

with open(sys.argv[1],"r") as mn:
    n,m = mn.readline().strip().split()
    n,m = int(n), int(m)

# m is smaller than n
subsets = 0
for x in range(m,n+1):
    subsets += comb(n,x, exact = True)

print(int(subsets)%1000000)
