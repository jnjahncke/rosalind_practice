#!/usr/bin/env python

import sys
from math import factorial

inputfile = sys.argv[1]

with open(inputfile,"r") as inputfile:
    n, k = inputfile.readline().split()

n = int(n)
k = int(k)

print(int((factorial(n)/factorial(n-k))%1000000))
