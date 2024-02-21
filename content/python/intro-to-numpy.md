# Numpy

Numpy is a library for representing and working with large and multi-dimensional
arrays. Most other libraries in the data-science ecosystem depend on numpy,
making it one of the fundamental data science libraries.

Numpy provides a number of useful tools for scientific programming, and in
this lesson, we'll take a look at some of the most common.

Convention is to import the `numpy` module as `np`.

```python
import numpy as np
```

## Indexing

Numpy provides an array type that goes above and beyond what Python's
built-in lists can do.

We can create a numpy array by passing a list to the `np.array` function:

```python
a = np.array([1, 2, 3])
a
```

    array([1, 2, 3])

We can create a multi-dimensional array by passing a list of lists to the
`array` function

```python
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
matrix
```

    array([[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]])

Referencing elements in numpy arrays at it's most basic is the same as
referencing elements in Python lists.

```python
a[0]
```

    1

```python
print('a    == {}'.format(a))
print('a[0] == {}'.format(a[0]))
print('a[1] == {}'.format(a[1]))
print('a[2] == {}'.format(a[2]))
```

    a    == [1 2 3]
    a[0] == 1
    a[1] == 2
    a[2] == 3

However, multidimensional numpy arrays are easier to index into. To obtain the
element at the second column in the second row, we would write:

```python
matrix[1, 1]
```

    5

To get the first 2 elements of the last 2 rows:

```python
matrix[1:, :2]
```

    array([[4, 5],
           [7, 8]])

Arrays can also be indexed with a boolean sequence used to indicate which
values should be included in the resulting array.

```python
should_include_elements = [True, False, True]
a[should_include_elements]
```

    array([1, 3])

Note that the boolean sequence must the the same length as the array being indexed.

## Vectorized Operations

Another useful feature of numpy arrays is vectorized operations.

If we wanted to add 1 to every element in a list, without numpy, we can't
simply add 1 to the list, as that will result in a `TypeError`.

```python
original_array = [1, 2, 3, 4, 5]
try:
    original_array + 1
except TypeError as e:
    print('An Error Occured!')
    print(f'TypeError: {e}')
```

    An Error Occured!
    TypeError: can only concatenate list (not "int") to list

Instead, we might write a `for` loop or a list comprehension:

```python
original_array = [1, 2, 3, 4, 5]
array_with_one_added = []
for n in original_array:
    array_with_one_added.append(n + 1)
print(array_with_one_added)
```

    [2, 3, 4, 5, 6]

```python
original_array = [1, 2, 3, 4, 5]
array_with_one_added = [n + 1 for n in original_array]
print(array_with_one_added)
```

    [2, 3, 4, 5, 6]

Vectorizing operations means that operations are automatically applied to
every element in a vector, which in our case will be a numpy array. So if we
are working with a numpy array, we **can** simply add 1:

```python
original_array = np.array([1, 2, 3, 4, 5])
original_array + 1
```

    array([2, 3, 4, 5, 6])

This works the same way for the other basic arithmatic operators as well.

```python
my_array = np.array([-3, 0, 3, 16])

print('my_array      == {}'.format(my_array))
print('my_array - 5  == {}'.format(my_array - 5))
print('my_array * 4  == {}'.format(my_array * 4))
print('my_array / 2  == {}'.format(my_array / 2))
print('my_array ** 2 == {}'.format(my_array ** 2))
print('my_array % 2  == {}'.format(my_array % 2))
```

    my_array      == [-3  0  3 16]
    my_array - 5  == [-8 -5 -2 11]
    my_array * 4  == [-12   0  12  64]
    my_array / 2  == [-1.5  0.   1.5  8. ]
    my_array ** 2 == [  9   0   9 256]
    my_array % 2  == [1 0 1 0]

Not only are the arithmatic operators vectorized, but the same applies to
the comparison operators.

```python
my_array = np.array([-3, 0, 3, 16])

print('my_array       == {}'.format(my_array))
print('my_array == -3 == {}'.format(my_array == -3))
print('my_array >= 0  == {}'.format(my_array >= 0))
print('my_array < 10  == {}'.format(my_array < 10))
```

    my_array       == [-3  0  3 16]
    my_array == -3 == [ True False False False]
    my_array >= 0  == [False  True  True  True]
    my_array < 10  == [ True  True  True False]

Knowing what we know about indexing numpy arrays, we can use the comparison
operators to select a certain subset of an array.

For example, we can get all the positive numbers in `my_array` like so:

```python
my_array[my_array > 0]
```

    array([ 3, 16])

### In-Depth Example

As another example, we could obtain all the even numbers like this:

```python
my_array[my_array % 2 == 0]
```

    array([ 0, 16])

To better understand how this is all working let's go through the above
example in a little more detail.

The first expression that gets evaluated is this:

```python
my_array % 2
```

    array([1, 0, 1, 0])

Which results in an array of 1s and 0s. Then the array of 1s and 0s is
compared to 0 with the `==` operator, producing an array of True or False
values.

```python
result = my_array % 2
result == 0
```

    array([False,  True, False,  True])

Lastly, we use this array of boolean values to index into the original
array, giving us only the values that are evenly divisible by 2.

```python
step_1 = my_array % 2
step_2 = step_1 == 0
step_3 = my_array[step_2]

step_3
```

    array([ 0, 16])

Put another way, here is how the expression is evaluated:

```python
print('1. my_array[my_array % 2 == 0]')
print('    - the original expression')
print('2. my_array[{} % 2 == 0]'.format(my_array))
print('    - variable substitution')
print('3. my_array[{} == 0]'.format(my_array % 2))
print('    - result of performing the vectorized modulus 2')
print('4. my_array[{}]'.format(my_array % 2 == 0))
print('    - result of comparing to 0')
print('5. {}[{}]'.format(my_array, my_array % 2 == 0))
print('    - variable substitution')
print('6. {}'.format(my_array[my_array % 2 == 0]))
print('    - our final result')
```

    1. my_array[my_array % 2 == 0]
        - the original expression
    2. my_array[[-3  0  3 16] % 2 == 0]
        - variable substitution
    3. my_array[[1 0 1 0] == 0]
        - result of performing the vectorized modulus 2
    4. my_array[[False  True False  True]]
        - result of comparing to 0
    5. [-3  0  3 16][[False  True False  True]]
        - variable substitution
    6. [ 0 16]
        - our final result

## Array Creation

Numpy provides several methods for creating arrays, we'll take a look at several
of them.

`np.random.randn` can be used to create an array of specified length of
random numbers drawn from the standard normal distribution.

```python
np.random.randn(10)
```

    array([-1.63526513,  0.4437877 , -0.026761  ,  0.91365701, -0.19552803,
            0.65391594, -1.3590744 ,  0.01449514, -1.22718349, -0.48087435])

We can also pass a second argument to this function to define the shape of a
two dimensional array.

```python
np.random.randn(3, 4)
```

    array([[-0.67528597, -1.44504125,  0.63126959,  1.0732026 ],
           [ 1.58057546,  0.67135057,  1.49905094,  0.26424952],
           [-0.21247359,  0.38302284,  0.51563093,  0.23534614]])

If we wish to draw from a normal distribution with mean $\mu$ and standard
deviation $\sigma$, we'll need to apply some arithmetic. Recall that to
convert from the standard normal distribution, we'll need to multiply by the
standard deviation, and add the mean.

```python
mu = 100
sigma = 30

sigma * np.random.randn(20) + mu
```

    array([ 34.46131222,  33.34454853,  77.63942809, 129.42668519,
            62.22808303,  92.14175929,  98.24106166,  81.90569207,
            69.34275465, 127.88917976,  74.47590005,  65.20865997,
            93.86237794,  63.36017475,  88.72409051, 126.61874322,
           113.73558219, 156.98882589,  84.47295832, 120.03330185])

The `zeros` and `ones` functions provide the ability to create arrays of a
specified size full or either 0s or 1s, and the `full` function allows us to
create an array of the specified size with a default value.

```python
print('np.zeros(3)    == {}'.format(np.zeros(3)))
print('np.ones(3)     == {}'.format(np.ones(3)))
print('np.full(3, 17) == {}'.format(np.full(3, 17)))
```

    np.zeros(3)    == [0. 0. 0.]
    np.ones(3)     == [1. 1. 1.]
    np.full(3, 17) == [17 17 17]

We can also use these methods to create multi-dimensional arrays by passing
a tuple of the dimensions of the desired array, instead of a single integer
value.

```python
np.zeros((2, 3))
```

    array([[0., 0., 0.],
           [0., 0., 0.]])

Numpy's `arange` function is very similar to python's builtin `range`
function. It can take a single argument and generate a range from zero up to,
but not including, the passed number.

```python
np.arange(4)
```

    array([0, 1, 2, 3])

We can also specify a starting point for the range:

```python
np.arange(1, 4)
```

    array([1, 2, 3])

As well as a step:

```python
np.arange(1, 4, 2)
```

    array([1, 3])

Unlike python's builtin `range`, numpy's `arange` can handle decimal numbers

```python
np.arange(3, 5, 0.5)
```

    array([3. , 3.5, 4. , 4.5])

The `linspace` method creates a range of numbers between a minimum and a
maximum, with a set number of elements.

```python
print('min: 1, max: 4, length = 4 -- {}'.format(np.linspace(1, 4, 4)))
print('min: 1, max: 4, length = 7 -- {} '.format(np.linspace(1, 4, 7)))
```

    min: 1, max: 4, length = 4 -- [1. 2. 3. 4.]
    min: 1, max: 4, length = 7 -- [1.  1.5 2.  2.5 3.  3.5 4. ]

Note that here the maximum is inclusive.

## Array Methods

Numpy arrays also come with built-in methods to make many mathematical
operations easier.

```
a = np.array([1, 2, 3, 4, 5])
```

Some of the most common are:

- `.min`

    ```python
    a.min()
    ```

        1

- `.max`

    ```python
    a.max()
    ```

        5

- `.mean`

    ```python
    a.mean()
    ```

        3.0

- `.sum`

    ```python
    a.sum()
    ```

        15

- `.std`: standard deviation

    ```python
    a.std()
    ```

        1.4142135623730951

## Further Reading

- [Numpy Array Methods](https://docs.scipy.org/doc/numpy/reference/arrays.ndarray.html#array-methods)

## Exercises

Set up a new local and remote called `ds-libraries-exercises` for this module. 

Let's review the steps to get setup. 

- Create a new repository named `ds-libraries-exercises` on GitHub.com 
- Copy the SSH link for this repository 
- In the terminal, navigate to `~/codeup-data-science`
- Clone your remote repository to your local using: `git clone` + the link you copied
- Create a `.gitignore`
- Create a README.md file that outlines the purpose of this repository
- Add, commit, and push these two files. 
- Go to GitHub.com and very that the `.gitignore` and README.md are there


In your new repo, create a file named `numpy_exercises.py` or `numpy_exercises.ipynb` for this exercise.

Use the following code for the questions below:

```
a = np.array([4, 10, 12, 23, -2, -1, 0, 0, 0, -6, 3, -7])
```

1. How many negative numbers are there?

1. How many positive numbers are there?

1. How many even positive numbers are there?

1. If you were to add 3 to each data point, how many positive numbers would
   there be?

1. If you squared each number, what would the new mean and standard deviation
   be?

1. A common statistical operation on a dataset is **centering**. This means to
   adjust the data such that the mean of the data is 0. This is done by
   subtracting the mean from each data point. Center the data set. See [this link](https://www.theanalysisfactor.com/centering-and-standardizing-predictors/) for more on centering.

1. Calculate the z-score for each data point. Recall that the z-score is given
   by:

    $$
    Z = \frac{x - \mu}{\sigma}
    $$

1. Copy the setup and exercise directions from [More Numpy Practice](https://gist.github.com/ryanorsinger/c4cf5a64ec33c014ff2e56951bc8a42d) into your `numpy_exercises.py` and add your solutions.

** Awesome Bonus **
For much more practice with numpy, go to `https://github.com/rougier/numpy-100` and clone the repo down to your laptop. 

To clone a repository:

- Copy the SSH address of the repository
- In your terminal, run `cd ~/codeup-data-science` (goes to your codeup-data-science folder)
- Run `git clone git@github.com:rougier/numpy-100.git` (clones down Rougeir's files)
- Run `cd numpy-100` (move into the numpy folder)
- Run `git remote remove origin` (so you won't accidentally try to push your work to Rougier's repo)

Congratulations! You have cloned Rougier's 100 numpy exercises to your computer. Now you need to make a new, blank, repository on GitHub.

- Go to `https://github.com/new` to make a new repo. Name it `numpy-100`.
- DO NOT check any check boxes. We need a blank, empty repo.
- Finally, follow the directions to "push an existing repository from the command line" so that you can push up your changes to your own account. 
- Now do work, add it, commit it, and push it!
