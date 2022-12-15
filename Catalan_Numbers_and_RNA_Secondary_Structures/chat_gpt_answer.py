#!/usr/bin/env python

import sys

def solve_problem(fasta_file):
    # read the input file and extract the RNA string
    with open(fasta_file, 'r') as f:
        rna = f.read().strip().split('\n')[1]

    # calculate the number of noncrossing perfect matchings of basepair edges
    # using a recursive approach with memoization
    cache = {}
    def memoize(f):
        def decorated_function(*args):
            if args not in cache:
                cache[args] = f(*args)
            return cache[args]
        return decorated_function

    @memoize
    def dp(rna):
        if len(rna) == 0:
            return 1
        matches = 0
        for i in range(1, len(rna)):
            if rna[0]+rna[i] in ['AU', 'UA', 'CG', 'GC']:
                matches += dp(rna[1:i]) * dp(rna[i+1:])
        return matches

    # return the result modulo 1,000,000
    return dp(rna) % 1000000


fasta_file = sys.argv[1]
result = solve_problem(fasta_file)
print(result)
