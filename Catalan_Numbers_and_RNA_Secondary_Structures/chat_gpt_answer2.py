#!/usr/bin/env python

import sys

MODULUS = 1_000_000

def cat(rna, cache):
    if rna == '':
        return 1
    elif len(rna) == 1:
        return 0
    elif rna in [ 'AU', 'UA', 'CG', 'GC' ]:
        return 1
    elif len(rna) == 2:
        return 0
    elif rna in cache:
        return cache[rna]
    else:
        sum = 0
        for i in range(1, len(rna)):
            a = rna[0]
            b = rna[i]
            if a + b in [ 'AU', 'UA', 'CG', 'GC' ]:
                inside = rna[1:i]
                outside = rna[i+1:]

                cat_inside = cat(inside, cache) % MODULUS
                if cat_inside == 0:
                    continue
                cat_outside = cat(outside, cache) % MODULUS
                if cat_outside == 0:
                    continue

                sum += cat_inside * cat_outside
        cache[rna] = sum % MODULUS
        return sum % MODULUS

rna = ''.join([ line.strip() for line in open(sys.argv[1]) if line[0] not in '>' ])

cache = {}
print(cat(rna, cache))

