/*
Exercises
Create a file named join_exercises.sql to do your work in.

*/

/*
Join Example Database
/*
1. Use the join_example_db. Select all the records from both the users and roles tables.
*/


/*
2. Use 
- INNER join, 
- LEFT join, and 
- RIGHT join 
to combine results from the users and roles tables as we did in the lesson. 

Before you run each query, guess the expected number of results.
*/


/*
3. Although not explicitly covered in the lesson, 
aggregate functions like count can be used with join queries. 
Use count and the appropriate join type to get a 
- list of roles along with 
- the number of users that has the role. 
(Hint: You will also need to use group by in the query.)
*/


/*
Employees Database
1. Use the employees database.
*/


/*
2. Using the example in the Associative Table Joins section as a guide, 
write a query that shows 
- each department along with 
- the name of the CURRENT manager for that department.

  Department Name    | Department Manager
 --------------------+--------------------
  Customer Service   | Yuchang Weedman
  Development        | Leon DasSarma
  Finance            | Isamu Legleitner
  Human Resources    | Karsten Sigstam
  Marketing          | Vishwani Minakawa
  Production         | Oscar Ghazalie
  Quality Management | Dung Pesch
  Research           | Hilary Kambil
  Sales              | Hauke Zhang
*/


/*
3.Find the 
- name of all departments 
- currently managed by women.

Department Name | Manager Name
----------------+-----------------
Development     | Leon DasSarma
Finance         | Isamu Legleitner
Human Resources | Karsetn Sigstam
Research        | Hilary Kambil
*/


/*
4. Find the 
- current titles of employees 
- currently working in the CUSTOMER SERVICE department.

Title              | Count
-------------------+------
Assistant Engineer |    68
Engineer           |   627
Manager            |     1
Senior Engineer    |  1790
Senior Staff       | 11268
Staff              |  3574
Technique Leader   |   241
*/


/*
5. Find the Current SALARY of all Current MANAGERS.

Department Name    | Name              | Salary
-------------------+-------------------+-------
Customer Service   | Yuchang Weedman   |  58745
Development        | Leon DasSarma     |  74510
Finance            | Isamu Legleitner  |  83457
Human Resources    | Karsten Sigstam   |  65400
Marketing          | Vishwani Minakawa | 106491
Production         | Oscar Ghazalie    |  56654
Quality Management | Dung Pesch        |  72876
Research           | Hilary Kambil     |  79393
Sales              | Hauke Zhang       | 101987
*/


/*
6. Find the NUMBER of Current EMPLOYEES in EACH Department.

+---------+--------------------+---------------+
| dept_no | dept_name          | num_employees |
+---------+--------------------+---------------+
| d001    | Marketing          | 14842         |
| d002    | Finance            | 12437         |
| d003    | Human Resources    | 12898         |
| d004    | Production         | 53304         |
| d005    | Development        | 61386         |
| d006    | Quality Management | 14546         |
| d007    | Sales              | 37701         |
| d008    | Research           | 15441         |
| d009    | Customer Service   | 17569         |
+---------+--------------------+---------------+
*/


/*
7. Which Department has the HIGHEST AVERAGE SALARY? 
(Hint: Use current not historic information.)

+-----------+----------------+
| dept_name | average_salary |
+-----------+----------------+
| Sales     | 88852.9695     |
+-----------+----------------+
*/


/*
8. Who is the HIGHEST PAID EMPLOYEE in the Marketing Department?

+------------+-----------+
| first_name | last_name |
+------------+-----------+
| Akemi      | Warwick   |
+------------+-----------+
*/


/*
9. Which CURRENT Department MANAGER has the HIGHEST SALARY?

+------------+-----------+--------+-----------+
| first_name | last_name | salary | dept_name |
+------------+-----------+--------+-----------+
| Vishwani   | Minakawa  | 106491 | Marketing |
+------------+-----------+--------+-----------+
*/


/*
10. Determine the AVERAGE SALARY for Each DEPARTMENT. 
- Use ALL salary information and 
- ROUND your results.

+--------------------+----------------+
| dept_name          | average_salary | 
+--------------------+----------------+
| Sales              | 80668          | 
+--------------------+----------------+
| Marketing          | 71913          |
+--------------------+----------------+
| Finance            | 70489          |
+--------------------+----------------+
| Research           | 59665          |
+--------------------+----------------+
| Production         | 59605          |
+--------------------+----------------+
| Development        | 59479          |
+--------------------+----------------+
| Customer Service   | 58770          |
+--------------------+----------------+
| Quality Management | 57251          |
+--------------------+----------------+
| Human Resources    | 55575          |
+--------------------+----------------+
*/


/*
*******Bonus*******
11. Find the 
- names of ALL CURRENT Employees, 
- their department name, and 
- their current manager's name.

240,124 Rows

Employee Name | Department Name  |  Manager Name
--------------|------------------|-----------------
 Huan Lortz   | Customer Service | Yuchang Weedman

 .....