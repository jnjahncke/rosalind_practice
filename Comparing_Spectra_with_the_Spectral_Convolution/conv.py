#!/usr/bin/env python

import sys

# import multisets
with open(sys.argv[1],"r") as i:
    a = [float(x) for x in i.readline().split()]
    b = [float(x) for x in i.readline().split()]

# calculate differences
d = []
for i in a:
    for j in b:
        d.append(round(i-j,5))

# calculate reoccurrences
mult = {}
for i in d:
    if i not in mult:
        mult[i] = 1
    else:
        mult[i] += 1

# find max reoccurrence
num = 0
for i in mult:
    if mult[i] > num:
        num = mult[i]
        result = i

print(num)
print(result)
