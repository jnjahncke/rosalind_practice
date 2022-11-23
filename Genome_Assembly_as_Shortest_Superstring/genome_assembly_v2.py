#!/usr/bin/env python

import sys

fasta = sys.argv[1]

def get_superstring(seqs, superstring=''):
    if len(seqs) == 0:
        return superstring

    elif len(superstring) == 0:
        superstring = seqs.pop(0)
        return get_superstring(seqs, superstring)

    else:
        for i in range(len(seqs)):
            current = seqs[i]
            length = len(current)

            for test in range(length // 2):
                overlap_length = length - test

                if superstring.startswith(current[test:]):
                    seqs.pop(i)
                    return get_superstring(seqs, current[:test] + superstring)

                if superstring.endswith(current[:overlap_length]):
                    seqs.pop(i)
                    return get_superstring(seqs, superstring + current[overlap_length:])

# import subsequences
sequences = {}
with open(fasta,"r") as inputfile:
    for line in inputfile:
        line = line.rstrip()
        if line[0] == ">":
            seq = line[1:]
            sequences[seq] = ""
        else:
            sequences[seq] += line
seqs = list(sequences.values())

# find superstring
consensus = get_superstring(seqs)
print(consensus)
