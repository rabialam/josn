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
