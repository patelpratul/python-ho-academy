# Logical Operations in Python

## Introduction

Logical operators in Python are used to manipulate and combine Boolean values. These operators allow you to perform logical operations such as AND, OR, and NOT.

## List of Logical Operators

1. **AND (and):** Returns `True` if both operands are `True`.
2. **OR (or):** Returns `True` if at least one of the operands is `True`.
3. **NOT (not):** Returns the opposite Boolean value of the operand.

## Examples

### AND Operator

```python
x = True
y = False
result = x and y
# result will be False
```

### OR Operator

```python
a = True
b = False
result = a or b
# result will be True
```
### Exercise

```python
x = True
y = False

and_result = x and y
or_result = x or y
not_result_x = not x
not_result_y = not y

print("x and y:", and_result)
print("x or y:", or_result)
print("not x:", not_result_x)
print("not y:", not_result_y)
```
