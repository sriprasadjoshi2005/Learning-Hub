---
title: Lists, Tuples, Sets and Dictionaries
level: intermediate
---

Programming languages provide different collection types for storing and organising data. Lists, tuples, sets and dictionaries represent common structures used in general-purpose programming.

## 1. Lists

A list is an ordered collection of elements.

Characteristics:

- Maintains element order.
- Can contain duplicate values.
- Often supports modification.
- Can store multiple data types in flexible languages.

Example:

FRUITS = ["Apple", "Mango", "Orange"]

Common operations:

- Append an element.
- Insert an element.
- Remove an element.
- Access an element.
- Sort elements.
- Find the length.

Lists are useful when a collection must preserve order and allow updates.

## 2. Tuples

A tuple is an ordered collection that is commonly immutable in languages such as Python.

Example:

COORDINATE = (10, 20)

Characteristics:

- Maintains order.
- Allows duplicate values.
- Supports indexing.
- Cannot be directly modified after creation in Python.

Tuples are useful for representing fixed collections of related values.

## 3. Sets

A set is a collection of distinct elements.

Example:

NUMBERS = {2, 4, 6, 8}

Characteristics:

- Does not contain duplicate elements.
- Supports membership testing.
- Supports mathematical set operations.
- Does not guarantee a meaningful positional order in Python.

Common set operations:

**Union:** Combines elements from two sets.

A union B

**Intersection:** Returns common elements.

A intersection B

**Difference:** Returns elements present in A but absent from B.

A difference B

**Symmetric Difference:** Returns elements present in either set but not both.

## 4. Dictionaries

A dictionary stores information as key-value pairs.

Example:

STUDENT = {
    "name": "Ravi",
    "age": 20,
    "course": "Computer Science"
}

Characteristics:

- Stores key-value associations.
- Keys must be unique.
- Supports efficient key-based retrieval in typical hash-table implementations.
- Values can be updated.
- Dictionaries maintain insertion order in modern Python.

## 5. Comparison of Collection Types

| Feature | List | Tuple | Set | Dictionary |
|---|---|---|---|---|
| Ordered | Yes | Yes | No positional order guarantee | Yes in modern Python |
| Duplicates | Allowed | Allowed | Not allowed | Keys are unique |
| Mutable in Python | Yes | No | Yes | Yes |
| Access method | Index | Index | Membership | Key |
| Main purpose | General sequence | Fixed sequence | Unique elements | Key-value mapping |

## 6. List Operations

Example:

NUMBERS = [10, 20, 30]

Append 40:

NUMBERS.append(40)

Insert 15 at index 1:

NUMBERS.insert(1, 15)

Remove 20:

NUMBERS.remove(20)

These are Python-style examples.

## 7. Dictionary Operations

Example:

STUDENT = {
    "name": "Ravi",
    "marks": 85
}

Access:

STUDENT["name"]

Update:

STUDENT["marks"] = 90

Add:

STUDENT["grade"] = "A"

Dictionaries are useful for records, configuration data and structured information.

## 8. Choosing the Appropriate Collection

Use a list when:

- Order matters.
- Duplicates are allowed.
- Elements may change.

Use a tuple when:

- A fixed sequence is needed.
- Direct modification should not be allowed.

Use a set when:

- Unique values are required.
- Membership testing and set operations are important.

Use a dictionary when:

- Values must be retrieved using meaningful keys.
- Data is naturally represented through key-value relationships.

## Common Exam Traps

- Lists are ordered and mutable in Python.
- Tuples are ordered and immutable in Python.
- Sets contain unique elements.
- Dictionaries store key-value pairs.
- Dictionary keys must be unique.
- Set operations correspond to mathematical set operations.
- Collection behaviour can vary across programming languages.

## Quiz

1. Which Python collection is designed to store unique elements?

- [ ] List.
- [ ] Tuple.
- [x] Set.
- [ ] Dictionary.

> Sets automatically maintain distinct elements and support mathematical set operations.

2. Which collection is commonly used to store key-value pairs?

- [ ] Tuple.
- [ ] List.
- [ ] Set.
- [x] Dictionary.

> A dictionary associates unique keys with corresponding values.

3. Which Python collection is ordered and immutable?

- [ ] List.
- [x] Tuple.
- [ ] Set.
- [ ] Mutable dictionary.

> A tuple preserves element order and does not support direct modification after creation.