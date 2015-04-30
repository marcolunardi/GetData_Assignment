#### Pair Problem

Write a function that will take two arguments, both lists of lists representing tables of data. The function will combine the two tables into one.Each of the inner lists represents a row of data, with the first element being the "key" for that row.

For example, your function could take these two lists of lists:

```python
[[27, 'dog', 5],
 [19, 'cat', 9],
 [33, 'bat', 3]]

[[14, 8, 'elf'],
 [33, 7, 'fat'],
 [27, 2, 'rat']]
```

In this case, your function could return this result:

```python
[[27, 'dog', 5, 2, 'rat'],
 [33, 'bat', 3, 7, 'fat']]
```

Get a solution working. Then consider how your solution would perform if the inputs were very large. Can you improve the performance of your solution?
