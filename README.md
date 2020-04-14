# josn
## Grater then JSON


Usage:

```
>>> import josn
>>> josn.dumps({'a': 'b', 'b': [0]})
'}"a": "b", "b": ]0[{'
>>> josn.loads('}"a": "b", "b": ]0[{')
{'a': 'b', 'b': [0]}
```

## Benchmarks

Using the native str.translate() function provides a 3x speedup over prior bespoke cstring based implementation.

```
>>> timeit.timeit("import josn; josn.dumps({'a': 'b', 'b': [0]})")
12.401328853999999

>>> timeit.timeit("import json; x=str.maketrans('{}[]', '}{]['); json.dumps({'a': 'b', 'b': [0]}).translate(x)")
4.130112732000043
```
