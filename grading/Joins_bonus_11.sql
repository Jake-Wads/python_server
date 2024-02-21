-- Bonus Find the highest paid employee in each department.-- 

USE employees; 



SELECT salaries.emp_no, max_salary.max_salary, max_salary.dept_no, emp.first_name, emp.last_name, dept.dept_name
FROM salaries
JOIN (
		SELECT MAX(A.salary) AS max_salary, A.dept_no FROM 
				(SELECT dept_emp.emp_no, dept_emp.dept_no, dept_emp.to_date, salaries.salary
				FROM dept_emp
				JOIN salaries USING (emp_no)
				WHERE dept_emp.to_date > NOW()
			) A
			GROUP BY A.dept_no
            ) max_salary 
            ON salaries.salary = max_salary.max_salary
JOIN employees emp ON salaries.emp_no = emp.emp_no
JOIN departments dept ON max_salary.dept_no = dept.dept_no
WHERE salaries.to_date > NOW()
; 


