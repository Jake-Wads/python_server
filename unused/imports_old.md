# Imports

There are 3 main places we can import from:

- The Python standard library. This comes with the Python language, and no
  special action is needed in order to use it.
- 3rd party libraries. These require installation either through `conda` or
  `pip`.
- Our own code. We can break our code into separate files and use imports to use
  code from one file in another.

Let's take a look at some examples:

The simplest way to import a *module* is to use the `import` keyword and the
name of the module.

```python
import time
```

Once we have imported the module, we can reference variables or functions
defined in the module using a `.` after the module's name.

```python
time.sleep(2)
print('All Done!')
```
We can also rename a module when we import it. This allows us to refer to the
module with a different (often shorter) name.

```python
import time as t

t.sleep(2)
print('All Done!')
```

In addition to importing an entire module, we can import individual functions or
variables using the `from` and `import` keywords.

```python
from time import sleep

sleep(2)
print('All Done!')
```

    All Done!

Like importing a module, you can rename individual functions when they are
imported.

```python
from time import sleep as wait

wait(2)
print('All Done!')
```

    All Done!


## Importing From Your Own Code

To import from code that you have written, simply reference the name of the file
without the `.py` extension.

!!!warning "Naming Conventions"
    In order to import from another file, that file's name (i.e. everything
    before the `.py` extension) must be a valid python identifier, that is, you
    could use it as a variable name.

We have a file, `util.py`, in the same directory as the script we are running.

`util.py` has the following contents:

```python
def sayhello():
    print("Hello, World!")
```

We can import our file like this:

```python
import util

util.sayhello()
```

    Hello, World!


When a module is imported, all the code in that file is executed. Sometimes this
can produce some undesired side effects, so a best practice is to only have
*definitions* inside of a module. If the module contains *procedural code*, that
is, code that does something, we can place it inside of an `if` statement like
this:

```python
if __name__ == '__main__':
    print('Hello, World!')
```

    Hello, World!


The `__name__` variable is a special variable that is set by python. It's value
will be `__main__` when the module is being run directly, but *not* when the
module is being imported. This way you can write files that do something when
you run them directly, but can also be imported from without producing side
effects.

## Further Reading

- [Python Standard Library](https://docs.python.org/3/library/index.html)

## Exercises

Create a file named `import_exercises.py` to do your work in.

1. Import and test 3 of the functions from your functions exercise file.

    Import each function in a different way:

    - import the module and refer to the function with the `.` syntax
    - use `from` to import the function directly
    - use `from` and give the function a different name

For the following exercises, read about and use the [`itertools`
module](https://docs.python.org/3/library/itertools.html) from the standard
library to help you solve the problem.

1. How many different ways can you combine the letters from "abc" with the
   numbers 1, 2, and 3?
1. How many different ways can you combine two of the letters from "abcd"?

Save [this
file](https://gist.githubusercontent.com/ryanorsinger/f77e5ec94dbe14e21771/raw/d4a1f916723ca69ac99fdcab48746c6682bf4530/profiles.json)
as `profiles.json` inside of your exercises directory. Use the `load` function
from the `json` module to open this file, it will produce a list of
dictionaries. Using this data, write some code that calculates and outputs the
following information:

- Total number of users
- Number of active users
- Number of inactive users
- Grand total of balances for all users
- Average balance per user
- User with the lowest balance
- User with the highest balance
- Most common favorite fruit
- Least most common favorite fruit
- Total number of unread messages for all users
