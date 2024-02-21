# Type Annotations

Python allows us to specify the type of variables, function parameters, and
function return values through **type annotations**.

The python language itself will *not* enforce type annotations, but there are
several third party tools that can use the type annotations to analyze your code
and detect type mismatch issues.

Apart from preventing code execution errors, type annotations are a great tool
for communication about your function's api. Type annotations can clarify what
should be passed in to a function and what is returned out of it.

Let's take a look at an example of using type annotations:

```python
def add(x: int, y: int) -> int:
    return x + y
```

Here the `: int` tells us the type of each function parameter, and `-> int`
tells us the return type.

More complex types can be expressed with the classes available in the `typing`
module. For example, we can define a function that takes in a list of floats and
returns all of them rounded to the nearest whole number:

```python
from typing import List

def round_all(numbers: List[float]) -> List[int]:
    return [round(n) for n in numbers]
```

Here `List` specifies that the type of the `numbers` parameter will be a list,
and with the square brakets, we can further specify the type of every element in
the list.

## Further Reading

- [mypy](http://mypy-lang.org/)
- [pytype](https://github.com/google/pytype)
