#!/usr/bin/env python

from random import randrange
from math import factorial
from copy import deepcopy

n = 5

nums = []
for i in range(1,n+1):
    nums.append(i)

possible = factorial(n)
print(possible)

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
    if perm not in permutations:
        permutations.append(perm)
        print(*perm, sep = " ")
