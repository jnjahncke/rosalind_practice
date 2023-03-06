# Problem

For a weighted alphabet A and a collection L of positive real numbers, the spectrum graph of L is a digraph constructed in the following way. First, create a node for every real number in L. Then, connect a pair of nodes with a directed edge (u,v) if v>u and v−u is equal to the weight of a single symbol in A. We may then label the edge with this symbol.

In this problem, we say that a weighted string s=s1s2⋯sn matches L if there is some increasing sequence of positive real numbers (w1,w2,…,wn+1) in L such that w(s1)=w2−w1, w(s2)=w3−w2, ..., and w(sn)=wn+1−wn.

**Given**: A list L (of length at most 100) containing positive real numbers.

**Return**: The longest protein string that matches the spectrum graph of L (if multiple solutions exist, you may output any one of them). Consult the monoisotopic mass table.

## Sample Dataset

```
3524.8542
3623.5245
3710.9335
3841.974
3929.00603
3970.0326
4026.05879
4057.0646
4083.08025
```

## Sample Output

```
WMSPG
```
