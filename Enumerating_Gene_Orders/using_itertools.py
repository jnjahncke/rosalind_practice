#!/usr/bin/env python

import itertools as it
from math import factorial

n = 3

possible = factorial(n)
print(possible)

permutations = it.permutations(range(1,n+1))

for permutation in permutations:
    print(*permutation, sep = " ")
