# Problem

In a weighted tree, each edge is assigned a (usually positive) number, called its weight. The distance between two nodes in a weighted tree becomes the sum of the weights along the unique path connecting the nodes.

To generalize Newick format to the case of a weighted tree T, during our repeated "key step," if leaves v1,v2,…,vn are neighbors in T, and all these leaves are incident to u, then we replace u with (v1:d1,v2:d2,…,vn:dn)u, where di is now the weight on the edge {vi,u}.

**Given**: A collection of n weighted trees (n≤40) in Newick format, with each tree containing at most 200 nodes; each tree Tk is followed by a pair of nodes xk and yk in Tk.

**Return**: A collection of n numbers, for which the kth number represents the distance between xk and yk in Tk.

## Sample Dataset

```
(dog:42,cat:33);
cat dog

((dog:4,cat:3):74,robot:98,elephant:58);
dog elephant
```

## Sample Output

```
75 136
```
