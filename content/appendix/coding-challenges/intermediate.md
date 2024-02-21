# Intermediate Coding Challenges

1. Write a function that takes an array of integers and a target integer, then returns the indices of the two integers that add up to the target. You may assume that each input would have exactly one solution, and you may not use the same element twice.

	Example:

	```
	Input: [ 1, 4, 8, 12 ], 20 | Output: [ 2, 3 ]
	```

2. Write a function that sorts a string in decreasing order based on the frequency of the characters within it.

	Examples:

	```
	Input: "bee" | Output:"eeb"
    Input: "Abaaacdb" | Output: "aaabbAcd"
	```

3. Return the length of the longest possible palindrome within a given string.

	Examples:

	```
	Input: "bbadbb" | Output:5 (bbabb or bbdbb)
    Input: "bcd" | Output: 1 (b, c, or d)
	```

4. Write a function that finds the least number of perfect squares that add up to the given integer.

	Examples:

	```
	Input: 12 | Output:3 (4 + 4 + 4)
    Input: 13 | Output: 2 (4 + 9)
	```

5. Write a function that will divide two integers without using the
   multiplication, division, or modulo operators (yes, we will check your code
   :P).

6. Return the integer equivalent of a given Roman numeral string. (Max = 1000)

	Example:

	```
	Input: XXIV | Output: 24
	```

7. Write a function that will take a positive integer, convert it to binary,
   reverse the binary string, then return this reversed string in decimal form.

	Example:

	```
	Input: 35 | Output: 49
	```

8. Given an integer parameter, write a function that will return the next greater number using the same digits.

	Example:

	```
	Input: 230 | Output: 302
	```

9. Return the sum of all of the numbers in a given string divided by the number
   of letters. The answer should be rounded to the nearest whole number.

	Example:

	```
	Input: H3llo fr13nd9 | Output: 2 (9+3+3+1 = 16, 16 / 8 letters = 2)
	```

10. Write a function that determines whether or not a given string is a valid
    password. A password must follow these rules:

    1. It must have a capital letter.

    2.  It must have at least one number.

    3.  It must contain a punctuation mark.

    4.  It cannot have the word "password" in it.

    5.  It must be longer than 7 characters and shorter than 21 characters.

	Examples:

	```
	Input: passWord101! | Output: false
    Input: codE35? | Output: true
	```

11. Let’s start this off with Pokemon Go! ("Team Instinct woo!") :D To evolve a
    pokemon costs candy, but every time you catch a pokemon you get some candy.
    When you evolve a pokemon you are given a candy in return. You can also get
    rid of surplus pokemon in exchange for 1 candy of their type. Your job is to
    write a function that takes 2 integers as arguments: the number of Pidgeys
    you have and the amount of candy you have, and return the maximum XP gained
    from evolving the highest possible number of Pidgeys.

    (Note: evolving a Pidgey costs 12 candy and returns 500 XP)

	Example:

	```
    Input: 2, 23 | Output: 1000
	```

12. Return an array of standard CSS hex notation colors from a given string of
    ASCII characters. For every 3 characters, include the associated color. If
    the input string is not evenly divisible by three, ignore any trailing
    characters.

	Example:

	```
	Input: B%1A | Output: [ "#422531" ]
	```

13. Write a function that returns the number of different integer triangles with
    an angle of 120 degrees and a perimeter under or equal to a certain value.
    Each side of an integer triangle is an integer value.

	Example:

	```
	Input: 30 | Output: 3
	```

14. Create a function to validate if the given parameters are valid geo
    coordinates. Latitude (first) can be between 0 and 90, positive or negative.
    Longitude (second) can be between 0 and 180, positive or negative.
    Coordinates can only contain digits or one of the following symbols -, .
    There should not be a space between the minus "-" sign and the digit after it.

	Examples:

	```
	Input: 24.78245, 23.64572 | Output:true
    Input: 2,-37J425.87, 874.123 | Output: false
	```

15. Create a function that converts a number to the corresponding 32-bit binary
    value. It should be able to convert both positive AND negative numbers. Do
    not use internal functions to do the conversion, as we WILL be checking your
    code on this last answer.

	Example:

	```
	Input: 0.15625 | Output:00111110001000000000000000000000
	```

16. Write a function that capitalizes the first letter of each word in a string.

17. Write a function that changes every letter in a string to the next letter in
    the alphabet. Capital letters must remain capitalized.

18. Build a pyramid using the characters from a given string.

	Example:

	```
	Given string: "azb" | Output: b	zzz	aaaaa
	```

    There is no limit to the amount of characters you may be given.

19. Create a bit calculator. You will be given two numbers that have been
    translated into bit form. You must return the sum of those two numbers in
    decimal form.

	Example:

	```
	Given numbers: 1011, 10 | Output:13
	```

20. Given any number, find out how many different ways you can write it as a sum
    of positive integers.

	Example:

	```
	Given number: 4 | Output:5
	```

	These are the 5 different ways you can write it:

	```
	4
    3 + 1
    2 + 2
    2 + 1 + 1
    1 + 1 + 1 + 1
	```

21. Given an integer, determine whether or not the number is a perfect square.

	Examples:

	```
	Input: 3 | Output:false
    Input: 25 | Output: true
	```

22. Write a function that takes a single string as its argument and returns an
    ordered list of the indexes of all capital letters in the string. Assume
    that all input will have at least one capital letter.

	Example:

	```
	Input: HelLO | Output:0,3,4
    Input: codinG | Output: 5
	```

23. Write a function that converts miles per gallon (US gallon) to kilometers per liter. Output must be rounded to two decimal points.

	Example:

	```
	Input: 5 | Output:2.13
    Input: 18 | Output: 7.65
	```

24. ATMs only allow for 4 or 6 digit PINs. These PINs can only contain integers.
    Write a function that takes a PIN and checks to see if it is valid.

	Example:

	```
	Input: 8472 | Output:true
    Input: 76a1 | Output: false
	```

25. Determine whether or not a word is an anagram of another. Return true if it is, and false if it is not.

	Example:

	```
	Input: deco, code | Output:true
    Input: last, nope | Output: false
	```

26. A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

	For Example:

	```
	44 -> 32 -> 13 -> 10 -> **1** -> **1**
    85 -> **89** -> 145 -> 42 -> 20 -> 4 -> 16 -> 37 -> 58 -> **89**
	```

    Therefore any chain that arrives at 1 or 89 will become stuck in an endless
    loop. What is most amazing is that EVERY starting number will eventually
    arrive at 1 or 89.

    How many starting numbers below one million will arrive at 89?

27. The series, 1<sup>1</sup> + 2<sup>2</sup> + 3<sup>3</sup> + ... + 10<sup>10</sup> = 10405071317.

    Find the last ten digits of the series, 1<sup>1</sup> + 2<sup>2</sup> + 3<sup>3</sup> + ... + 1000<sup>1000</sup>.

28. It is possible to write five as a sum in exactly six different ways:

	```
	4 + 1
    3 + 2
    3 + 1 + 1
    2 + 2 + 1
    2 + 1 + 1 + 1
    1 + 1 + 1 + 1 + 1
	```

    How many different ways can one hundred be written as a sum of at least two integers?

29. Find the number of integers 1 < n < 10<sup>7</sup>, for which n and n + 1
    have the same number of positive divisors. For example, 14 has the positive
    divisors 1, 2, 7, 14 while 15 has 1, 3, 5, 15.

30. Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2, 3, 4.

    Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4,
    5, 6.

    Peter and Colin roll their dice and compare totals: the highest total wins.
    The result is a draw if the totals are equal.

    What is the probability that Pete beats Colin? Give your answer rounded to 7
    decimal places.

31. Write a program to calculate multiplication or division of two numbers.
    User should have input boxes to enter two different numbers and then clicks
    either a ‘add’ button or a ‘subtract’ button. The solution is then printed
    out. You may use any format.

32.  Write a function to find the TWO highest values in an array..

    ```
    a.  Example [ 12, 34, 56, 1 ]
        Answer: 34, 56
    b.  Example[ 0, -12,-34, -50,-1 ]
        Answer: 0, -1
    ```

33.  Write a function to get the least common denominator (LCD) of an array of numbers.

    ```
    a. Example: [ 1, 1/2, 3/8, 5/6, 3 ]
        Answer: 24
    b.  Example: [ 1/3, 5/6, 12/60 ]
        Answer: 60
    ```

34.  Write a function that returns the shortest word in a string. Ignore punctuation. If there are two or more words that are the same length, return the LAST word from the string with that length.

    ```
    a. Input: "My phone battery is always dead"
        Answer: is
    b. Input: "Travis wears a parka in the office"
        Answer: a
    ```

35.  Take an input string parameter and determine if exactly 3 question marks
     exist between every pair of numbers that add up to 10) If so, return TRUE,
     otherwise, return FALSE.

    ```
    a. Input: "arrb6???4xxbl5???eee5" | Return: TRUE
    b. Input: [ acc?7??sss?3rr1??????5 ] | Return: TRUE
    c. Input: "5?aaaaaaaaaaaaaa?5?5" | Return: FALSE
    ```
