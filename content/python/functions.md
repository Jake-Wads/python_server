
# Functions

In this lesson, we'll discuss functions.

## Using Functions

We have already been using some of Python's built-in functions, but it is worthwhile to talk in more detail about how to use them.

To *run*, or *invoke* a function, we call the function by it's name, followed by a set of parenthesis. Inside the the parenthesis are any *arguments*. Note that writing the name of the function by itself (i.e. without parenthesis) will refer to the function itself, as opposed to running it.

- we've already used built-ins



```python
# a reference to the max function
max
```




    <function max>




```python
# calling the max function with 1 argument, a list of numbers
max([4, 2, 3, 1])
```




    4





The value our function produces, also called the *return value*, can be assigned to a variable, or used as an argument to another function



```python
maximum_number = max([4, 2, 3, 1])
print(maximum_number)
```

    4






```python
print('The max is: ' + str(max([4, 2, 3, 1])))
```

    The max is: 4


In the example above, the return value of the `max` function is being passed as an argument to the `str` function.

## Defining Functions

In addition to the built-in functions that are part of the Python language, we can define our own functions. To illustrate this, let's take a look at a very simple function that takes in a number and returns the number plus one.



```python
def increment(n):
    return n + 1
```

A function definition is made up of several parts:

- the keyword `def`
- the name of the function, in the example above, `increment`
- a set of parenthesis that define the inputs (or *parameters*) to the function
- the *body* of the function (everything that is indented after the first line defining the function)
- a *return statement* inside the body of the function

Whatever expression follows the `return` keyword will be the output of the function we've defined.

Let's take a look in more detail at how the function executes:



```python
six = increment(increment(increment(3)))

print(six)
```

    6


The first line is evaluated "inside-out", that is:

1. The increment function is called with the integer literal `3`
1. The output of the first call to the increment function is passed as an argument again to increment function. At this point, we are calling `increment` with `4`
1. The output from the previous step is again passed in to the `increment` function.
1. Finally, the output from the last call to the `increment` function is assigned to the variable `six`

We can imagine the code executing like this:



```python
six = increment(increment(increment(3)))
six = increment(increment(4))
six = increment(5)
six = 6
```

Let's look at another example of return values:



```python
def increment(n):
    return n + 1
    print('You will never see this')
    return n + 1

increment(3)
```




    4





When a `return` statement is encountered, the function will immediately return to where it is called. Put another way: a function only ever execute one return statement, and when a return statement is reached, no more code in the function will be executed.

## Arguments / Parameters

We have been using these terms already, but, formally:

- an *argument* is the value a function is called with
- a *parameter* is part of a function's definition; a placeholder for an argument

You can think of parameters as a special kind of variable that takes on the value of the function's arguments each time it is called.



```python
def add(a, b):
    result = a + b
    return result

x = 3
seven = add(x, 4)
```

Here `a` and `b` are the parameters of the `add` function.

On the last line above, when the function is called, the arguments are the value of the variable `x`, and `4`.

All of our examples thus far have contained both inputs and outputs, but these are actually both optional.



```python
def shout(message):
    print(message.upper() + '!!!')

return_value = shout('hey there')
print(return_value)
```

    HEY THERE!!!
    None


Here the `shout` function does not have a return value, and when we try to store it in a variable and print it, we see that the special value `None` is produced (recall that `None` indicates the absence of a value).



```python
def sayhello():
    print('Hey there!')

sayhello()
```

    Hey there!


Here the `sayhello` function takes in no inputs and produces no outputs. In fact, it would be an error to call this function with any arguments:



```python
sayhello(123)
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-12-6836f6e880ec> in <module>
    ----> 1 sayhello(123)


    TypeError: sayhello() takes 0 positional arguments but 1 was given


### Default Values

Functions can define default values for parameters, which allows you to either specify the argument or leave it out when the function is called.



```python
def sayhello(name='World', greeting='Hello'):
    return '{}, {}!'.format(greeting, name)

```

This function can be called with no arguments, and the specified default values will be used, or we can expliciltly pass a name, or a name and a greeting.



```python
sayhello()
```




    'Hello, World!'








```python
sayhello('Codeup')
```




    'Hello, Codeup!'








```python
sayhello('Codeup', 'Salutations')
```




    'Salutations, Codeup!'





### Keyword Arguments

Thus far, we have seen examples of functions that rely on *positional arguments*. Which string was assigned to `name` and which string was assigned to `greeting` depended on the position of the arguments, that is, which one was specified first and which one was second.

We can also specify arguments by their name.



```python
sayhello(greeting='Salutations', name='Codeup')
```




    'Salutations, Codeup!'





When arguments are specified in this way we say they are *keyword arguments*, and their order does not matter. The only restriction is that keyword arguments must come after any positional arguments.



```python
sayhello('Codeup', greeting='Salutations') # Okay
```




    'Salutations, Codeup!'








```python
sayhello(greeting='Salutations', 'Codeup') # ERROR!
```


      File "<ipython-input-19-efee9975a519>", line 1
        sayhello(greeting='Salutations', 'Codeup') # ERROR!
                                        ^
    SyntaxError: positional argument follows keyword argument





### Calling Functions

Python provides a way to *unpack* either a list or a dictionary to use them as function arguments.



```python
args = ['Codeup', 'Salutations']

sayhello(*args)
```




    'Salutations, Codeup!'





Using the `*` operator in front of a list makes as though we had used each element in the list as an argument to the function. The order of the elements in the list will be the order that they are passed as positional arguments to the function.

Similarly, we can unpack a dictionary to use it's values as keyword arguments to a function using the `**` operator.



```python
kwargs = {'greeting': 'Salutations', 'name': 'Codeup'}

sayhello(**kwargs)
```




    'Salutations, Codeup!'



## Function Scope

*Scope* is a term that describes where a variable can be referenced. If a variable is *in-scope*, then you can reference it, if it is *out-of-scope* then you cannot. Variables created inside of a function are *local* variables and are only in scope inside of the function they are defined in. Variables created outside of functions are *global* variables and are accessible inside of any function.

We can access global variables from anywhere:



```python
a_global_variable = 42

def somefunction():
    print('Inside the function: %s' % a_global_variable)

somefunction()
print('Outside the function: %s' % a_global_variable)
```

    Inside the function: 42
    Outside the function: 42


but variables defined within a function are only available in the function body:



```python
def somefunction():
    a_local_variable = 'pizza'
    print('Inside the function: %s' % a_local_variable)

somefunction()
print('Outside the function: %s' % a_local_variable)
```

    Inside the function: pizza



    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-23-038e8b55111b> in <module>
          4
          5 somefunction()
    ----> 6 print('Outside the function: %s' % a_local_variable)


    NameError: name 'a_local_variable' is not defined


When we try to print `a_local_variable` outside the function, it is no longer in-scope, and we get an error saying that the variable is not defined.

We can also define a local variable with the same name as a local variable. This is called *shadowing*. Under these circumstances, inside the function in which it is defined, the name will refer to the local variable, but the global variable will remain unchanged.



```python
n = 123

def somefunction():
    n = 10
    n = n - 3
    print('Inside the function, n == %s' % n)

print('Outside the function, n == %s' % n)
somefunction()
print('Outside the function, n == %s' % n)
```

    Outside the function, n == 123
    Inside the function, n == 7
    Outside the function, n == 123


## Lambda Functions

For functions that contain a single return statement in the function body, python provides a *lamdba* function. This is a function that accepts 0 or more inputs, and only executes a single return statement (note the `return` keyword is implied and not required).

Here are some examples of lambda functions:



```python
add_one = lambda n: n + 1
add_one(9)
```




    10








```python
square = lambda n: n ** 2
square(9)
```




    81





## Exercises

Create a file named `function_exercises.py` for this exercise. After creating each function specified below, write the necessary code in order to test your function.

1. Define a function named `is_two`. It should accept one input and return `True` if the passed input is either the number or the string `2`, `False` otherwise.
1. Define a function named `is_vowel`. It should return `True` if the passed string is a vowel, `False` otherwise.
1. Define a function named `is_consonant`. It should return `True` if the passed string is a consonant, `False` otherwise. Use your `is_vowel` function to accomplish this.
1. Define a function that accepts a string that is a word. The function should capitalize the first letter of the word if the word starts with a consonant.
1. Define a function named `calculate_tip`. It should accept a tip percentage (a number between 0 and 1) and the bill total, and return the amount to tip.
1. Define a function named `apply_discount`. It should accept a original price, and a discount percentage, and return the price after the discount is applied.
1. Define a function named `handle_commas`. It should accept a string that is a number that contains commas in it as input, and return a number as output.
1. Define a function named `get_letter_grade`. It should accept a number and return the letter grade associated with that number (A-F).
1. Define a function named `remove_vowels` that accepts a string and returns a string with all the vowels removed.
1. Define a function named `normalize_name`. It should accept a string and return a valid python identifier, that is:
    - anything that is not a valid python identifier should be removed
    - leading and trailing whitespace should be removed
    - everything should be lowercase
    - spaces should be replaced with underscores
    - for example:
        - `Name` will become `name`
        - `First Name  ` will become `first_name`
        - `% Completed` will become `completed`
1. Write a function named `cumulative_sum` that accepts a list of numbers and returns a list that is the cumulative sum of the numbers in the list.
    - `cumulative_sum([1, 1, 1])` returns `[1, 2, 3]`
    - `cumulative_sum([1, 2, 3, 4])` returns `[1, 3, 6, 10]`

### Additional Exercise
- Once you've completed the above exercises, follow the directions from https://gist.github.com/zgulde/ec8ed80ad8216905cda83d5645c60886 in order to thouroughly comment your code to explain your code.

### Bonus

1. Create a function named `twelveto24`. It should accept a string in the format `10:45am` or `4:30pm` and return a string that is the representation of the time in a 24-hour format. **Bonus** write a function that does the opposite.
1. Create a function named `col_index`. It should accept a spreadsheet column name, and return the index number of the column.
    - `col_index('A')` returns `1`
    - `col_index('B')` returns `2`
    - `col_index('AA')` returns `27`
