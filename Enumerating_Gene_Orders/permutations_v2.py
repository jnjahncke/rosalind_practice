#!/usr/bin/env python

import sys
from itertools import permutations

with open(sys.argv[1],"r") as i:
    n = int(i.read())

p = [y for y in permutations([x for x in range(1,n+1)],n)]

print(len([x for x in p]))
for i in p:
    print(*i, sep=" ")
