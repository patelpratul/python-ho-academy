# Membership Operations in Python

## Introduction

Membership operators in Python are used to check whether a value is present in a sequence or collection, such as a list, tuple, or string. The membership operators are "in" and "not in."

## List of Membership Operators

1. **in:** Returns `True` if the left operand is found in the sequence on the right.
2. **not in:** Returns `True` if the left operand is not found in the sequence on the right.

### Examples

#### in Operator

```python
fruits = ["apple", "banana", "cherry"]
result = "banana" in fruits
# result will be True
```

#### not in Operator

```python
colors = ["red", "green", "blue"]
result = "yellow" not in colors
# result will be True
```

### Exercise
```python
my_list = [1, 2, 3, 4, 5]

# Membership operators
element_in_list = 3 in my_list
element_not_in_list = 6 not in my_list

print("a is my_list:", is_same_object)
print("b is not my_list:", is_not_same_object)
print("3 in my_list:", element_in_list)
print("6 not in my_list:", element_not_in_list)

```
