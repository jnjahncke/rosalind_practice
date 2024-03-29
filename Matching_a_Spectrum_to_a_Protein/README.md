# Problem

The complete spectrum of a weighted string s is the multiset S[s] containing the weights of every prefix and suffix of s.

**Given**: A positive integer n followed by a collection of n protein strings s1, s2, ..., sn and a multiset R of positive numbers (corresponding to the complete spectrum of some unknown protein string).

**Return**: The maximum multiplicity of R⊖S[sk] taken over all strings sk, followed by the string sk for which this maximum multiplicity occurs (you may output any such value if multiple solutions exist).

## Sample Dataset

```
4
GSDMQS
VWICN
IASWMQS
PVSMGAD
445.17838
115.02694
186.07931
314.13789
317.1198
215.09061
```

## Sample Output

```
3
IASWMQS
```
