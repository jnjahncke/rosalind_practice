# Problem

A matching in a graph is noncrossing if none of its edges cross each other. If we assume that the n nodes of this graph are arranged around a circle, and if we label these nodes with positive integers between 1 and n, then a matching is noncrossing as long as there are not edges {i,j} and {k,l} such that i<k<j<l.

A noncrossing matching of basepair edges in the bonding graph corresponding to an RNA string will correspond to a possible secondary structure of the underlying RNA strand that lacks pseudoknots, as shown in Figure 3.

In this problem, we will consider counting noncrossing perfect matchings of basepair edges. As a motivating example of how to count noncrossing perfect matchings, let cn denote the number of noncrossing perfect matchings in the complete graph K2n. After setting c0=1, we can see that c1 should equal 1 as well. As for the case of a general n, say that the nodes of K2n are labeled with the positive integers from 1 to 2n. We can join node 1 to any of the remaining 2n−1 nodes; yet once we have chosen this node (say m), we cannot add another edge to the matching that crosses the edge {1,m}. As a result, we must match all the edges on one side of {1,m} to each other. This requirement forces m to be even, so that we can write m=2k for some positive integer k.

There are 2k−2 nodes on one side of {1,m} and 2n−2k nodes on the other side of {1,m}, so that in turn there will be ck−1⋅cn−k different ways of forming a perfect matching on the remaining nodes of K2n. If we let m vary over all possible n−1 choices of even numbers between 1 and 2n, then we obtain the recurrence relation cn=∑nk=1ck−1⋅cn−k. The resulting numbers cn counting noncrossing perfect matchings in K2n are called the Catalan numbers, and they appear in a huge number of other settings. See Figure 4 for an illustration counting the first four Catalan numbers.

**Given**: An RNA string s having the same number of occurrences of 'A' as 'U' and the same number of occurrences of 'C' as 'G'. The length of the string is at most 300 bp.

**Return**: The total number of noncrossing perfect matchings of basepair edges in the bonding graph of s, modulo 1,000,000.

## Sample Dataset

```
>Rosalind_57
AUAU
```

## Sample Output

```
2
```
