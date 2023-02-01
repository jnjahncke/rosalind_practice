# Problem

In “Counting Subsets”, we saw that the total number of subsets of a set S containing n elements is equal to 2n.

However, if we intend to count the total number of subsets of S having a fixed size k, then we use the combination statistic C(n,k), also written (nk).

**Given**: Positive integers n and m with 0≤m≤n≤2000.

**Return**: The sum of combinations C(n,k) for all k satisfying m≤k≤n, modulo 1,000,000. In shorthand, ∑nk=m(nk).

## Sample Dataset

```
6 3
```

## Sample Output

```
42
```
