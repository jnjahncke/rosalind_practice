#!/usr/bin/env python

import sys

inputfile = sys.argv[1]

with open(inputfile,"r") as raw:
    n = int(raw.readline())
    perm = [int(x) for x in raw.readline().split()]

def LDS(perm):
    m = [0] * len(perm)
    for x in range(len(perm)-2,-1,-1):
        for y in range(len(perm)-1,x,-1):
            if m[x] <= m[y] and perm[x] > perm[y]:
                m[x] = m[y] + 1

    max_value = max(m)

    result = []
    for i in range(len(m)):
        if max_value == m[i]:
            result.append(perm[i])
            max_value -= 1

    return(result)

def LIS(perm):
    m = [0] * len(perm)
    for x in range(len(perm)-2,-1,-1):
        for y in range(len(perm)-1,x,-1):
            if m[x] >= m[y] and perm[x] < perm[y]:
                m[x] = m[y] - 1

    min_value = min(m)

    result = []
    for i in range(len(m)):
        if min_value == m[i]:
            result.append(perm[i])
            min_value += 1

    return(result)

print(*LIS(perm), sep = " ")
print(*LDS(perm), sep = " ")
