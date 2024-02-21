# Python Project

## Command Line Checkbook Application

You will create a command line checkbook application that allows users to
track their finances with a command line interface.


## Project Requirements

- Build a `.py` file that will be run from the command line. 

- If the ledger file does not exists prior to running the `.py` file, it should be created. 

- When run, the application should welcome the user, and prompt them for an action
to take:
    - view current balance
    - add a debit (withdrawal)
    - add a credit (deposit)
    - exit

- The application should notify the user if the input is invalid and prompt
for another choice. 

- The application should persist between times that it is run. 
    - Example, if you run the application, add some credits, exit the application 
      and run it again, you should still see the balance that you previously created. 
      In order to do this, your application will need to store its data in a text file. 
      Consider creating a file where each line in the file represents a single transaction.

- Utilize functions to call the balance, debit, credit, and exit

## Example Ouput

Here is an example of what using the program might look like:

        $ python checkbook.py

        ~~~ Welcome to your terminal checkbook! ~~~

        What would you like to do?

        1) view current balance
        2) record a debit (withdraw)
        3) record a credit (deposit)
        4) exit

        Your choice? 5
        Invalid choice: 5

        Your choice? 1

        Your current balance is $100.00.

        What would you like to do?

        1) view current balance
        2) record a debit (withdraw)
        3) record a credit (deposit)
        4) exit

        Your choice? 2

        How much is the debit? $50

        What would you like to do?

        1) view current balance
        2) record a debit (withdraw)
        3) record a credit (deposit)
        4) exit

        Your choice? 1

        Your current balance is $50.00.

        What would you like to do?

        1) view current balance
        2) record a debit (withdraw)
        3) record a credit (deposit)
        4) exit

        Your choice? 4

        Thanks, have a great day!

## Bonus Features 

**Attempt these features only if you have completed the basic application.** 

In no particular order, things to try:

- Add a menu item that allows the user to view all historical transactions
- Assign categories to each transaction
    - Add a menu item to allow the user to view all the transactions in a given
      category
    - Provide the user with summary statistics about the transactions in each
      category
- Keep track of the date and time that each transaction happened
    - Allow the user to view all the transactions for a given day
    - Hint: Make sure your list of previous transactions includes the timestamp for
      each
- Allow the user to optionally provide a description for each transaction
    - Allow the user to search for keywords in the transaction descriptions, and
      show all the transactions that match the user's search term
- Allow the user to modify past transactions

