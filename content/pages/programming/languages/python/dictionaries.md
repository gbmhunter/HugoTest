---
author: gbmhunter
date: 2018-11-24
draft: false
title: Dictionaries
type: page
url: /programming/languages/python/dictionaries
---

# Get A List Of Dictionary Keys

Calling `keys()` on a Python dictionary returns a `dict_keys` object. A `dict_keys` object is similar to a List, but you cannot index or modify the object.

```python
my_dict = {
    'foo': 1,
    'bar': 2
}

print(my_dict.keys())
# stdout: dict_keys(['foo', 'bar'])
```

If you really want a list, you can pass this `dict_keys` object into the `list()` constructor.

```python
keys_list = list(my_dict.keys())

print(keys_list)
# stdout: ['foo', 'bar']
```

# Iterating And Deleting Keys At The Same Time

Strictly speaking, you can't iterate over a dictionary and delete entries at the same time. However, you can quite easily create a copy of the dictionary keys, iterate of that, and delete entries from the dictionary, as shown in the following example:

```python
my_dict = {
    'foo': 1,
    'bar': 2
}
for key in list(my_dict.keys()):
    if key == 'foo':
        del my_dict[key]

print(my_dict)
# stdout: {'bar': 2}
```

This does not occur much overhead as you are just copying the keys, and not the values.

# del vs. pop()

Both `del` and `pop()` can be used to remove items from a dictionary:

```python
my_dict = {
    'foo': 1,
    'bar': 2
}

del my_dict['foo']
my_dict.pop('foo')
```

It is recommended to use `del` if you just want to delete the item, as it will be slightly faster than `pop()`. Use `pop()` if you want to capture the removed item, as `pop()` returns the removed item:

```python
my_item = my_dict.pop('foo')
```