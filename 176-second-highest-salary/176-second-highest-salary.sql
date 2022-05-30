SELECT MAX(salary) SecondHighestSalary FROM Employee
WHERE salary NOT IN (SELECT MAX(SALARY) FROM Employee)