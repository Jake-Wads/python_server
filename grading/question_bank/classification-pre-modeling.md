# Inter-Review

For the content up to, but not including modeling in classification.

## Inter-Review

- When working on a data science project, how do you organize your code, data,
  and notebooks?
- What is the difference between precision and recall? When would you choose one
  or the other?
- How do you handle missing values in a dataset?
- Below is some python code:

    ```python
    def f(l):
        l = [4, 5, 6]

    l = [1, 2, 3]
    f(l)
    print(l)
    ```

    Will the code run without error? If an error occurs, what type of error will
    it be? If the code runs, what will it output?

## Inter-Review

- What do you understand by the phrase "overloaded operator"?
- When should you scale your data?
- Below is some python code:

    ```python
    def f(l):
        l[0] = '?'

    l = [1, 2, 3]
    f(l)
    print(l)
    ```

    Will the code run without error? If an error occurs, what type of error will
    it be? If the code runs, what will it output?

## Inter-Review

- What's the difference between an argument and a parameter?
- What is a baseline model? What is a good choice for a baseline model in a
  classification problem?
- What does it mean to impute? Give examples of several imputation strategies.
- Below is a sample of a dataset:

    | coffee_size   |   hours_slept |   late_to_class |
    |:--------------|--------------:|----------------:|
    | s             |       6.09283 |               0 |
    | l             |       5.60105 |               1 |
    | m             |       5.66708 |               0 |
    | l             |       5.67625 |               1 |
    | xl            |       6.0306  |               1 |

    How would you visualize the relationship between each of the combination of
    2 variables? All 3 together?

## Inter-Review

Below is some python code:

```python
def f(x, l=[]):
    l.append(x)
    return l

l1 = f(1)
l2 = f(2)
l3 = f(3)

l2[-1] = '?'

print(l1)
print(l2)
print(l3)
```

Will the code run without error? If an error occurs, what type of error will
it be? If the code runs, what will it output?
