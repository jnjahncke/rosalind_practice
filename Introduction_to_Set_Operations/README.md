# Problem

If A and B are sets, then their union A∪B is the set comprising any elements in either A or B; their intersection A∩B is the set of elements in both A and B; and their set difference A−B is the set of elements in A but not in B.

Furthermore, if A is a subset of another set U, then the set complement of A with respect to U is defined as the set Ac=U−A. See the Sample sections below for examples.

**Given**: A positive integer n (n≤20,000) and two subsets A and B of {1,2,…,n}.

**Return**: Six sets: A∪B, A∩B, A−B, B−A, Ac, and Bc (where set complements are taken with respect to {1,2,…,n}).

## Sample Dataset

```
10
{1, 2, 3, 4, 5}
{2, 8, 5, 10}
```

## Sample Output

```
{1, 2, 3, 4, 5, 8, 10}
{2, 5}
{1, 3, 4}
{8, 10}
{8, 9, 10, 6, 7}
{1, 3, 4, 6, 7, 9}
```
