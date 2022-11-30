#!/usr/bin/env python

import sys
from itertools import permutations

with open(sys.argv[1],"r") as data:
    n = int(data.readline())

# make list
pos = [x for x in range(1,n+1)]
neg = [x * -1 for x in range(1,n+1)]
nums = pos + neg

# make list of permutations
perms = []
for x in permutations(nums,n):
    # make sure numbers are unique (ie. 1 and -1 do not appear together)
    temp = [abs(y) for y in x]
    if len(set(temp)) == n:
        perms.append(x)

print(len(perms))
for x in perms:
    print(*x, sep = " ")
