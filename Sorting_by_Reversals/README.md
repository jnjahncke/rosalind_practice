# Problem

A reversal of a permutation can be encoded by the two indices at the endpoints of the interval that it inverts; for example, the reversal that transforms (4,1,2,6,3,5) into (4,1,3,6,2,5) is encoded by [3,5].

A collection of reversals sorts π into γ if the collection contains drev(π,γ) reversals, which when successively applied to π yield γ.

**Given**: Two permutations π and γ, each of length 10.

**Return**: The reversal distance drev(π,γ), followed by a collection of reversals sorting π into γ. If multiple collections of such reversals exist, you may return any one.

## Sample Dataset

```
1 2 3 4 5 6 7 8 9 10
1 8 9 3 2 7 6 5 4 10
```

## Sample Output

```
2
4 9
2 5
```
