# NumPy Introduction

#### What is NumPy and why should you care?

NumPy is the fundamental package for scientific computing with Python. It is the *de-facto* linear algebra library for Python and is the computational tool behind many other data science tools including pandas.

- Provides an implementation of a high-performance multi-dimensional array object
- Provides a large toolbox of linear algebra methods. 
- NumPy is *super fast*. Use `%timeit` in Jupyter to show how fast an operation takes to run.

#### What problems does does Numpy solve for us?

- Native lists in Python don't do linear algebra out of the box. For example, `[1, 2, 3] * 2` is `[1, 2, 3, 1, 2, 3]` because the `+` and `*` operators in Python perform concatenation, not linear algebra.`x
  - Optimized scalar, vector, and matrix arithmetic
- **Scalar addition, subtraction, and multiplication**. Given `x = np.array([1, 2, 3])
  - `x + 2` returns `np.array([3, 4, 5])`
  - `x - 2` returns `np.array([-1, 0, 1])`
  - `x * 2` returns `np.array([2, 4, 6])`
- **Vector addition** `np.array([1, 2]) + np.array([1, 2])` is `np.array([2, 4])`
- **Vector subtraction** `np.array([1, 2]) - np.array([1, 2])` is `np.array([0, 0])`
- **Vector multiplication** `np.array([1, 2]) * np.array([1, 2])` is `np.array([1, 4])`

## Vectorized Operations == awesome

Given a task like "write a function named `add_one_to_each_element` that takes in a list of numbers and returns the list with one added to each number", the implementation is simple, direct, and doesn't worry about loops.

```python
import numpy as np
def add_one_to_each_element(numbers):
    return np.array(numbers) + 1
```









Define a function named `multiply_from_one_to(x)`

```python
def multiply_from_one_to_x(x):
    array = np.arange(1, x + 1)
    return array.prod()
```

### Boolean Masking with NumPy

Boolean masking allows us to extract, modify, count, and manipulate values in an array based on criteria. We can make and apply boolean masks with NumPy and pandas in order to solve many tasks that imperative code has historically solved with **selection** and **iteration**. Here is a quick example.

````python
# The
x = np.array([-3, -2, -1, 0, 1, 2, 3])
mask = x > 0
# mask holds the array([False, False, False, False,  True,  True,  True])
````

A boolean mask is an array of booleans (`True` or `False`). This array of booleans "turns on" or "turns off" elements from the original list when we apply the mask. See below:

```python
# get the number of positive elements in the above list
# We're summing the Trues as 1 and the Falses are seen as 0
# In this way, .sum on an array of booleans counts the number of True values
mask.sum()

# show only the elements that are 
x[mask] # returns np.array([1, 2, 3])

# Multi-step problems like "Sum all of the positive numbers becomes
x[mask].sum()
```



Further links

https://numpy.org/doc/1.16/user/basics.broadcasting.html

https://numpy.org/devdocs/user/basics.types.html