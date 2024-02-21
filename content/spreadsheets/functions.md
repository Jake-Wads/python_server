# Functions

Excel refers to these as *formulas*, Google Sheets refers to them as *functions*

Categories of functions include:

- Most recently used
- Financial
- Logical
- Text
- Date & Time
- Lookup & Reference
- Math & Trig
- Statistical
- Engineering
- Information

## Referencing Cells

### How it works

- `=A2` is a relative reference. If you copy the formula to the cell below, you will see the formula changes to `=A3`.

- `=$A$2` is an absolute reference. No matter where you copy that formula, it will always reference cell A2, i.e. it will always show as `=$A$2`.

- `=$A2` is an absolute reference for the column A and a relative reference for row 2. If you copy the formula down one row, the new cell will have the formula `=$A3`. If you copy the formula over one column from its original point, the new cell will have the formula `=$A2`. If you copy the formula over one column and down one row, the new cell will have the formula `=$A3`.

- `=A$2` is an absolute reference for row 2 and a relative reference for  column A. If you copy the formula down one row, the new cell will have the formula `=A$2`. If you copy the formula over one column from its original point, the new cell will have the formula `=B$2`. If you copy the formula over one column and down one row, the new cell will have the formula `=B$2`.

Example: we have a formula in B2 `=A2`

| manually entered in: | `B2` | `=A2` | `=$A2` | `=A$2` |`=$A$2`|
| :------------------- |:----:|:-----:| :-----:| :-----:|:-----:|
| copied to:           | `B3` | `=A3` | `=$A3` | `=A$2` |`=$A$2`|
| copied to:           | `Bn` | `=An` | `=$An` | `=A$2` |`=$A$2`|
| copied to:           | `C2` | `=B2` | `=$A2` | `=B$2` |`=$A$2`|
| copied to:           | `C3` | `=B3` | `=$A3` | `=B$2` |`=$A$2`|
| copied to:           | `Cn` | `=Bn` | `=$An` | `=B$2` |`=$A$2`|
| copied to:           | `Zn` | `=Yn` | `=$An` | `=Y$2` |`=$A$2`|

## Logical

- `=IF(logical_test, value_if_true, value_if_false)`

- Comparison operators: =, >, <, >=, <=, <>

- Comparison Functions:
    - `=ISNA()`
    - `=ISNUMBER()`
    - `=ISTEXT()`
    - `=ISBLANK()`
    - `=ISNONTEXT()`
    - `=ISLOGICAL()`

- `=IFERROR(A3/B3, .00001)`: if `=A3/B3` results in an error (e.g. if B3 = 0), return .00001 instead of the error.

## Text

- `FIND("!", mytext)`: Find the '!' in mytext and return the number of characters it is from the start of the string.
- `LEN(mytext)`: Number of characters in mytext.
- `=SUBSTITUTE(mytext, "!", "?")`: Replace any "!" with "?" in mytext.
- `=VALUE("6")`: Converts a number that is being stored as text to a number.
- `=TRIM(mytext)`: Remove any leading or trailing whitespaces like the one leading this phrase.
- Split text into multiple cells:  Data -> `Text to Columns`
- `=CONCAT("H","e","l","l","o")`: Merge text from multiple cells into a single cell with no defined delimeter.  "Hello"
- `=mytext & " I think..."`: Concatenate text using '&'...You can merge both cell references and constant strings.  " Caught you smiling! I think..."
- `=TEXTJOIN(delimeter="-", ignore_empty=TRUE, "210", "867", "5309")`: Place the delimeter between each string of text upon concatenation.  "210-867-5309"
- `=LEFT(mytext, 3)`: Return the first 3 characters from the left.
- `=RIGHT(mytext, 3)`: Return the first 3 characters from the right.
- `=MID(mytext, 2, 3)`: Return the first 3 characters from the left, starting at character 2, so basically return characters 2, 3, & 4.

## Lookup and Reference

### VLOOKUP: Vertical Lookup

Looks for a value in the leftmost column of a table, and then returns a value in the same row from a column you specify. By default, the table must be sorted in an ascending order.

`=VLOOKUP(lookup_value,table_array,col_index_num,range_lookup)`

- Lookup_value: is the value to be found in the first column of the table, and can be a value, a reference, or a text string.
- Table_array: is a table of text, numbers, or logical values, in which data is retrieved. Table_array can be a reference to a range or a range name.
- Col_index_num: is the column number in table_array from which the matching value should be returned. The first column of values in the table is column 1.
- Range_lookup: is a logical value: to find the closest match in the first column (sorted in ascending order) = TRUE or omitted; find an exact match = FALSE.

### HLOOKUP: Horizontal Lookup

Looks for a value in the top row of a table or array of values and returns the value in the same column from a row you specify.

`=HLOOKUP(lookup_value,table_array,row_index_num,range_lookup)`

- Lookup_value: is the value to be found in the first row of the table and can be a value, a reference, or a text string.
- Table_array: is a table of text, numbers, or logical values in which data is looked up. Table_array can be a reference to a range or a range name.
- Row_index_num: is the row number in table_array from which the matching value should be returned. The first row of values in the table is row 1.
- Range_lookup: is a logical value: to find the closest match in the top row (sorted in ascending order) = TRUE or omitted; find an exact match = FALSE.

## Date & Time

### Extracting date parts from a date

mydate `= '01/01/2019'`

- `=WEEKDAY(mydate)`
- `=DAY(mydate)`
- `=MONTH(mydate)`
- `=YEAR(mydate)`

### Formatting dates

See "more number formats" in the data type drop down menu to define a custom date format.

- `yy`: 19
- `yyyy`: 2019
- `m`: 1
- `mm`: 01
- `mmm`: Jan
- `mmmm`: January
- `d`: 1
- `dd`: 01
- `ddd`: Tue
- `dddd`: Tuesday

### Computing dates

How many days are between 2018-11-22 and 2017-11-28?

- dateDiff `= endDate - startDate`
- Result is in days.
- Convert to other units via division or multiplication: e.g. convert result to months by dividing results by 30.4. `=dateDiff/30.4`

What was the date 90 days ago?

- newdate `= mydate-90`
- To add or subtract any units other than days, convert those units to days: e.g. convert hours to days by `=h/24`, convert years to days by `= y * 365`

### Special cases in date calculations

- Workdays are non-weekend
- Networkdays are non-weekend, non-holidays
- These can be identified and included in calculations in order to count 'workdays' between two dates, e.g.

## Math & Trig

- `ROUND(number,num_digits), ROUNDDOWN(number,num_digits), ROUNDUP(number,num_digits)`
- `TRUNC(number)`: will truncate the number by dropping the all decimal places.
- `RAND()`: Returns a random number greater than or equal to 0 and less than 1, evenly distributed (changes on recalculation).
- `RANDBETWEEN(bottom, top)
- `COMBIN(number,number_chosen)`: Returns the number of combinations for a given number of items WITHOUT repetitions. Number is the total number of items, and Number_chosen is the number of items in each combination.
- `COMBINA(number,number_chosen)`: Returns the number of combinations WITH repetitions for a given number of items.
- `LOG10(number)`: Returns the base-10 logarithm of a number.
- `QUOTIENT(numerator,denominator)`
- `PRODUCT()`
- `SUM()`
- `SUMIF(range,criteria,sum_range)`
- `SUMIFS(sum_range,criteria_range,criteria,...)`
- `SUMPRODUCT(array1, array2)`: Returns the sum of the products of corresponding ranges or arrays.
- `SUMSQ()`: Returns the sum of the squares of the arguments. The arguments can be numbers, arrays, names, or references to cells that contain numbers.
- `SUMX2MY2()`: Sums the differences between the squares of two corresponding ranges or arrays.

## Statistical

- `AVERAGE(), AVERAGEA(), AVERAGEIF(), AVERAGEIFS()`
- `COUNT(), COUNTA(), COUNTIF(), COUNTIFS(), COUNTBLANK()`
- `MIN(), MINA(), MINIFS(), MAX(), MAXA(), MAXIFS()`
- `PERCENTILE.INC(), PERCENTILE.EXC(), QUARTILE.INC(), QUARTILE.EXC()`
- `RANK(), PERCENTRANK.INC(), PERCENTRANK.EXC()`
- `PERMUT(), PERMUTATIONA()`
- `CORREL()`
- `CHISQ.DIST(), CHISQ.INV(), CHISQ.TEST()`
- `CONFIDENCE.NORM(), CONFIDENCE.T()`
- `F.DIST(), F.INV(), F.TEST()`
- `GAMMA.DIST(), GAMMA.INV(), GAMMA.TEST()`
- `NORM.DIST(), NORM.INV(), NORM.TEST()`
- `T.DIST(), T.INV(), T.TEST()`

## Exercises

### Working with dates

1. Use `Table5_Dates` for this exercise.
1. Add a new column that is the original date formatted as YYYYMMDD.
2. Insert 4 new columns that contain the weekday, day, month, year.
3. Insert 1 new column that computes the number of workdays from the current date (i.e. current row) through the latest date listed in the table. Reference the holidays table in your computation.
3. Insert a new column that contains a 1 if the date is a workday and a 0 if not.

### Using the users worksheet

1. Use `Table7_Users` for this exercise.
1. Insert a new column that is a clean version of customer_id, trimming any leading or trailing whitespace. All following tasks using the users table should reference the clean customer_id instead of the original.
2. Split the customer id into 2 columns where the characters before the hyphen are one column and the characters after the hyphen are another.
3. Add the email address for each customer, using the username and domain.tld columns.

### Using your customer details worksheet

1. Make a copy of `Table1_CustDetails` to work with so that the original is unchanged.
1. Add new columns, `is_female`, `has_churned`, `has_phone`, `has_internet`, and `has_phone_and_internet`. Populate these fields with the applicable boolean value (TRUE or FALSE).
2. Insert a new column `partner_dependents` that returns a 0 for no partners and no dependents, 1 indicates partner only, 2 indicates dependents only, 3 indicates partner and dependents.
4. Insert a new column that computes average monthly charges using total_charges and tenure. (do not copy the "monthly_charges" column). Format the data type appropriately.  Use a function to validate that your calculations match the original field `monthly_charges`.
5. Using the reference tables of contract type, phone service and internet service, add the descriptions of each to your customer details table using vlookups.
