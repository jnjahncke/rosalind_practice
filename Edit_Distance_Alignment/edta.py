#!/usr/bin/env python

import sys

def cost(x,y):
    if x == y:
        return 0
    else:
        return 1

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

            d[i][j] = min(d[i-1][j] + 1, # deletion
                d[i][j-1] + 1, # insertion
                d[i-1][j-1] + cost(s[i-1],t[j-1])) # substitution(1)/same(0)

    change = d[m][n]
    
    # format sequences
    s_fmt = ""
    t_fmt = ""

    while m > 0 and n > 0:
        left = d[m][n-1]
        top = d[m-1][n]
        left_top = d[m-1][n-1]
        floor = min(left, top, left_top)

        if (floor == d[m][n]) or \
                (floor == left and floor == top) or \
                (floor != left and floor != top):
            s_fmt = s[m-1] + s_fmt
            t_fmt = t[n-1] + t_fmt
            m -= 1
            n -= 1

        elif floor != left and floor == top:
            s_fmt = s[m-1] + s_fmt
            t_fmt = "-" + t_fmt
            m -= 1

        elif floor == left and floor != top:
            s_fmt = "-" + s_fmt
            t_fmt = t[n-1] + t_fmt
            n -= 1

#    print(*d,sep="\n")
    return(change, s_fmt, t_fmt)

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

    change,s_fmt,t_fmt = levenshtein_distance(s,t)

    print(change)
    print(s_fmt)
    print(t_fmt)

if __name__ == "__main__":
    main()
