## Functions

<img alt="function diagram" src="https://cdn.glitch.com/02073022-2df9-4d98-be8d-abf50f7837e5%2Fsmall-function.png?1529106496333" >

A function is a reusable block of code. Functions are procedures. Think of them as spells.

Functions either **do** something like a command or **transform** values like a math operator

In addition to built-in functions of the language and libraries, we built our own functions 

Effectively naming our functions is critical because they become the *language of the solution*.

#### Anatomy of a Function Definition

1. The `def` keyword
2. The name of the function (use snake_case). Name your functions verbs and verb phrases.
3. Parameters in parentheses (these will hold the inputs coming into the function)
4. The body of the function (This is the procedure the function executes)
5. `return` hands value(s) back out of the function and exits. No return returns `None`

```python
def increment(x):
    return x + 1
```

#### The Function "Two-Step"

- Step 1 - Define the function. Functions transform inputs into outputs, following a procedure.
- Step 2 - Call, run, invoke, or execute the function. `increment(5)` returns `6`

#### Function Vocabulary

- "Call", "invoke", or "execute" all mean to run a function
- Parameter - In the above example function, `x` is the placeholder for inputs.
- Argument - In the example `times_two_plus_three(5)`, the `5` is the input going into the function.

#### The value of return values

```python
def return_two():
    return 2

def print_two():
    print(2)
```

Try out `x = return_two()` then `print(x)` then `print(type(x))`

Then compare to `y = print_two()`, `print(y)`, `print(type(y))`

##### Lambda Functions

Lambdas are anonymous functions. In Python, they're defined on one line. The return is implicit.

```python
increment = lambda x: x + 1
type(increment)
increment(2)            
increment(increment(increment(increment(1))))
```

##### Docstrings and Multiple Returns

Explain what your function does with a docstring. When using jupyter or ipython, adding `?` to the function outputs the docstring.

```python
def sum_and_product(a, b):
    """ Returns a tuple containing the sum and product of the inputs """
    return a+b, a*b
```

##### Keyword Arguments and Default Values

```python
def greet(greeting="Hello", recipient="World"):
    print(greeting + " " + recipient)
greet()
greet("Hi")
greet(recipient="Y'all", greeting="Howdy")
```

##### Recursion - When a process is defined in terms of itself.
```python
def factorial(number):
    if number == 1:           # this is the base case
        return number
    else: 
        return number * factorial(number - 1)  # recur towards the base case
```