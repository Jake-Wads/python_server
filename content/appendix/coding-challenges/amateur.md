# Amateur Coding Challenges

1. Write a function that returns the SUM of a sequence of numbers. This sequence
   is determined by three variables: start, finish, and step. The sequence
   begins at start, ends at finish, and goes up by step until it reaches finish
   or a number that when increased by step would go past finish.

	Examples:

	```
	Input: start: 1 finish: 4 step: 1 | Output: 10
    Input: start: 4 finish: 10 step: | Output: 49
	```

2. Given a string of any length with any characters in it, write a function to
   determine whether or not the string contains the whole word "english". The
   order of characters/spelling is important, a string "agkjnenglishsad" would
   return true while "asdneglihsth" would return false. Upper and lower case
   does not matter. Return values should be booleans (true/false).

	Examples:

	```
	Input: "FaagdnglishAGG"	| Output: false
    Input: "SMFENgliSHasnD" | Output: true
	```

3. Given an array of integers, write a function that returns an array of 2
   integers. The first integer will be the count of the positive integers, and
   the second integer will be the sum of the negative integers. If the input is
   empty or null, return an empty array.

	Examples:

	```
	Input: [1, -6, 5, 4, 3, -7, -10, 201, -3] | Output: [5, -26]
    Input: null | Output: []
	```

4. Write a function that translates an input string by replacing each character
   with a number representing the amount of times that character appears in the
   string. Then separate each individual number with a different character.

    Examples:

    ```
    Input: "hello world", "-" | Output: "1-1-3-3-2-1-1-2-1-3-1"
    Input: "challenge", "/" | Output: "1/1/1/2/2/2/1/1/2"
    ```

5. Given a string of names like this:
   "Travis:Meyer;Gene:Carangal;Tom:Young;Jeff:Meyer", write a function that
   makes the entire string uppercase and sorts it in alphabetical order by last
   name. If the last names are the same sort them by the first name. Put the
   last name in front of the first name, remove the colons and semicolons, put
   the names in parentheses and separate the names with commas.

    Example:

    The end string should look like this: "(CARANGAL, GENE)(MEYER, JEFF)(MEYER, TRAVIS)(YOUNG, TOM)"

6. Write a function to calculate a person’s age based on the date entered in the
   format MM/DD/YYYY.

    Example:

    ```
    Input: 11/04/1982
    Output: 34
    ```

7. Write a function to convert a string into an array of words.

    Example:

    ```
    Input: "Trick or Treat"
    Output: [‘Trick’, ‘or’, ‘Treat’]
    ```

8. Write a function to count the number of occurrences of a substring in a given string.

    Example:

    ```
    Input: "The pumpkin rolled down the hill and under someone’s car.", "the"
    Output: 2
    ```

9. Write a function to remove these special characters from a string:
	`~`,`!`,`$`,`&`,`%`,` ` ,`#`,`@`,`-`,`_`,`^`,`?`,`,` (yes, "space" is a character in that list)

    Examples:

    ```
    Input: "Happy ~!&$%#@- Halloween" | Output: "HappyHalloween"
    Input: "I’ll bet living in a nudist-colony takes all the fun out of Halloween!!" | Output: "IllbetlivinginanudistcolonytakesallthefunoutofHalloween"
    ```

10. Write a function called "multiply" that takes two integers and returns the
    product. You are NOT allowed to use the * operator or any imported
    multiplication function. We will check your code.

    Example:

    ```
    Input: multiply(5, 6) | Output: 30
    Input: multiply(-1, 15)	| Output: -15
    Input: multiply(-2, -7) | Output: 14
    ```

11. Write a function that takes a string and returns true if all of the characters are the same case, false otherwise.

	Examples:

	```
	Input: "hello world" | Output: true
    Input: "HELLO WORLD" | Output: true
    Input: "HeLLo wORld" | Output: false
	```

12. Write a function that takes an array of integers and returns an array of
    integers where each number is the sum of itself and all of the previous
    numbers in the array.

    Example:

    ```
    Input: [1, 1, 1] | Output: [1, 2, 3]
    Input: [4, 2, 1, 3, 5] | Output: [4, 6, 7, 10, 15]
    ```

13. An Isogram is a word that has no repeating letters, consecutive or not.
    Write a function that takes a string and returns true if it’s an isogram and
    false if it isn’t.

    Examples:

    ```
    Input: "fish" | Output: true
    Input: "food" | Output: false
    Input: "color" | Output: false
    ```

14. Write a function that takes a phone number with letters in it and converts
    it to one with only numbers. All input phone numbers will follow this
    pattern: "###-###-####" (Hint: Search for "phone keypad")

    Examples:

    ```
    Input: 210-367-CODE | Output: 210-367-2633
    Input: TRY-THE-FOOD | Output: 879-843-3663
    ```

15. Write a function that returns all possible partitions of an array from left
    to right. With an n amount of elements in the input the returned array
    should have n-1 subarrays. An empty array should return an empty array.

    Examples:

    ```
    Input: [1, 5, 3, 2]	| Output: [[[1], [5, 3, 2]], [[1, 5], [3, 2]], [[1, 5, 3], [2]]]
    Input: [a, b, c] | Output: [[[a], [b, c]], [[a, b], [c]]]
    ```

