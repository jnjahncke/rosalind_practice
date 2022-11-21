#!/usr/bin/env python

import sys

inputfile = sys.argv[1]

with open(inputfile,"r") as raw:
    n = int(raw.readline())
    perm = [int(x) for x in raw.readline().split()]

def LIS(n,perm):
    arr = [[]]*(n+1)
    for i in perm:
        arr[i] = max(arr[:i], key = len) + [i]
    return(map(str, max(arr, key = len)))

print(*LIS(n,perm), sep = " ") # longest increasing sequence
print(*list(LIS(n,reversed(perm)))[::-1], sep = " ") # longest decreasing sequence
