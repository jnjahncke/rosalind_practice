#!/usr/bin/env python

import sys
import numpy as np

# import number of couples (in order: AA-AA, AA-Aa, AA-aa, Aa-Aa, Aa-aa, aa-aa)
with open(sys.argv[1],"r") as i:
    parents = np.array([int(x) for x in i.read().split()])

# probabilities (assuming 2 children/couple)
probs = np.array([2 * x for x in [1, 1, 1, 0.75, 0.5, 0]])

# multiply parent*prob for each genotype to get expected number of offspring with dominant allele, sum up all genotypes
print(sum(parents*probs))
