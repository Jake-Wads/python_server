<style>ol li { padding-bottom: 4em; /*room to write*/ }</style>

# Python Assessment

## Instructions

1. Write your name at the top of the paper.
1. Answer all the questions below.

## Questions

1. What is the difference between a function that `print`s it's result, and one
   that `return`s it's result?

1. Name 2 differences between dictionaries and lists in Python.

1. What is the difference between `pandas` and `numpy`?

1. What is the difference between `seaborn` and `matplotlib`?

1. What is the output of the following code?

    ```python
    def myincrement(n):
        return n + 1 if n > 5 else n - 1

    numbers = [myincrement(n) for n in range(11) if n % 3 == 0]
    print(numbers)
    ```
