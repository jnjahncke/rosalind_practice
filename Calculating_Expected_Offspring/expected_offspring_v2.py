#!/usr/bin/env python

import sys

inputfile = sys.argv[1]

# in the order of: AA-AA, AA-Aa, AA-aa, Aa-Aa, Aa-aa, aa-aa
with open(inputfile, "r") as inputfile:
    parents = [int(x) for x in inputfile.read().split()]

# multiply probability * number of offspring (2)
probabilities = [2 * x for x in [1, 1, 1, 0.75, 0.5, 0]]

# add up parents * probabilities
n = sum([parent*prob for parent,prob in zip(parents, probabilities)])
print(n)
