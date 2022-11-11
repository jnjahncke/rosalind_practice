#!/usr/bin/env python

import sys

inputfile = sys.argv[1]

# Numbers correspond to number of couples with each genotype combo
with open(inputfile, "r") as inputfile:
    for line in inputfile:
        line = line.rstrip()
        AAAA, AAAa, AAaa, AaAa, Aaaa, aaaa = line.split()

# each couple has two offspring
# calculate expected number of offspring with dominant allele
n1 = int(AAAA) * 1 * 2 # number of couples * probability of A * number of offspring
n2 = int(AAAa) * 1 * 2
n3 = int(AAaa) * 1 * 2
n4 = int(AaAa) * 0.75 * 2
n5 = int(Aaaa) * 0.5 * 2
n6 = int(aaaa) * 0 * 2

print(n1 + n2 + n3 + n4 + n5 + n6)
