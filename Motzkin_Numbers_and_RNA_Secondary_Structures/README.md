# Problem

Similarly to our definition of the Catalan numbers, the n-th Motzkin number mn counts the number of ways to form a (not necessarily perfect) noncrossing matching in the complete graph Kn containing n nodes.

How should we compute the Motzkin numbers? As with Catalan numbers, we will take m0=m1=1. To calculate mn in general, assume that the nodes of Kn are labeled around the outside of a circle with the integers between 1 and n, and consider node 1, which may or may not be involved in a matching. If node 1 is not involved in a matching, then there are mn−1 ways of matching the remaining n−1 nodes. If node 1 is involved in a matching, then say it is matched to node k: this leaves k−2 nodes on one side of edge {1,k} and n−k nodes on the other side; as with the Catalan numbers, no edge can connect the two sides, which gives us mk−2⋅mn−k ways of matching the remaining edges. Allowing k to vary between 2 and n yields the following recurrence relation for the Motzkin numbers: mn=mn−1+∑nk=2mk−2⋅mn−k.

To count all possible secondary structures of a given RNA string that do not contain pseudoknots, we need to modify the Motzkin recurrence so that it counts only matchings of basepair edges in the bonding graph corresponding to the RNA string.

**Given**: An RNA string s of length at most 300 bp.

**Return**: The total number of noncrossing matchings of basepair edges in the bonding graph of s, modulo 1,000,000.

## Sample Dataset

```
>Rosalind_57
AUAU
```

## Sample Output

```
7
```
