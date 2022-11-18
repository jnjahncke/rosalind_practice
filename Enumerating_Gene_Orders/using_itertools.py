#!/usr/bin/env python

import itertools as it
from math import factorial
import sys

n = int(sys.argv[1]) 

possible = factorial(n)
print(possible)

permutations = it.permutations(range(1,n+1))

for permutation in permutations:
    print(*permutation, sep = " ")
