#!/usr/bin/env python

import sys
from scipy.special import comb

with open(sys.argv[1],"r") as data:
    n = int(data.readline().strip())

subsets = 1
for x in range(1,n+1):
    subsets += comb(n,x, exact = True)

print(int(subsets)%1000000)
