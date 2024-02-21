# Data Types, Operators, and Variables

Data types determine how a computer represents a value. For a data scientist, data types also reflect the information a value conveys.


Here are the Python data types we will use:


| Data type | Description |
|:-: |----------|
| `bool`|   Boolean values (True or False) |
| `int`|   whole, or counting numbers |
| `str`  |   text, characters, or sequences of characters |
| `float`|  decimal numbers |
| `list`| an ordered sequence of objects |
| `dict`| a collection of named values |
| `NoneType` |  indicates an absence of a value |


### Finding data types 

The `type` function takes a Python object as an argument and returns the object's type.


Examples

```python
type(123)
```

    int




```python
type('hello')
```

    str




```python
type(True)
```

    bool



## Variables

A variable associates an object with a human-readable name. Variables are created by choosing a valid *identifier* and using the *assignment operator*, `=`.

!!!note "Code Style"
    While there are many different [naming
    conventions](https://en.wikipedia.org/wiki/Naming_convention_(programming)), `snake_case` is used for Python code. This means that variable names should be lowercase and separate multi-word names with underscores.


### Assigning a variable


```python
favorite_number = 42
n = favorite_number + 7
```

Line 1: The variable `favorite_number` is created and assigned the value 42.

Line 2: The variable `n` is created and assigned the value of`favorite_number` plus 7.


### Updating variables


Variables can reference themselves when they are assigned or re-assigned. This may look confusing, but keep in mind that the `=` operator **does not** mean equal to. It *assigns* a value. 



```python
x = 1
print(x)
x = x + 1
print(x)
x = x * 3 + x
print(x)
```

    1
    2
    8


## Booleans

There are 2 possible boolean values, `True` or `False`. Booleans can be thought of as the answer to a yes or no question. For example:


- Is a user logged in to a webpage? `is_logged_in`
- Does a dataset contain missing values? `has_missing_values`

Boolean values can be compared with the `==` and `!=` operators, which themselves produce a boolean value.



```python
True == True
```


    True




```python
True == False
```

    False




```python
True != True
```




    False




```python
True != False
```




    True



Boolean values can be combined with the `and` and `or` operators. `and` will
evaluate to `True` if both boolean values are `True`, and `or` will evaluate to
`True` if either boolean value is `True`.

The `not` operator takes the opposite boolean value.



```python
not False
```




    True




```python
True and True
```




    True




```python
True and False
```




    False



!!!note "Code Style"
    It is common to name variables that hold boolean values such that they
    represent a yes/no question.



```python
is_first_of_the_month = True
report_has_been_sent = False

should_process_report = is_first_of_the_month and not report_has_been_sent

print(should_process_report)
```

    True


!!!tip "Try It Out"
    What would happen if you changed the `is_first_of_the_month` variables to
    `False`? The `report_has_been_sent` variable to `True`?

## Numbers

Python has two main types that represent numbers, `int` and `float`. The
difference is that `int`s cannot have decimal places in them, while `float`s
can.

You can perform arithmetic with numbers with the following operators:

| Operation      | Operator | Example  |
| ---------      | -------- | -------  |
| Addition       | `+`      | `4 + 4`  |
| Subtraction    | `-`      | `9 - 1`  |
| Multiplication | `*`      | `4 * 2`  |
| Division       | `/`      | `16 / 2` |
| Exponentiation | `**`     | `2 ** 3` |

Numbers can be compared with the following operators:

| Operator | Description              | Example  |
| -------- | -----------              | -------  |
| `==`     | Equal to                 | `1 == 1` |
| `!=`     | Not equal to             | `1 != 0` |
| `>`      | Greater than             | `1 > 0`  |
| `<`      | Less than                | `0 < 1`  |
| `>=`     | Greater than or equal to | `1 >= 1` |
| `<=`     | Less than or equal to    | `1 <= 1` |

!!!note "Code Style"
    While it is not required, it is considered good form to put spaces around
    either side of all operators in Python.




```python
4 + 5 > 10 - 2
```




    True




```python
0.1 + 0.2
```




    0.30000000000000004



## Strings

Strings are used to represent arbitrary text. The following values are strings:



```python
'hello there!'
''
'123'
"here is a number: 42. It's a nice number"
```




    "here is a number: 42. It's a nice number"



Strings are delimited with either single or double quotes. The only difference
is that in order to have a string that contains a quote, you must either use
the opposite type of quote or *escape* the string. Escaping is when a character
inside a string is preceded by a backslash, and it takes on a special meaning
instead of a literal value.

!!!note "Code Style"
    It is a good practice to pick one type of quote for your code base and
    stick to it, either single or double.



```python
print('Here is a single quote --> \' <-- ')
print("Here is a single quote --> ' <-- ")
print()
print("Here is a double quote --> \" <--")
print('Here is a double quote --> " <--')
print()
print('Newlines are indicated by the character "n" preceded by a backslash, like so')
print()
print('This string\ncontains a newline')
```

    Here is a single quote --> ' <--
    Here is a single quote --> ' <--

    Here is a double quote --> " <--
    Here is a double quote --> " <--

    Newlines are indicated by the character "n" preceded by a backslash, like so

    This string
    contains a newline


Strings can also be delimited with triple quotes, and the string can have
multiple lines in it:



```python
'''
This string
can contain
a lot of
text!
'''
```




    '\nThis string\ncan contain\na lot of\ntext!\n'



### String Operations

Strings can be compared with the `==` and `!=` operators. String can be
*concatenated*, i.e. put together, with the `+` operator. A String can be
repeated with the `*` operator and a number.



```python
'hello' == 'hello'
```




    True



!!!tip "Try It Out"
    What happens if you change the casing on the strings? That is, is the string
    `HELLO` equal to the string `hello`?



```python
'abc' != 'def'
```




    True




```python
'abc' + 'def'
```




    'abcdef'




```python
'abc' * 3
```




    'abcabcabc'



Note that while you can use the `+` operator (and the `*` operator) with
strings, it is an error to try and use the other arithmetic operators to combine
strings and numbers:



```python
'2' + 1
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-23-c944a1d25078> in <module>
    ----> 1 '2' + 1


    TypeError: must be str, not int


### String Formatting

It is very common that a string needs to contain the contents of a variable.
There are several different ways to include variables in strings.

- `%` formatting: a little older, but still fairly common
- `.format`: a newer way to format strings
- f-strings: introduced in Python 3.6; comparable to string interpolation in other languages

We'll take a look at some examples of each:



```python
name = 'World'
```


```python
'Hello, %s!' % name
```




    'Hello, World!'




```python
'Hello, {}!'.format(name)
```




    'Hello, World!'




```python
f'Hello {name}!'
```




    'Hello World!'



We've only scratched the surface of using string formatting in Python, but the
examples above show the most common use cases.

### String Methods

String objects have a bunch of useful methods that can be used to perform common
text manipulation tasks. We will take a look at the most common ones here:

- `.lower` and `.upper`: convert the string to all lower or upper-case
- `.strip`: removes any leading and trailing whitespace from the string
- `.isdigit`: tests whether or not the string is a number
- `.split`: converts a string to a list
- `.join`: converts a list to a string

!!!warning "String Methods"
    All of the string methods here **do not** modify the original string, they
    return a new string with the modification.



```python
s = '   Hello, Codeup!   '
```


```python
s.lower()
```




    '   hello, codeup!   '




```python
s.strip()
```




    'Hello, Codeup!'







```python
s.isdigit()
```




    False








```python
'123'.isdigit()
```




    True








```python
s.strip().split(', ')
```




    ['Hello', 'Codeup!']








```python
', '.join(['one', 'two', 'three'])
```




    'one, two, three'





## Lists

Lists allow us to store a sequence of objects. Each item in a list is referred to
as an *element*. The elements in a list can be any type (including another
list), but it is most common to see lists where each element is the same type.



```python
[1, 2, 3] # a list with 3 numbers
```
    [1, 2, 3]




```python
['one', 'two', 'three'] # a list with 3 strings
```

    ['one', 'two', 'three']




```python
[[1, 2, 3], [4, 5, 6], [7, 8, 9]] # a list of lists of numbers
```

    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]





### List Operations

Items can be added to a list with `.append` and removed with `.pop`.


Create a list named `numbers` with the elements 1, 2, 3, 

```python
numbers = [1, 2, 3]
```



```python
numbers.append(4) 
numbers
```

    [1, 2, 3, 4]




```python
numbers.pop()
numbers
```
    [1, 2, 3]





The length of a list can be obtained with the `len` built-in function.



```python
len(numbers)
```




    3





Individual elements in a list can be referenced by their *index*, which starts
from zero. That is, the element at index 0 is the first element in the list, and
the last element is located at the index that is one less than the length of the
list.



```python
numbers[0] # the first element in the list
```

    1



```python
numbers[2] # the last element in the list
```




    3





*Slices* of a list can be obtained by using a `:` to indicate a range inside of
the square brackets

```python
numbers[:2] # everything up to, but not including, the element at index 2
```

    [1, 2]








```python
numbers[1:2] # everything from index 1 up to, but not including, index 2
```




    [2]








```python
numbers[1:] # everything from index 1 to the end of the list
```




    [2, 3]





### Converting to a List

There are many Python functions that return an *iterable*, as opposed to a list.
For example, the range function returns an iterable `range` object, not a list.
These type of objects can be converted to a list by using the `list` function.



```python
list(range(10))
```




    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]








```python
list('abcde')
```




    ['a', 'b', 'c', 'd', 'e']








```python
list(map(str, [1, 2, 3]))
```




    ['1', '2', '3']





## Tuples

Tuples are like lists, except that they are *immutable*, meaning they cannot be
changed. Once a tuple is created, its length is fixed, and no more items can be
added to it or removed from it.



```python
(1, 'two', ['t', 'h', 'r', 'e', 'e'])
```


    (1, 'two', ['t', 'h', 'r', 'e', 'e'])





You can access elements of a tuple the same way you would a list:

```python
my_tuple = (1, 2, 3)
my_tuple[1]
```




    2





Generally speaking, tuples are used when the elements are of different types,
and lists are used when the elements are all of the same type. Lists are
generally much more common, although you will see tuples in some places.

## Dictionaries

Dictionaries are a way to group values together and give a name to each value.
The names of the values in a dictionary are referred to as *keys*. It is
common to refer to a dictionary as a group of *key-value pairs*.

Dictionaries can be created by writing a *dictionary literal*, which is
delimited with curly braces, the keys are separated from the values with a
colon, and key-value pairs are separated by commas.



```python
{'name': 'Codeup', 'age': 4}
```




    {'name': 'Codeup', 'age': 4}





Dictionaries can also be created with the built-in `dict` function:



```python
dict(name='Codeup', age=4)
```




    {'name': 'Codeup', 'age': 4}





You can access values in a dictionary by their name, using a similar syntax to the way that list elements are accessed.



```python
school = dict(name='Codeup', age=9)

school['name']
```




    'Codeup'


```python
school['age'] += 1

school
```


    {'name': 'Codeup', 'age': 5}





Notice that you can both access and use the values this way.

## Further Reading

- [A Foolish Consistency is the Hobgoblin of Little Minds: Official Python Code Style Guide](https://www.python.org/dev/peps/pep-0008/)
- [Digital Ocean Tutorial: Understand Boolean Logic in Python](https://www.digitalocean.com/community/tutorials/understanding-boolean-logic-in-python-3)
- [Digital Cheat Sheet with Examples of String Formatting](https://pyformat.info/)
- [List of String Methods](https://docs.python.org/3/library/stdtypes.html#string-methods)
- [Python string literal reference](https://docs.python.org/3/reference/lexical_analysis.html#string-and-bytes-literals)


---

## Exercises

Create a Python script file named `data_types_and_variables.py` or `data_types_and_variables.ipynb`.

1\. Identify the data type of the following values:

```python
99.9
```

```python
"False"
```

```python
False
```

```python
'0'
```

```python
0
```

```python
True
```

```python
'True'
```

```python
[{}]
```

```python
{'a': []}
```



---

2\. What data type would best represent the following?

- A term or phrase typed into a search box
- Whether or not a user is logged in
- A discount amount to apply to a user's shopping cart
- Whether or not a coupon code is valid
- An email address typed into a registration form
- The price of a product
- The email addresses collected from a registration form
- Information about applicants to Codeup's data science program

---

3\. For each of the following code blocks: 

- Read the expression and predict the evaluated results 

- Execute the expression in a Python REPL.


```python
'1' + 2
```

```python
6 % 4
```

```python
type(6 % 4)
```

```python
type(type(6 % 4))
```

```python
'3 + 4 is ' + 3 + 4
```

```python
0 < 0
```

```python
'False' == False
```

```python
True == 'True'
```


```python
5 >= -5
```

```python
True or "42"
```


```python
6 % 5
```

```python
5 < 4 and 1 == 1
```

```python
'codeup' == 'codeup' and 'codeup' == 'Codeup'
```

```python
4 >= 0 and 1 !== '1'
```

```python
6 % 3 == 0
```

```python
5 % 2 != 0
```

```python
[1] + 2
```

```python
[1] + [2]
```

```python
[1] * 2
```

```python
[1] * [2]
```

```python
[] + [] == []
```

```python
{} + {}
```

---

4\. Create variables and use operators to describe the following scenario:

You have rented some movies for your kids.

- The Little Mermaid for 3 days
- Brother Bear for 5 days
- Hercules for 1 day

If the daily fee to rent a movie is 3 dollars, how much will you have to pay?


5\. Create variables and use operators to describe the following scenario:

Suppose you're working as a contractor for 3 companies: Google, Amazon and Facebook.

They pay you the following hourly rates:

- Google: 400 dollars
- Amazon: 380 dollars
- Facebook: 350 dollars

This week you worked: 10 hours for Facebook, 6 hours for Google, and 4 hours for Amazon. 

How much will you receive in payment for this week?  


6\. Create boolean variables and use operators to describe the following scenario: 

A student can be enrolled in a class only if the class is not full and the class schedule does not conflict with her current schedule.


7\. Create boolean variables and use operators to describe the following scenario: 

A product offer can be applied only if a customer buys more than 2 items, and the offer has not expired. Premium members do not need to buy a specific amount of products.


---

8\. Use the following code to follow the instructions below:


```python
username = 'codeup'
password = 'notastrongpassword'
```

Create a variable that holds a boolean value for each of the following conditions:

- The password must be at least 5 characters
- The username must be no more than 20 characters
- The password must not be the same as the username
- **Bonus**: Neither the username or password can start nor end with whitespace


