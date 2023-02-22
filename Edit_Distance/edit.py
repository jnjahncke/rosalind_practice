#!/usr/bin/env python

import sys

def levenshtein_distance(s,t):
    
    m = len(s)
    n = len(t)

    # create empty matrix with dimensions m x n
    d = [[0 for j in range(n+1)] for i in range(m+1)]

    # make first column == 0:len(s)
    for i in range(m+1):
        d[i][0] = i
    
    # make first row = 0:len(t)
    for i in range(n+1):
        d[0][i] = i
    
    # calculate distance of all prefixes of s vs all prefixes of t
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s[i-1] == t[j-1]:
                cost = 0
            else:
                cost = 1

            d[i][j] = min(d[i-1][j] + 1, # deletion
                d[i][j-1] + 1, # insertion
                d[i-1][j-1] + cost) # substitution
    
    return(d[m][n])

def fasta_parser(filename):
    seq_dict = {}
    with open(filename,"r") as fasta:
        for line in fasta:
            line = line.rstrip()
            if line[0] == ">":
                seq = line[1:]
                seq_dict[seq] = ""
            else:
                seq_dict[seq] += line
    return(seq_dict)

def main():
    seq_dict = fasta_parser(sys.argv[1])
    s,t = seq_dict.values()

    print(levenshtein_distance(s,t))

if __name__ == "__main__":
    main()
