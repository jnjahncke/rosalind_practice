#!/usr/bin/env python

from random import randrange
from math import factorial
from copy import deepcopy
import sys

n = int(sys.argv[1])

# build sequence from 1 to n
nums = []
[nums.append(i) for i in range(1,n+1)]

# find total possible number of permutations
possible = factorial(n)
print(possible)

# find all possible permutations
permutations = []
while len(permutations) < possible:
    temp = deepcopy(nums)
    perm = []
    while len(perm) < n:
        x = temp[randrange(len(temp))]
        while x in perm:
            x = temp[randrange(len(temp))]
        temp.remove(x)
        perm.append(x)
    # print to standard out
    if perm not in permutations:
        permutations.append(perm)
        print(*perm, sep = " ")
