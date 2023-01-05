# Sorting words using a custom alphabet

From [stack overflow](https://stackoverflow.com/a/26579479).

```
alphabet = "bafmxpzv"
a = ['af', 'ax', 'am', 'ab', 'zvpmf']
sorted(a, key=lambda word: [alphabet.index(c) for c in word])
```

Out: `['ab', 'af', 'am', 'ax', 'zvpmf']`

## About `sorted`

`sorted` enables a wide range of custom sorting. The sorted function has three optional arguments: cmp, key, and reverse:

* `cmp` is good for complex sorting tasks. If specified, `cmp` should be a function that takes two arguments. It should return a negative, zero or positive number depending on whether the first argument is considered smaller than, equal to, or larger than the second argument. For this case, `cmp` is overkill.

* `key`, if spedified, should be a function that takes one argument and returns something that python knows natively how to sort. In this case, key returns a list of the indices of each of the word's characters in the alphabet. In this case, `key` returns the index of a letter in alphabet.

* `reverse`, if true, reverses the sort-order.
