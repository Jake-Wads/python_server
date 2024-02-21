# Professional Coding Challenges

1. Write a function that returns all possible partitions of an array from left
   to right. With an *n* amount of elements in the input the returned array
   should have *n-1* subarrays. An empty array should return an empty array.

	Example:

	```
	Input: [1, 5, 3, 2] | Output: [[[ 1 ], [5, 3, 2]], [[1, 5], [3, 2]], [[1, 5, 3], [ 2 ]]]
    Input: [a, b, c] | | Output: [[[ a ], [b, c]], [[a, b], [ c ]]]
	```

2. Write a function to return a string in star shorthand. If a character is
   repeated *n* amount of times, convert the character *x* into *x*n*. Leave
   single characters alone. An empty string should return an empty string.

	Example:

	```
	Input: "zmmxxxy" | Output: "zm*2x*3y"
    Input: "aab" | Output: "a*2b"
    Input: "qwer" | Output: "qwer"
	```

3. Even if a number is not a palindrome, one of the number’s descendants may be.
   A number’s descendant can be found by adding each pair of adjacent digits
   together to make the digits of the next number. Write a function that returns
   *true* if the input number or any of its descendants down to 2 digits is a
   palindrome, return *false* otherwise. Your input will always have an even
   number of digits. If there is a single number trailing after addition leave
   it.

	Example:

	```
	Input: 443244 | Calcs: 858 | Output: true
    Input: 56 | Calcs: 11 | Output: true
    Input: 12344321 | Output: true
    Input: 121113 | Calcs: 324 -54 | Output: false
	```

4. An IPv4 formatted address contains 4 integers ranging from 0 to 255 separated
   by periods (.). Write a function that takes a string as input and returns
   *true* if the string is a valid IPv4 address. Return *false* otherwise.

	Example:

	```
	Input: 123.123.123.123 | Output: true
    Input: 0.0.0.256 | Output: false
	```

5. Write a function that calculates the Golomb sequence to the *nth* term. The
   Golomb sequence is a non-decreasing sequence of integers where *a(n)* is the
   total amount of times that *n* appears in the sequence, beginning with *a(1)
   = 1*. The equation to find the next number in the sequence is as follows:
   *a(n + 1) = 1 + a(n + 1 - a(a(n)))*.

	Example:

	```
	Input: 5 | Output: [1, 2, 2, 3, 3]
    Input: 15 | Output: [1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5, 6, 6, 6, 6]
	```

6. Given a string of words, find the highest scoring word. Each letter of the
   word has a score corresponding to its place in the alphabet (a = 1, b = 2, c
   = 3, …, z = 26). If two words have the same score, return the word that comes
   first in the string. All letters will be lowercase, all inputs will be valid.

	Example:

	```
	Input: two toads talking | Output: talking
	```

7. Given a string, return the minimum number of parentheses reversals that would
   be needed to make to make the parentheses balanced.

	Example:

	```
	Input: ")()(()" | Output: 2
    Input: "((()" | Output: 1
	```

8. Given an array of numbers, find the maximum sum of a contiguous subsequence
   of any length. If the array is made up entirely of positive numbers, simply
   give the sum of the entire array. If they are all negatives, return 0.

	Example:

	```
	Input: [2, 6, -1, 3, -2] | Output: 10
    Input: [-4, 3, -2, -7, 1, 1] | Output: 3
	```

9. Write a function that decomposes a given a positive integer’s factorial (n!)
   into its prime factors. Your inputs will be anywhere from 2 -20 (due to
   different language’s math limitations). Your output should be an equation
   string of the prime factors listed from the smallest prime to the largest.

	Example:

	```
	Input: 5 (5! = 5 * 4 * 3 * 2 * 1 = 120) | Output: 2^3 * 3 * 5
    (Because 120 is divisible by 2 three times, 3 once and 5 once)
    Input: 17 | Output: 2^15 * 3^6 * 5^3 * 7^2 * 11 * 13 * 17
    (try to do it without a math library :D)
	```

10. Write a function that returns a duration (given as a number of seconds) in a
    human-readable way. This function will only take a non-negative integer and
    return a duration expressed as a combination of years, days, hours, minutes
    and seconds. If the number is 0, the function must return "now".

	Example:

	```
	Input: 4782 | Output: 1 hour, 19 minutes and 42 seconds
    Input: 84773672123 | Output: 2688 years, 56 days, 18 hours, 15 minutes and 23 seconds
	```

11. Given a string of names like this: "Travis:Meyer;Gene:Carangal;Tom:Young;Jeff:Meyer"

    Write a function that makes the entire string uppercase and sorts it in
    alphabetical order by last name. If the last names are the same sort them by
    the first name. Put the last name in front of the first name, remove the
    colons and semicolons, put the names in parentheses and separate the names
    with commas. The end string should look like this:

    "(CARANGAL, GENE)(MEYER, JEFF)(MEYER, TRAVIS)(YOUNG, TOM)"

12. A rectangle can be split up into a grid of 1x1 squares, with the amount of
    which being equal to the product of the two dimensions of the rectangle.
    Depending on the size of the rectangle, it can be split up into larger
    squares as well. For Example a 3x2 rectangle has 8 squares, 6 1x1 squares
    and 2 possible 2x2 squares. Write a function that returns the total number
    of squares for any given rectangle, the dimensions being two integers with
    the first always being equal to or larger than the second.

	Example:

	```
	Input: 3, 2 | Output: 8
    Input: 1, 1 | Output: 1
	```

13. Write a function that finds the maximum sum of a contiguous subsequence in
    an array of integers. If the array is made up of only negative numbers
    return 0 instead.

	Example:

	```
	Input: [1, -5, 3, 4, -7, 2, 9, 1] | Output: 12
    Input: [-1, -3, -6] | Output: 0
	```

14. Write a function that accepts two integer arrays of equal length. Compare
    the value of each member in one array to the corresponding member in the
    other, and square the difference between those two values. Return the
    average of those squared differences.

	Example:

	```
	Input: [1, 10], [10, 1] | 9, 9 = (81 + 81) / 2 = 81 | Output: 81
    Input: [1, 2, 3], [4, 8, 4] | 3, 6, 1 = (9 + 36 + 1) / 3 = 15 | Output: 15
	```

15. Write a function that takes a number and returns a string of that number in
    english. You should be able to handle any number from 0 to 6 If you get a
    number outside of that or not an integer return an empty string.

	Example:

	```
	Input: 123 | Output: "one hundred twenty three"
    Input: 97264 | Output: "ninety seven thousand two hundred sixty four"
    Input: 1.5 | Output: ""
	```

16. Write a function that converts between camelCase, snake_case, and
    kebab-case. You must be able to handle all three case types. All input you
    are given will be valid.

	Example:

	```
	Input: "codeCamel", "snake" | Output: "code_camel"
    Input: "code_snake", "kebab" | Output: "code-snake"
	```

17. A palindromic number is a number that looks the same when read forwards and
    backwards. Write a function that, when given an upper and lower limit,
    returns the largest palindromic number that’s a product of any two numbers
    within the inclusive range of the lower and upper limit. You can use the
    same number twice, a single digit number does count as a palindrome, and you
    will always be given valid, positive integers.

	Example:

	```
	Input: 2, 12 | Output: 121
    Input: 34, 112 | Output: 12321
	```

18. Write regex that will validate a given password to make sure it meets the following criteria:

     - At least 12 characters long
     - Contains a lowercase letter
     - Contains an uppercase letter
     - Contains a number
     - Contains a special character

	Example:

	```
	Input: "AbC14jde" | Output: false
    Input: "g$batYD&#ceB" | Output: true
	```

19. For a given chemical formula represented by a string, count the number of
    atoms of each element contained in the molecule and return an object (or
    associative array, dictionary, map, for w/e language you use).

    Some formulas have parens or brackets in them. The number outside the brackets tells you that you have to multiply the count of each atom inside the bracket by that number.

	Example:

	```
	Input: H2O | Output: {H: 2, O: 1}
    Input: (NH4)2SO4 | Output: {N: 2, H: 8, S: 1, O: 4}
	```

20. Given two numbers: ‘left’ and ‘right’ (1 <= left <= right <= 1) return the
    sum of all occurrences of the number ‘1’ in the binary representations of
    numbers between ‘left’ and ‘right’ (including both).

	Example:

	```
	Input: 13, 784 | Output: 3629
    Input: 480, 97566 | Output: 792308
	```

21. Write a function to translate english into Morse code. Morse is written in
    dots (.) and dashes (-) and is case insensitive. When a Morse message is
    written, a single space is used to separate character codes and 3 spaces are
    used to separate words.

	Example:

	```
	Input: "hey im hungry" | Output: ".... . -.-- .. -- .... ..- -. --. .-. -.--"
	```

22. Given an array of integers, find and return the key X where the sum of the
    integers to the left of X is equal to the sum of the integers on the right.
    If you can’t find a key that would make this happen, return -1.

	Example:

    ```
    Input: [1,2,3,4,3,2,1] | Output: 3
    ```

23. Come up with a way to parse a given chemical formula string and break it
    down into its individual atomic parts.

	Examples:

	```
	Input: "H2O" | Output: "{H: 2, O: 1}"
    Input: "(BH3)2" | Output: "{B: 2, H: 6}"
	```

24. When given a 2D "n x n" array, return a 1D array with the elements arranged
    from the outermost elements to the middle element, traveling clockwise.

	Example:

	```
	Input: [[3, 7, 2], [10, 4, 9], [7, 2, 6]] | Output: [3, 7, 2, 9, 6, 2, 7, 10, 4, 9]
	```

25. You will be building something made entirely out of cubes stacked on top of
    each other, and need to know the total number of cubes required for the
    building. The cube at the bottom will have a volume of n^3, the next one up
    will be (n-1)^3 and so on until you reach 1^3. Write a function that, given
    the total expected volume of the building will return the amount of cubes n
    needed for the project.

	Example:

	```
	Input: 36 | Output: 3
	```

26. Convert the input string to pig latin. Pig latin consists of moving the
    first letter of each word to the end and adding "ay" to the end of the word.
    The output sentence should begin with a capital letter and end with a
    punctuation mark.

	Example:

	```
	Input: "Hi there!" | Output: "Ihay heretay!"
    Input: "I like food." | Output: "Iay ikelay oodfay."
	```

27. Write a function that takes an ordered list of integers separated by commas
    and return the same range with the ranges inside the list defined by dashes
    "-". It is not considered a range unless it spans at least 3 integers. For
    Example (1, 2, 3-9)

	Example:

	```
	Input: [0, 2, 3, 5, 7, 8, 9, 11, 12, 13, 14] | Output: [0, 2, 3, 5, 7-9, 11-14]
    Input: [-9, -3, -2, -1, 0, 2, 3, 4, 7] | Output: [-9, -3-0, 2-4, 7]
	```

28. Given a positive integer, return the next larger integer with the same
    digits. If one cannot be found, return false.

	Example:

	```
	Input: 789 | Output: 879
    Input: 11 | Output: false
	```

29. A product-sum number is a number which can be expressed as both the product
    and sum of the same set of numbers. For instance with a set of three
    numbers, 6 = 1 x 2 x 3 = 1 + 2 + 3 or with a set of two numbers 4 = 2 x 2 =
    2 + 2. Your job is to write a function that takes an integer and finds the
    smallest product-sum number that can be expressed by that many numbers.

	Example:

	```
	Input: 4 | Output: 8 | (8 = 1 x 1 x 2 x 4 = 1 + 1 + 2 + 4)
    Input: 5 | Output: 8 | (8 = 1 x 1 x 2 x 2 x 2 = 1 + 1 + 2 + 2 + 2)
	```

30. Create a simple calculator that given a string of operators and numbers
    separated by spaces will return the value of the expression.  Remember your
    order of operations!

	Example:

	```
	Input: "2 + 2 * 3 / 3 - 1" | Output: 3
    Input: "10 * 3 / 2 + 4 / 2 * 1 - 8" | Output: 9
	```

31. Find the closest prime number less than a given number *n* that has the
    maximum amount of even digits.

	Example:

	```
	Input: 1000 | Output: 887
	```

32. Write a function that takes a string of braces, brackets & parentheses and
    determine whether or not it is formatted/ordered correctly.

	Example:

	```
	Input: "( { [ ] } )" | Output: true
    Input: "[ [ ] } )" | Output: false
	```

33. Create a function that finds the digital root of a given number. A digital
    root is the recursive sum of all the digits in that number. Given *n*, find
    the sum of all of the digits of *n*.

    If the remaining number has two digits or more, continue reducing the number
    in this way until one digit is remaining. You will not be given any doubles,
    this challenge only applies to integers.

	Example:

	```
	Input: 16 | Output: 7
    Input: 6241 | Output: 4
	```

35. Write a function that determines whether or not a string is a valid guess on
    a Boggle board, as per the rules of Boggle. A Boggle board is an array of
    individual characters, like so:

    ```
    [ ["I", "L", "A", "W"],

      ["B", "N", "G", "E"],

      ["I", "U", "A", "O"],

      ["A", "S", "R", "L"] ]
    ```

    Valid guesses are strings which can be formed by connecting adjacent cells
    (horizontally, vertically, or diagonally) without re-using any previously
    used cells.

    For Example, in the above board "BINGO", "LINGO", and "ILNBIA" would all be
    valid guesses, while "BUNGIE", "BINS", and "SINUS" would not.

    Your function should take two arguments (an array and a string) and return
    true or false depending on whether the string is found in the array.

    The array provided will always be a square array of single capitalized
    characters, and the string will always be a single capitalized word.

    You do NOT have to check whether the string is a real word or not, only if
    it's a valid guess.

36. When giving someone directions, would you tell them to go north then south?
    How about east then west? Better to just stay in the same place! Given an
    array of directions with not so reasonable combinations, return a more
    simplified version.

	Example:

	```
	Input: ["North", "South", "South", "East", "West", "North", "West"] | Output: [ "West" ]
	```

37. Given a list of integers and a single value, return the first two values in order of appearance that add up to form the value.

	Example:

	```
    Input: [4, 3, 2, 3, 4], 6 | Output: [4, 2]
    Input: [11, 3, 7, 5], 10 | Output: [3, 7]
	```

38. Write a function which takes a positive integer (seconds) and returns the
    time in a human-readable format (HH:MM:SS). Note: you will never be given a
    number greater than 86400, the amount of seconds in 24 hours.

	Example:

	```
	Input: 28314 | Output: 07:51:54
	```

39. Given string1 and string2, return true if a portion of the characters in
    string1 can be rearranged to form string2. Otherwise return false.

	Example:

	```
	Input: "lhkioell", "hello" | Output: true
    Input: "kjshaaeeee", "code" | Output: false
	```

40. Write a function that takes a string and returns the same string with all
    five or more letter words reversed.

	Example:

	```
	Input: "Coding is fun" | Output: "gindoC is fun"
	```

41. Write a function that takes a string and returns the first word with the
    greatest number of repeated letters. If there is not a word in the sentence
    with any repeated letters return false.

	Example:

	```
	Input: "Hello world!" | Output: "Hello"
    Input: "Have a nice day." | Output: false
	```

42. Write a function that will take a string parameter which will be two times
    separated by a hyphen. Return the number of minutes between the two times.

	Example:

	```
	Input: "2:05am-10:30am" | Output: 505
    Input: "4:00pm-1:00am" | Output: 540
	```

43. Write a function that takes a string and encodes it by changing every letter
    in the message into its corresponding numeric position in the alphabet. Keep
    any numbers or extra characters in the string.

	Example:

	```
	Input: "25 tacos" | Output: "25 20131519"
    Input: "new-year & 2018" | Output: "14523-255118 & 2018"
	```

44. Write a function that takes a number and returns the next number in the
    sequence by following a simple rule: to create the next number you need to
    read the digits of the given number, counting the number of digits in groups
    of the same digit.

	Example:

	```
	Input: 22371 | Output: 22131711
    Input: 44610211 | Output: 241611101221
	```

45. Write a function that will take a string parameter that is a simple math
    equation. It will be made up of three numbers, an operator, and an equals
    sign; all separated by spaces. You must return the digit that will complete
    the equation. (You will never be given an equation where the digit could be
    "anything" such as "x98 * 0 = 0". Also yes, the letter "x" will always be
    used to denote the missing digit.)

	Example:

	```
	Input: "15 - x = 12" | Output: 3
    Input: "22 + 3 = x5" | Output: 2
	```

46. Taking an array of positive integers as input, perform an algorithm that
    continuously gets the difference of adjacent integers to create a new array
    of integers, then do the same with the new array until a single number is
    left and return that number.

	Example:

	```
	Input: [7, 2, 6, 9, 1] | Output: 4
	```

47. Write a function that takes a string parameter and determine if the string
    being passed is a valid serial number with the following constraints:

    1. It needs to contain three sets each with three digits (1 through 2)
       separated by a period.

    2. The first set of digits must add up to an even number.

    3. The second set of digits must add up to an odd number.

    4. The last digit in each set must be larger than the two previous digits in
       the same set.

	Examples:

	```
	Input: "11.124.667" | Output: false
    Input: "114.568.112" | Output: true
	```

48. Given a string of parentheses, square brackets, and curly brackets,
    determine the minimum number of brackets that need to be removed to create a
    string of correctly matched brackets.

	Example:

	```
	Input: "[()}{](]" | Output: 4
	```

49. Write a function that takes an array of numbers as the parameter. This
    function should return true if any combination of numbers in the array can
    be added up to equal the largest number in the array, otherwise return
    false. The array will not be empty, will not contain the same elements, and
    may contain negative numbers.

	Examples:

	```
	Input: [5, 7, 16, 1, 2] | Output: false
    Input: [3, 5, -1, 8, 12] | Output: true
	```

50. You are given an array of strings which will always contain 3 elements and
    will always be in the form ["(x1, y1)", "(x2, y2)", "(x3, y3)"]. Your goal
    is to first create a line formed by the first two points, and then determine
    what side of the line point 3 is on. The result will be right, left, or
    neither.

	Examples:

	```
	Input: ["(0, -3)", "(-2, 0)", "(0, 0)"] | Output: right
    Input: ["(0, 0)", "(0, 5)", "(0, 2)"] | Output: neither
	```

51. Given a list of integers and a single sum value, return the first two values
    (from left to right) in order of appearance that add up in order to form the
    sum. Negative numbers and duplicate numbers can and will appear, and there
    will be instances in which there are no pairs of values that can be added to
    return the single sum. Make sure those are handled appropriately.

	Examples:

	```
	Input: [3, 2, 4, 2, -1, 0], 2 | Output: 3, -1
    Input: [1, 0, 4, 28, 6], 18 | Output: None
	```

52. Write a function that takes a number and returns its multiplicative
    persistence, which is the number of times you can multiply the digits in the
    number given until you can reach a single digit.

	Examples:

	```
	Input: 123 | Output: 1
    Input: 976342186 | Output: 3
	```

53. Create a function that takes an integer and returns the Roman Numeral
    representation of that integer.

    Roman Numerals:
    I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000

	Examples:

	```
	Input: 3012 | Output: MMMXII
    Input: 985 | Output: CMLXXXV
	```

54. Write a function that when given a URL parses out just the domain name and
    returns it as a string. DO NOT assume you will only be given .com or http
    sites.

	Examples:

	```
	Input: http://facebook.com/login | Output: facebook
    Input: https://greenlight.md/ | Output: greenlight
	```

55. Write calculations using functions and return the results.

    Requirements:

    - There must be a function for each number from 0 ("zero") to 9 ("nine").
    - There must be a function for each of the following mathematical operations: plus, minus, times, dividedBy.
    - Each calculation must consist of of exactly one operation and two numbers.
    - The most outer function represents the left operand, the most inner function represents the right operand.

    We WILL test you on all operations.

	Examples:

	```
	Input: eight(minus(nine())) | Output: -1
    Input: three(times(four())) | Output: 12
	```
