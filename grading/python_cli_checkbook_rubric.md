# Python Checkbook Project Grading Rubric

## 4 main features
- view current balance          25%
- add a debit (withdrawal)      25%
- add a credit (deposit)        25%
- exit                          25%


## Software Quality Checklist
Major oversight or bug: Minus 20 points
- Not writing to or reading from a file ƒor persistence

Minor bugs: Minus 5 points for each minor bug or oversight
- we can withdraw more than the balance
- output shows cents but we can't deposit or withdraw floats
- only able to deposit/withdraw integers, not floats
- user can provide a bad input for the menu that crashes the application 
- user can provide bad inputs for the withdrawal amount, crashing the application
- unable to exit the application
- able to withdraw/deposit a negative value

## Additional Features
- Any additional feature 5 points (up to but not exceeding 95 points)

## Example:
- Pat turns in their checkbook application. The application can view the balance, make deposits, make withdrawals, but lacks functionality to exit vs doing ctrl+c to exit the application. This puts Pat at a 75 grade. Also, Pat added one of the additional features, so this bumps up their grade by 5 points. The final grade is an 80.
- Kelly runs in an application with no working exit feature, but adds 10 extra additional features. The lack of the exit functionality starts the grade at 75, but the extra features bump up the grade each by 5, capping out at 95.