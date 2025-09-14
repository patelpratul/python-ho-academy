# Relational Operations in Python

## Introduction

Relational operators in Python are used to compare two values and determine the relationship between them. These operators return a Boolean result, which is either `True` or `False`.

## List of Relational Operators

1. **Equal to (==):** Checks if two values are equal.

2. **Not equal to (!=):** Checks if two values are not equal.

3. **Greater than (>):** Checks if the left operand is greater than the right operand.

4. **Less than (<):** Checks if the left operand is less than the right operand.

5. **Greater than or equal to (>=):** Checks if the left operand is greater than or equal to the right operand.

6. **Less than or equal to (<=):** Checks if the left operand is less than or equal to the right operand.

## Examples

### Equal to

```python
a = 5
b = 5
result = a == b
# result will be True
```

### Not equal to

```python
x = 10
y = 7
result = x != y
# result will be True
```

### Exercise
Compare the values of a and b using the following comparison operators: <, >, <=, >=, ==, and !=.
Print the results of each comparison.

```python
a = 10
b = 5

less_than = a < b
greater_than = a > b
less_than_or_equal = a <= b
greater_than_or_equal = a >= b
equal = a == b
not_equal = a != b

print("a < b:", less_than)
print("a > b:", greater_than)
print("a <= b:", less_than_or_equal)
print("a >= b:", greater_than_or_equal)
print("a == b:", equal)
print("a != b:", not_equal)
```
