# List Comprehensions

A list comprehension consists of 3 parts:

- what each element looks like
- what collection(s) we are pulling from
- (optionally) a condition to be met for the element to be included

```python
[x * 2 for x in range(-10, 11) if x > 0]
```

Building this list with a `for` loop would look like this:

```python
new_numbers = []
for x in range(-10, 11):
    if x > 0:
        new_numbers.append(x * 2)
new_numbers
```

---

Here's a problem that combines tuples and list comprehensions: which right
triangle that has integers for all sides and all sides equal to or smaller than
10 has a perimeter of 24?

```python
[(a, b, c) for a in range(1, 11) for b in range(1, 11) for c in range(1, 11)
           if a**2 + b**2 == c**2 and a + b + c == 24]
```

```python
triangles = [(a, b, c) for a in range(1, 11) for b in range(1, 11) for c in range(1, 11)]
right_triangles = [(a, b, c) for a, b, c in triangles if a**2 + b**2 == c**2]
[(a, b, c) for a, b, c in right_triangles if a + b + c == 24]
```

## Exercises

Use the code below to answer all of the exercises:

```python
fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]
```

1. Rewrite the above example code below using a list comprehension. Make a
   variable named `uppercased_fruits` to hold the output of the list
   comprehension. Output should be `['MANGO', 'KIWI', etc...]`

    ```python
    output = []
    for fruit in fruits:
        output.append(fruit.upper())
    ```

2. Create a variable named `capitalized_fruits` and use a list comprehension
   to produce output like `['Mango', 'Kiwi', 'Strawberry', etc...]`

3. Use a list comprehension to make a variable named
   `fruits_with_more_than_two_vowels`. Hint: You'll need a way to check if
   something is a vowel.

4. Make a variable named `fruits_with_only_two_vowels`. The result should be
   `['mango', 'kiwi']`

5. Make a list that contains each fruit with more than 5 characters

6. Make a list that contains each fruit with exactly 5 characters

7. Make a list that contains fruits that have less than 5 characters

8. Make a list containing the number of characters in each fruit. Output would
   be `[5, 4, 10, etc... ]`

9. Make a variable named `fruits_with_letter_a` that contains a list of only the
   fruits that contain the letter "a"

10. Make a variable named `even_numbers` that holds only the even numbers

11. Make a variable named `odd_numbers` that holds only the odd numbers

12. Make a variable named `positive_numbers` that holds only the positive
    numbers

13. Make a variable named `negative_numbers` that holds only the negative
    numbers

14. Use a list comprehension with a conditional in order to produce a list of
    numbers with 2 or more numerals

15. Make a variable named `numbers_squared` that contains the numbers list with
    each element squared. Output is `[4, 9, 16, etc...]`

16. Make a variable named `odd_negative_numbers` that contains only the numbers
    that are both odd and negative.

17. Make a variable named primes that is a list containing the prime numbers in
    the numbers list.
