#!/usr/bin/env python

import sys

inputfile = sys.argv[1]

with open(inputfile,"r") as inputfile:
    n, k = inputfile.readline().split()
n, k = int(n), int(k)

x = 1
for i in range(k):
    x *= n - i
    x %= 1000000
print(x)
