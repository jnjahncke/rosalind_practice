#!/usr/bin/env python

import sys
from itertools import permutations

with open(sys.argv[1],"r") as data:
    n = int(data.readline())

# make list of numbers to pull from
nums = [x for x in range(-n,n+1) if x != 0]

# make list of permutations
perms = []
for x in permutations(nums,n):
    # make sure numbers are unique (ie. 1 and -1 do not appear together)
    temp = [abs(y) for y in x]
    if len(set(temp)) == n:
        perms.append(x)

# print number of permutations
print(len(perms))

# print all permutations
for x in perms:
    print(*x, sep = " ")
