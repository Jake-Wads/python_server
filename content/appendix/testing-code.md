# Testing

**Unit testing** involves writing short snippets of code that test other small
bits of code. We've seen examples of both doctests and `assert`s to achieve
this.

Test Driven Development (or TDD) is the practice of writing a test for code
before writing the code itself. This is very similar to what we did for the
function exercises where I wrote the code that tests the function before writing
the function itself.

There is much more to this practice that is pertinent to software developers,
but is not important enough to data science that we will spend time on it in
this course.

## Where do the `assert`s go?

There are several answers to this question.

- Don't use asserts, use
  [doctests](https://docs.python.org/3/library/doctest.html) instead.

    That is, instead of writing asserts to test your code, write examples in
    doctest format.

    Doctests look like what you would see in an interactive python session. They
    show the code that is run and the expected output.

    ```
    >>> 1 + 1
    2
    ```

    When using doctests, python will run the code after the `>>>` and check if
    the code's actual output matches with what you have specified.

    Doctests can go in one of several places:

    - Inside of a docstring for a function.

        ```python
        def increment(n):
            '''
            Increment the passed number.

            >>> increment(3)
            4
            >>> increment(increment(3))
            5
            '''
            return n + 1
        ```

    - Inside of the documentation for a module.

        !!!tip "Module Docstring"
            Like functions, if the first thing in a python module (i.e. a python
            file) is a string literal, the contents of that string will be used
            as the documentation for the module. Each module can only have one
            docstring, and it must be the first thing at the top of the file.

        ```python
        '''
        This module defines two functions, increment and decrement to add and
        subtract one from passed numbers.

        >>> increment(3)
        4
        >>> increment(increment(3))
        5
        >>> decrement(2)
        1
        >>> decrement(decrement(2))
        0
        >>> decrement(increment(2))
        2
        '''

        def increment(n):
            return n + 1
        def decrement(n):
            return n - 1
        ```

    - An external `.txt` file. This can be useful to seperate longer
      documentation from your source code.

    Regardless of where the docstring tests are, you can run them like this:

    ```
    python -m doctest FILENAME
    ```

    Where `FILENAME` is the name of the file that contains the doctests (be it a
    `.txt` file or a `.py` file).

- Write asserts in `if __name__ == '__main__'`

    For example, your code might look like:

    ```python
    def sayhello():
        return "Hello, World!"

    # ... more function definitions ...

    if __name__ == "__main__":
        assert sayhello() == "Hello, World!"
        # ... more asserts ...
    ```

    The `if __name__ == '__main__':` condition will only run code when the given
    module is run directly (i.e. not imported from). This allows you to cleanly
    seperate your test code from your function definitions.

- [`unittest`](https://docs.python.org/3/library/unittest.html)

    The `unittest` module is part of the python standard library, so is the
    "standard" way to unit-test your code.

- [`pytest`](https://docs.pytest.org/en/latest/)

    `pytest` is a third-party library, but it can do more fancy things with
    `assert` statements, like showing the actual values that caused failed
    assertions.
