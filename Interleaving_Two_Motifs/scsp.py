#!/usr/bin/env python

import sys

def shortest_common_supersequence(s, t):
    
    # initialize a 2D array to store lengths of LCS
    m, n = len(s), len(t)
    dp = [[0] * (n+1) for _ in range(m+1)]

    # fill the dp array using dynamic programming
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s[i-1] == t[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # construct the shortest common supersequence using dp array
    i, j = m, n
    scs = []
    while i > 0 and j > 0:
        if s[i-1] == t[j-1]:
            scs.append(s[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            scs.append(s[i-1])
            i -= 1
        else:
            scs.append(t[j-1])
            j -= 1
    while i > 0:
        scs.append(s[i-1])
        i -= 1
    while j > 0:
        scs.append(t[j-1])
        j -= 1

    # reverse the constructed string to get the shortest common supersequence
    scs.reverse()
    return ''.join(scs)


# import data
with open(sys.argv[1],"r") as r:
    s,t = [x.strip() for x in r.readlines()]

print(shortest_common_supersequence(s, t))
