Hashing

Hashing is the process of mapping data (such as a string, number, or object) to a fixed-size value (usually a number or string) using a hash function. The resulting value is called a hash code or simply hash.

- Hash Function:
A hash function takes an input (or "key") and produces a fixed-size string or number (the hash value). The function should be designed so that small changes to the input produce drastically different outputs. The output, known as the hash value or hash code, represents the input data in a unique (ideally) and compressed form.

Properties of a good hash function:
- Deterministic: The same input will always produce the same hash value.
- Fast: It should be computationally efficient to compute the hash.
- Uniform Distribution: It should produce a uniform distribution of hash values to minimize collisions.
- Collision-resistant: It should minimize the chances of different inputs producing the same hash value.

Examples in PY:

1. Hashing with a Dictionary:
```
my_dict = {'apple': 1, 'banana': 2, 'cherry': 3}
print(my_dict['apple']) 
```

2. Hashing with Sets:
```
my_set = {1, 2, 3, 4}
print(3 in my_set)
```