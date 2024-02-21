/*
SQL Functions Exercises

Copy the order by exercise and save it as functions_exercises.sql.
*/
use employees;

/*
1. Write a query to find all employees whose LAST name STARTS and ENDS with 'E'. 
Use concat() to combine their first and last name together as a single column named full_name.
*/
select 
	concat(first_name, ' ', last_name) as full_name
from employees
where last_name like 'e%e';

/*
2. Convert the names produced in your last query to all UPPERCASE.
*/
select 
	UPPER(concat(first_name, ' ', last_name)) as full_name
from employees
where last_name like 'E%e';


/*
3. Use a function to determine HOW MANY results were returned from your previous query.
*/
select 
	count(UPPER(concat(first_name, ' ', last_name))) as full_name_CNT
from employees
where last_name like 'e%e';


/*
4. Find all employees hired in the 90s and born on Christmas. 
Use datediff() function to find how many days they have been working at the company 
(Hint: You will also need to use NOW() ---or--- CURDATE()),
*/
select now(), curdate();

select 
	concat(first_name, ' ', last_name) as full_name
    , datediff(curdate(), hire_date) as CompanyTenure
from employees
where hire_date like '199%'-- between '1990-01-01' and '1999-12-31'
	and birth_date like '%-12-25'
order by hire_date DESC;


/*
5. Find the smallest and largest CURRENT salary from the SALARIES table.
*/
select 
	min(salary) as SmallestSalary
    ,max(salary) as LargestSalary
from salaries
where to_date >= curdate();


/*
6. Use your knowledge of built in SQL functions to generate a username for all of the employees. 
A username should be: 
	- all lowercase
    - consist of the first character of the employees first name
    - the first 4 characters of the employees last name 
    - an underscore
    - the month the employee was born
    - the last two digits of the year that they were born. 
*/
/*select 
	lower(concat(first_name,' ',last_name)) as fullname
    , lower(left(first_name,1)) as 1stname_1
    ,lower(left(last_name, 4)) as lstname_4
    , '_'
    ,date_format(birth_date, '%m') as b_month
--    ,month(birth_date) as b_month -- changed dbl digit format :(
--    ,substr(birth_date,6,2) as b_month
    ,RIGHT(year(birth_date),2) as b_yr_2
    */
    
select    
	LOWER(concat(left(first_name,1), left(last_name, 4)
		, '_'
		, date_format(birth_date, '%m')
		,RIGHT(year(birth_date),2)
    ))as username
    ,first_name
    ,last_name
    ,birth_date
from employees;

