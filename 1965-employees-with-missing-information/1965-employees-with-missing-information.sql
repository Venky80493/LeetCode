# Write your MySQL query statement below
SELECT DISTINCT t1.employee_id
FROM
(SELECT employee_id
FROM Employees 
UNION
SELECT employee_id
FROM Salaries)t1
LEFT JOIN Employees t2
ON t1.employee_id=t2.employee_id
LEFT JOIN Salaries t3
ON t1.employee_id=t3.employee_id
WHERE t2.name is null or t3.salary is null
order  by t1.employee_id